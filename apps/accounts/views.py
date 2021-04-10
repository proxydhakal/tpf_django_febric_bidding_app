from django.shortcuts import render,redirect
from django.views import View
from apps.accounts.forms import UserRegisterForm
from django.contrib.auth import authenticate, login
from django.contrib import messages
from apps.accounts.forms import UserCreationForm, UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
def success(request):
    template_name='accounts/success.html'
    return render(request, template_name)

class SignUpView(View):
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            return render(request,'accounts/register_user.html')
        else:
            template_name='accounts/register.html'
            form = UserRegisterForm()
            return render(request,template_name,{'form':form})

    def post(self, request, *args, **kwargs):
        form = UserRegisterForm(request.POST)
        template_name='accounts/login.html'
        if form.is_valid():
            user =form.save(commit=False)
            raw_password = form.cleaned_data['password']
            username = form.cleaned_data['username']
            user.set_password(raw_password)
            user.save()
            messages.success(request, f'Account created for {username}!')
            return redirect('/account/login')

        else:
            return render(request, 'accounts/register.html', {'form':form})

@login_required
def profile(request):
    template_name='accounts/profile.html'
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form =ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profiles)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your profile has been Updated.')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profiles)

    context={
        'u_form': u_form,
         'p_form': p_form
    }
    return render(request, template_name, context)
    