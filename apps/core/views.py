from django.shortcuts import render
from django.conf import settings
from django.core.mail import  send_mail
from apps.core.models import About, Term
from apps.setting.models import SEO, Title, Logo
from django.views.generic import TemplateView, ListView, DetailView



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
