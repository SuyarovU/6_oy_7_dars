from django import forms
from .models import Todo



class TodoModelForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = ["title", "description"]

   

# class TodoForm(forms.Form):
#     title = forms.CharField(max_length=10)
#     description = forms.CharField()


    # def clean_title(self):
    #     title = self.cleaned_data["title"] 
    #     if not title.startswith("a"):
    #         raise forms.ValidationError("Title a dan boshlanishi kerak edi!")
    #     return title




