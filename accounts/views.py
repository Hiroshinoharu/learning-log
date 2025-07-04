from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def register(request):
    """ Register a new user."""
    if request.method != 'POST':
        # Display a blank registration form.
        form = UserCreationForm()
    else:
        # Process the completed form.
        form = UserCreationForm(data=request.POST)
        
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)  # Log in the user after registration
            return redirect('learning_logs:index')  # Redirect to the index page

    # Display a blank or invalid form.
    context = {'form': form}
    return render(request, 'registration/register.html', context)