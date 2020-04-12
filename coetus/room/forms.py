from django import  forms
from .models import  file

class fileForm(forms.ModelForm):
    class Meta:
        model  = file
        fields = ("room" , "content")

        def save(self):
            file = super(fileForm, self).save()


