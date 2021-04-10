from django.contrib import admin
from apps.core.models import About, Term
# Register your models here.
from solo.admin import SingletonModelAdmin

admin.site.register(About, SingletonModelAdmin)
admin.site.register(Term, SingletonModelAdmin)