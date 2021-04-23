from django.shortcuts import render
from django.conf import settings
from django.core.mail import  send_mail
from apps.core.models import About, Term, Parent, Child, ListFebric,MultiStepFormModel
from apps.setting.models import SEO, Title, Logo
from django.views.generic import TemplateView, ListView, DetailView,CreateView,UpdateView
from django.urls import reverse_lazy
from apps.core.forms import ListFebricForm
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin



class IndexView(CreateView):
    model = ListFebric
    form_class= ListFebricForm
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["seo"] = SEO.objects.all().first()
        context["title"] = Title.objects.all().first()
        context["logo"] = Logo.objects.all().first()
        context["lists"] = ListFebric.objects.all()
        return context


# def index(request):
#     template_name= 'index.html'
#     seo = SEO.objects.all().first()
#     title = Title.objects.all().first()
#     logo = Logo.objects.all().first()
#     context = {'seo':seo, 'logo':logo, 'title':title}
#     return render(request, template_name,context)

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

class ListCreateView(LoginRequiredMixin,SuccessMessageMixin,CreateView):
    model = ListFebric
    form_class = ListFebricForm
    success_url = '/febrics/'
    template_name='submit_a_list.html'
    success_message = "List created successfully"


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


class FebricList(ListView):
    model = ListFebric
    ordering =['-created_at']
    paginate_by = 4
    context_object_name = 'list_febrics'
    template_name = 'search_febrics.html'
    queryset = ListFebric.objects.all()



from django.urls import reverse
from django.contrib import messages
from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
def multistepformexample(request):
    return render(request,"multistepform.html")

def multistepformexample_save(request):
    if request.method!="POST":
        return HttpResponseRedirect(reverse("multistepformexample"))
    else:
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        phone=request.POST.get("phone")
        twitter=request.POST.get("twitter")
        facebook=request.POST.get("facebook")
        gplus=request.POST.get("gplus")
        email=request.POST.get("email")
        password=request.POST.get("pass")
        cpass=request.POST.get("cpass")
        if password!=cpass:
            messages.error(request,"Confirm Password Doesn't Match")
            return HttpResponseRedirect(reverse('multistepformexample'))

        try:
            multistepform=MultiStepFormModel(fname=fname,lname=lname,phone=phone,twitter=twitter,facebook=facebook,gplus=gplus,email=email,password=password)
            multistepform.save()
            messages.success(request,"Data Save Successfully")
            return HttpResponseRedirect(reverse('multistepformexample'))
        except:
            messages.error(request,"Error in Saving Data")
            return HttpResponseRedirect(reverse('multistepformexample'))


