from django.db import models
from solo.models import SingletonModel
from django.utils.text import slugify
from django.urls import reverse
from django.contrib.auth.models import User
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

class Parent(models.Model):
        name = models.CharField(max_length=255, null=False, unique=True)
        slug = models.SlugField(null=True, max_length=255, blank=True)
        meta_desctrption = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def save(self, *args, **kwargs):
            self.slug = slugify(self.name)
            super(Parent, self).save(*args, **kwargs)

        def __str__(self):
                return self.name

class Child(models.Model):
        parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
        name = models.CharField(max_length=255, null=False, unique=True)
        slug = models.SlugField(null=True, max_length=255, blank=True)
        
        meta_description = models.TextField()
        days = models.IntegerField(null=False)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def save(self, *args, **kwargs):
            self.slug = slugify(self.name)
            super(Child, self).save(*args, **kwargs)

        def __str__(self):
                return self.name



class ListFebric(models.Model):
        CHOICES = [('1', 'Contact me Directly'), ('2', 'Conduct Sale at Another Location')]
        parent = models.ForeignKey(Parent, on_delete=models.CASCADE)
        child = models.ForeignKey(Child, on_delete=models.CASCADE)
        title = models.CharField(max_length=255, null=False, unique=True)
        price = models.IntegerField(null=False)
        sell_at = models.CharField(max_length=2,choices=CHOICES,default=1)
        link_ebay = models.URLField(max_length=255 ,null=False, blank=False)
        facebook_profile = models.URLField(max_length=255, null=False, blank= False)
        instagram_profile = models.URLField(max_length=255, null=False, blank=False)
        user = models.ForeignKey(User,on_delete=models.CASCADE, null=False, blank=False)
        email = models.EmailField(null=False, blank=False)
        phone = models.IntegerField(null=False)
        slug = models.SlugField(max_length=255, blank=True, null=True)
        short_description = models.TextField()
        long_description = models.TextField()
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def save(self, *args, **kwargs):
            self.slug = slugify(self.title)
            super(ListFebric, self).save(*args, **kwargs)

        def __str__(self):
                return self.title

class MultiStepFormModel(models.Model):
    id=models.AutoField(primary_key=True)
    fname=models.CharField(max_length=255)
    lname=models.CharField(max_length=255)
    phone=models.CharField(max_length=255)
    twitter=models.CharField(max_length=255)
    facebook=models.CharField(max_length=255)
    gplus=models.CharField(max_length=255)
    email=models.CharField(max_length=255)
    password=models.CharField(max_length=255)
    objects=models.Manager()








        
