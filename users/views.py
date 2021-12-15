from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm


# Create your views here.
def register(request):
    """register a new user"""
    # if not a post request then a get
    if request.method != 'POST':
        # create an empty form
        form = UserCreationForm()
    else:
        # fill the form with user data inputs
        form = UserCreationForm(data=request.POST)
        # save the data into the database, login the user and redirect to the homepage
        if form.is_valid():
            new_user = form.save()
            login(request, new_user)
            return redirect('learning_logs:index')
    # displays the empty/invalid form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
