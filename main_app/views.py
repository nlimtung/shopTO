from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Business


from django.views.generic import CreateView






# Create your views here.
def home (request):
    return render (request, 'home.html')

def businesses_index(request):
    businesses = Business.objects.all()
    return render(request, 'businesses/index.html', { 'businesses': businesses })

def businesses_detail(request, business_id):
  business = Business.objects.get(id=business_id)
  return render(request, 'businesses/detail.html', { 'business': business })

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

#Create business

def business_index(request):
  return render(request, 'business/index.html', { 'business': business })



class BusinessCreate(CreateView):
  model = Business
  fields = '__all__'
  
#   # This inherited method is called when a
#   # valid cat form is being submitted
#   def form_valid(self, form):
#     # Assign the logged in user (self.request.user)
#     form.instance.user = self.request.user  # form.instance is the cat
#     # Let the CreateView do its job as usual
#     return super().form_valid(form)