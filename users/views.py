from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterForm


def register(request):
    if request.user.is_authenticated:
        return redirect('/notes')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            full_name = form.cleaned_data.get('full_name')
            phoneNumber = form.cleaned_data.get('phoneNumber')
            messages.success(
                request, f'Account created for {full_name} with Phone Number {phoneNumber}.')
            return redirect('/notes')
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


# def login(request):
#     return render(request, 'login.html')
