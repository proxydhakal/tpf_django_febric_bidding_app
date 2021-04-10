from django.db import models
from solo.models import SingletonModel
# Create your models here.

class Logo(SingletonModel):
    logo= models.ImageField(upload_to='logo',null=False)
    class Meta:
        verbose_name = "Company Logo"


class Title(SingletonModel):
    name= models.CharField(max_length=255, null=False)

    class Meta:
        verbose_name = "Company Title"

class SEO(SingletonModel):
    meta_description= models.TextField(null=False)
    meta_keywords= models.TextField(null=False)
    google_analytics= models.TextField(null=False)

    class Meta:
        verbose_name = "SEO"