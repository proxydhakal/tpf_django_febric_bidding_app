from django.contrib.auth import models
from django.shortcuts import render,redirect
from django.views import View
from django.contrib.auth import authenticate, login
from django.contrib import messages
from apps.accounts.forms import UserUpdateForm, ProfileUpdateForm
from django.contrib.auth.decorators import login_required
from apps.accounts.models import Profile
from apps.core.models import ListFebric
from django.shortcuts import render,get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView ,DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
@login_required
def profile(request):
    model = ListFebric
    logged_in_user = request.user
    logged_in_user_posts = ListFebric.objects.filter(user=logged_in_user)
    template_name='account/profile.html'
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
         'p_form': p_form,
         'posts':logged_in_user_posts
    }

    # def get_queryset(self):
    #     user = get_object_or_404(User, user=self.kwargs.get('username'))
    #     return ListFebric.objects.filter(user=user).order_by('-created_at')
    return render(request, template_name, context)
    
class UserPostListView(LoginRequiredMixin,ListView):
    model =ListFebric
    paginate_by = 2
    template_name = 'account/profile.html'
    context_object_name = 'posts'
    

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return ListFebric.objects.filter(user=user).order_by('-created_at')