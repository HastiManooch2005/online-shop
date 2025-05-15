from django.shortcuts import render, redirect
from .forms import LoginForm
from django.contrib.auth import authenticate,login,logout

# Create your views here.
def user_login(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                form.add_error(None,"username or password is not true")
        else :
            form.add_error(None,"username or password is wrong")
    return render(request,'account/login.html',{"form":form})