from django.shortcuts import render, redirect
from .form import UserRegisterForm
from django.contrib import messages

# Create your views here.

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"Your account has been created, {username} can login now!")
            return redirect('login')
        else:
            pass
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form})