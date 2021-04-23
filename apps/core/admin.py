from django.contrib import admin
from apps.core.models import About, Term, Parent, Child ,ListFebric,MultiStepFormModel
# Register your models here.
from solo.admin import SingletonModelAdmin

admin.site.register(About, SingletonModelAdmin)
admin.site.register(Term, SingletonModelAdmin)
admin.site.register(Parent)
admin.site.register(Child)
admin.site.register(ListFebric)
admin.site.register(MultiStepFormModel)