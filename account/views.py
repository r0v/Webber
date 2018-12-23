from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login

# Create your views here.
def dashboard(request):
    return render(request, 'account/dashboard.html')

def register(request):
    
    # TODOS: Repair register for ExtendedUser model
    if request.method == 'POST':
        form = UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('account:index')
    else:
        form = UserCreationForm()
    
    context = { 'form': form }
    return render(request, 'registration/register.html', context)
