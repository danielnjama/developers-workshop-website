# views.py
from django.shortcuts import render, redirect
from .models import students

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        question = request.POST['question']
        student_instance = students(name=name, email=email, phone=phone, question=question)
        student_instance.save()
        # Pass a success variable to the 'success' view
        return redirect('success')
    return render(request, 'index.html')

def success(request):
    return render(request, 'success.html')
