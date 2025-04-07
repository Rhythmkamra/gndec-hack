from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import StudentFormCultural, StudentFormSports, StudentFormTechnical

def student_cultural_view(request):
    if request.method == 'POST':
        form = StudentFormCultural(request.POST, request.FILES)  # <-- FIXED
        if form.is_valid():
            form.save()
            messages.success(request, 'Data submitted successfully.')
            return redirect('cultural')
    else:
        form = StudentFormCultural()
    return render(request, 'data/home.html', {'form': form})

def student_sports_view(request):
    if request.method == 'POST':
        form = StudentFormSports(request.POST, request.FILES)  # <-- FIXED
        if form.is_valid():
            form.save()
            messages.success(request, 'Data submitted successfully.')
            return redirect('sports')
    else:
        form = StudentFormSports()
    return render(request, 'data/sports.html', {'form': form})

def student_technical_view(request):
    if request.method == 'POST':
        form = StudentFormTechnical(request.POST, request.FILES)  # <-- FIXED
        if form.is_valid():
            form.save()
            messages.success(request, 'Data submitted successfully.')
            return redirect('technical')
    else:
        form = StudentFormTechnical()
    return render(request, 'data/technical.html', {'form': form})
