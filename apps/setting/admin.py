from django.contrib import admin

from apps.setting.models import Logo, Title,SEO
# Register your models here.
from solo.admin import SingletonModelAdmin

admin.site.register(Logo, SingletonModelAdmin)
admin.site.register(Title, SingletonModelAdmin)
admin.site.register(SEO, SingletonModelAdmin)