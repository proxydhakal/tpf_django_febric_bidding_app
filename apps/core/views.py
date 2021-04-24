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



