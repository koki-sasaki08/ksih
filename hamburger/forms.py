from django import forms

#Mac
from .models import Mac

class MacCreateForm(forms.ModelForm):
    class Meta:
        model = Mac
        fields = ('name','price','ditail','photo')

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'

#Mos
from .models import Mos

class MosCreateForm(forms.ModelForm):
    class Meta:
        model = Mos
        fields = ('name','price','ditail','photo')

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'


#BurgerKing
from .models import BurgerKing

class BurgerKingCreateForm(forms.ModelForm):
    class Meta:
        model = BurgerKing
        fields = ('name','price','ditail','photo')

        def __init__(self,*args,**kwargs):
            super().__init__(*args,**kwargs)
            for field in self.fields.values():
                field.widget.attrs['class'] = 'form-control'