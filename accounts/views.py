from pyexpat.errors import messages
from django.contrib.auth import login, logout, authenticate
from django.shortcuts import redirect, render

from accounts.forms import SIgnUpForm

def signup(request):
    if request.method == 'GET':
        form = SIgnUpForm()
    elif request.method =='POST':
        form = SIgnUpForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('signin')
    return render(request, 'accounts/signup.html', {'form':form})
    
def signin(request):
    if request.method == 'GET':
        form = SIgnUpForm()
    elif request.method =='POST':
        form = SIgnUpForm(request, data = request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(request, email=email, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('todo_list')
            else:
                messages.error(request)
    return render(request, 'accounts/signup.html', {'form':form})

def signout(request):
    logout(request)
    return redirect('signin')
    
