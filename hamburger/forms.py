from django import forms

from .models import Hamburger

class DiaryCreateForm(forms.ModelForm):
    class Meta:
        model = Hamburger
        fields = ('title','content','photo1')

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'