from dataclasses import fields
from itertools import product
from pyexpat import model
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, UpdateView, DeleteView


from .models import Business, Product
from .forms import ProductForm
from .filter import BusinessFilter
import uuid
import boto3
S3_BASE_URL = 'http://s3.ca-central-1.amazonaws.com/'
BUCKET = 'businesscollector'









# Create your views here.
def home (request):
    return render (request, 'home.html')

def businesses_index(request):
    businesses = Business.objects.order_by('name')
    category_filter = BusinessFilter(request.GET, queryset=businesses, )

    return render(request, 'businesses/index.html', { 'businesses': businesses, 'category_filter': category_filter })

def businesses_detail(request, business_id):
  business = Business.objects.get(id=business_id)
  product = Product.objects.all()  
  product_form = ProductForm()
  if business.favourites.filter(id = request.user.id).exists():
    favourite = True
  else:
    favourite = False
  return render(request, 'businesses/detail.html', { 'business': business, 'favourite' : favourite, 'product_form': product_form, 'product': product})

def signup(request):
  error_message = ''
  if request.method == 'POST':
    # This is how to create a 'user' form object
    # that includes the data from the browser
    form = UserCreationForm(request.POST)
    if form.is_valid():
      # This will add the user to the database
      user = form.save()
      # This is how we log a user in via code
      login(request, user)
      return redirect('/')
    else:
      error_message = 'Invalid sign up - try again'
  # A bad POST or a GET request, so render signup.html with an empty form
  form = UserCreationForm()
  context = {'form': form, 'error_message': error_message}
  return render(request, 'registration/signup.html', context)


class BusinessCreate(LoginRequiredMixin, CreateView):
  model = Business
  fields =['name', 'address','city', 'province', 'postal_code', 'website', 'description', 'category', 'image']
  def form_valid(self, form):
    form.instance.user = self.request.user  
    return super().form_valid(form)

  

class BusinessesUpdate(LoginRequiredMixin, UpdateView):
  model = Business 
  fields = ['name', 'website', 'description', 'category']

class BusinessesDelete(LoginRequiredMixin, DeleteView):
  model = Business
  success_url = '/businesses/'  



@login_required
def my_profile(request):
  businesses = Business.objects.filter(user=request.user)
  return render(request, 'businesses/profile.html', { 'businesses': businesses})

@login_required
def add_product(request, business_id):
  form = ProductForm(request.POST, request.FILES)
  if form.is_valid():
    new_product = form.save(commit=False)
    new_product.business_id = business_id
    new_product.save()
  return redirect('detail', business_id=business_id)  

class edit_product(LoginRequiredMixin, UpdateView):
  model = Product
  fields =  ['description', 'url']
  success_url = '/businesses/{business_id}/'

class delete_product(LoginRequiredMixin, DeleteView):
  model = Product
  success_url = '/businesses/{business_id}/'
 
  
@login_required
def favourites_add (request, user_id, business_id):
  Business.objects.get(id=business_id).favourites.add(request.user)
  return redirect('detail', business_id=business_id)

@login_required
def favourites_delete (request, user_id, business_id):
  Business.objects.get(id=business_id).favourites.remove(request.user)
  return redirect('detail', business_id=business_id)



@login_required
def favourite_list (request):
  businesses = Business.objects.filter(favourites = request.user)
  return render(request, 'businesses/favourites.html', { 'businesses': businesses})
