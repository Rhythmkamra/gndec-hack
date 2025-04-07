from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from .forms import StudentFormCultural, StudentFormSports, StudentFormTechnical

# ------------------- AUTH VIEWS ------------------- #

def register_view(request):
    if request.user.is_authenticated:
        return redirect('cultural')  # Redirect to form if already logged in
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('cultural')  # Redirect to cultural form after registration
    else:
        form = UserCreationForm()
    return render(request, 'data/register.html', {'form': form})  # Make sure path matches your template location

def login_view(request):
    if request.user.is_authenticated:
        return redirect('cultural')  # Redirect logged-in users to form
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('cultural')  # Redirect to form after login
    else:
        form = AuthenticationForm()
    return render(request, 'data/login.html', {'form': form})  # Make sure path matches your template location

@login_required(login_url='login')
def dashboard_view(request):
    return render(request, 'data/dashboard.html')  # Optional: can keep for navigation

def logout_view(request):
    logout(request)
    return redirect('login')


# ------------------- STUDENT VIEWS ------------------- #

@login_required(login_url='login')
def student_cultural_view(request):
    if request.method == 'POST':
        form = StudentFormCultural(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data submitted successfully.')
            return redirect('cultural')
    else:
        form = StudentFormCultural()
    return render(request, 'data/home.html', {'form': form})

@login_required(login_url='login')
def student_sports_view(request):
    if request.method == 'POST':
        form = StudentFormSports(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data submitted successfully.')
            return redirect('sports')
    else:
        form = StudentFormSports()
    return render(request, 'data/sports.html', {'form': form})

@login_required(login_url='login')
def student_technical_view(request):
    if request.method == 'POST':
        form = StudentFormTechnical(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data submitted successfully.')
            return redirect('technical')
    else:
        form = StudentFormTechnical()
    return render(request, 'data/technical.html', {'form': form})
