from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import UserRegisterFrom

def register(request):

    if request.method == 'POST':
        form = UserRegisterFrom(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('blog-home')
    else:
        form = UserRegisterFrom()

    to_return = render(
        request,
        'users/register.html',
        context = {'form': form}
    )

    return to_return
