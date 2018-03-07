from django import forms

from main.models import Speakers

class PostForm(forms.ModelForm):

    class Meta:
        model = Speakers
        fields = ('name', 'descr', 'topic', 'sect')