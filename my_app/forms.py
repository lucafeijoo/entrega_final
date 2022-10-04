from django import forms
from my_app.models import Blog

class BlogForm(forms.ModelForm):
    class Meta:
        model= Blog
        fields = ['titulo','subtitulo','cuerpo']
