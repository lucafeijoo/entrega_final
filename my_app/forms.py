from django import forms
from my_app.models import Blog

# class mascotas(forms.Form):

#     nombre = forms.CharField(max_length= 48)
#     especie = forms.CharField(max_length= 48)
#     edad = forms.IntegerField()
    
class BlogForm(forms.ModelForm):
    class Meta:
        model= Blog
        fields = ['titulo','subtitulo','cuerpo']
