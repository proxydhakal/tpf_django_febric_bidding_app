from django import  forms
from django.forms import fields
from apps.core.models import Parent, Child, ListFebric
from django.forms import  TextInput,PasswordInput,Textarea,Select,URLInput,EmailInput,RadioSelect
FAVORITE_COLORS_CHOICES = [
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
]
class ListFebricForm(forms.ModelForm):

    class Meta:
        model = ListFebric
        fields = ('parent', 'child','title','price','sell_at','link_ebay','facebook_profile','instagram_profile','phone', 'email', 'short_description','long_description')
        widgets ={
            'parent':Select(attrs={'class':'form-control'}),
            'child':Select(attrs={'class':'form-control'}),
            'title':TextInput(attrs={'class':'form-control'}),
            'price':TextInput(attrs={'class':'form-control'}),
            'sell_at':RadioSelect(attrs={'class':'position-relative form-check-input text-decoration-none','type':'radio'}),
            'link_ebay':URLInput(attrs={'class':'form-control'}),
            'facebook_profile':URLInput(attrs={'class':'form-control'}),
            'instagram_profile':URLInput(attrs={'class':'form-control'}),
            'phone':TextInput(attrs={'class':'form-control'}),
            'email':EmailInput(attrs={'class':'form-control'}),
            'short_description':Textarea(attrs={'class':'form-control','rows':'4'}),
            'long_description':Textarea(attrs={'class':'form-control'}),
        }
    def __init__(self, *args, **kwargs):
            super().__init__(*args, **kwargs)
            self.fields['child'].queryset = Child.objects.none()

            if 'parent' in self.data:
                try:
                    parent_id = int(self.data.get('parent'))
                    self.fields['child'].queryset = Child.objects.filter(parent_id=parent_id).order_by('name')
                except (ValueError, TypeError):
                    pass 
            elif self.instance.pk:
                self.fields['child'].queryset = self.instance.parent.child_set.order_by('name')



