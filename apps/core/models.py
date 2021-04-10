from django.db import models
from solo.models import SingletonModel
# Create your models here.

class About(SingletonModel):
    
    title= models.CharField(max_length=100, null=False)
    description= models.TextField()
    def __str__(self):
            return self.title

    class Meta:
        verbose_name = "How It Works"


class Term(SingletonModel):
    
    title= models.CharField(max_length=100, null=False)
    description= models.TextField()
    def __str__(self):
            return self.title

    class Meta:
        verbose_name = "Terms of Service"
