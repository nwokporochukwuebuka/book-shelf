from django.conf import settings
from django.shortcuts import render, redirect, reverse
from django.contrib import auth, messages
from django.views.generic import TemplateView, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from shelf.models import Book
from .forms import LoginForm, UserSignupForm

# Things to introduce
# Detail of Each book and being able to also archive from that place


# Create your views here.
@login_required
def logout(request):
    """ user logout """
    auth.logout(request)
    messages.success(request, 'You have successfully logged out of the Library. Come again soon!')
    return(redirect(reverse('book:list')))

def login(request):
    """ login func """

    if request.method == "POST":
        login_form = LoginForm(request.POST)

        if login_form.is_valid():
            user = auth.authenticate(username=request.POST.get('username'), password=request.POST.get('password'))

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully logged into the Book Shelf")
                return redirect(reverse('book:list'))

            else:
                login_form.add_error(None, "Sorry, some of your details are incorrect. Please try again")

    else:
        login_form = LoginForm()
        
    return render(request, 'users/login.html', {'login_form': login_form})


# Sign Up View
def signup(request):

    if request.method == "POST":
        signup_form = UserSignupForm(request.POST)
        
        if signup_form.is_valid():
            signup_form.save()
            user = signup_form.cleaned_data.get('username')
            messages.success(request, 'Account was successfully created for ' + user)
            return redirect('users:login')

    else:
        signup_form = UserSignupForm()

    return render(request, 'users/signup.html', {"signup_form" : signup_form})


def password_reset_done(request):
    return(render(request, 'password_reset_done.html'))


def password_reset_complete(request):
    return(render(request, 'password_reset_complete.html'))