from django.shortcuts import render, redirect
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required

'''
What would happen if we would create a website from scratch without a framework?

We would have to put in different kinds of validation checks to make sure
user was putting the correct information correctly. Make sure that their hash passwords match.
Write regex to check if e-mail is ok...

Django takes care of that providing uses with forms that already give us that. These forms will
be classes that will be converted to html!
'''


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)  # Instantiates an user created form
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Your account has been created. Your are now able to log in!')
            return redirect('login')
    else:
        form = UserRegisterForm()

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):

    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')  # Causes the browser to send a get request instead of sending another post request once we reload the page
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'users/profile.html', context)
