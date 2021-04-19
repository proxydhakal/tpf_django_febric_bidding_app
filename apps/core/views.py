from django.shortcuts import render
from django.conf import settings
from django.core.mail import  send_mail
from apps.core.models import About, Term, Parent, Child, ListFebric
from apps.setting.models import SEO, Title, Logo
from django.views.generic import TemplateView, ListView, DetailView,CreateView,UpdateView
from django.urls import reverse_lazy
from apps.core.forms import ListFebricForm
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin

def index(request):
    template_name= 'index.html'
    seo = SEO.objects.all().first()
    title = Title.objects.all().first()
    logo = Logo.objects.all().first()
    context = {'seo':seo, 'logo':logo, 'title':title}
    return render(request, template_name,context)

def about(request):
    template_name= 'about.html'
    about = About.objects.all().first()
    context ={'about':about}
    return render(request, template_name, context)

def terms(request):
    template_name= 'terms_of_service.html'
    term = Term.objects.all().first()
    context ={'terms':term}
    return render(request, template_name, context)

def submit_a_listing(request):
    template_name ='submit_a_list.html'
    return render(request, template_name)

class ListCreateView(LoginRequiredMixin,CreateView):
    model = ListFebric
    form_class = ListFebricForm
    success_url = '/'
    template_name='submit_a_list.html'

    def form_valid(self, form):
        list = form.save(commit=False)
        list.user =self.request.user
        list.save()
        return super().form_valid(form)

    def form_invalid(self, form):
        print(form)
        return super(ListCreateView, self).form_invalid(form)



def load_list(request):
    parent_id = request.GET.get('parent')
    childs = Child.objects.filter(parent_id=parent_id).order_by('name')
    return render(request, 'child_dropdown_list.html', {'childs': childs})

