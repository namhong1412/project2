from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def signup(request):
    signup_path = 'pages/signup.html'

    if request.user.is_authenticated:
        return redirect("home")

    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            existing_user = User.objects.get(username=username)
            error_message = "This username already used."
        except User.DoesNotExist:
            try:
                existing_user = User.objects.get(email=email)
                error_message = "This email already used."
            except User.DoesNotExist:
                user = User.objects.create_user(username=username, email=email, password=password)
                user = authenticate(request, username=username, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('home')
                else:
                    error_message = "Unable to authenticate user."
        return render(request, signup_path, {'error_message': error_message})
    return render(request, signup_path)
