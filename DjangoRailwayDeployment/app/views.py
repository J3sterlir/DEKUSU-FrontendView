from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import LoginForm
from .models import Announcement
from .models import UserProfile
from django.views.decorators.cache import never_cache

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            # Authenticate the user
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')  # Redirect to the dashboard after successful login
            else:
                messages.error(request, "Invalid email or password")
        else:
            messages.error(request, "Invalid form submission")
    else:
        form = LoginForm()  # Empty form for GET requests
    return render(request, 'index.html', {'form': form})
def dashboard_guest(request):
    return render(request, 'dashboard(guest).html')
@never_cache
@login_required(login_url='index')
def dashboard(request):
    return render(request, 'dashboard.html')
@never_cache
@login_required(login_url='index')
def map_view(request):
    return render(request, 'map.html')
def map_guest(request):
    return render(request, 'map(guest).html')
@never_cache
@login_required(login_url='index')
def profile(request):
    try:
        user_profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        user_profile = None
    return render(request, 'profile.html', {'user_profile': user_profile})
@never_cache
@login_required(login_url='index')
def notifications(request):
    announcements = Announcement.objects.order_by('-date_posted')
    return render(request, 'notification.html', {'announcements': announcements})
def notifications_guest(request):
    announcements = Announcement.objects.order_by('-date_posted')
    return render(request, 'notification(guest).html', {'announcements': announcements})
def logout_view(request):
    logout(request)
    return redirect('index')
