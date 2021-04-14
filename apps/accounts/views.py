from django.shortcuts import render,redirect
from django.views import View
from apps.accounts.forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from apps.accounts.forms import UserCreationForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from apps.accounts.models import Profile


@login_required
def profile(request):
    template_name='accounts/profile.html'
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form =ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been Updated.')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context={
        'u_form': u_form,
         'p_form': p_form
    }
    return render(request, template_name, context)
    