from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterFrom
from django.contrib.auth.decorators import login_required

def register(request):

    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(
                request,
                'Your account has been created. You are now able to log in.')
            return redirect('login')
    else:
        form = UserRegisterFrom()

    to_return = render(
        request,
        'users/register.html',
        context = {'form': form}
    )

    return to_return

@login_required
def profile(request):
    to_return = render(request, 'users/profile.html')
    return to_return
