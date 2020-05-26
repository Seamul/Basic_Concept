from django import forms
from .models import Comment
class  EmailPistForms(forms.Form):
	name=forms.CharField(max_length=30)
	email=forms.EmailField()
	to=forms.EmailField()
	commants=forms.CharField(required=False,widget=forms.Textarea)
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email', 'body')