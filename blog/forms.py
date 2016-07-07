from django import forms
from .models import Post

class PostForm(forms.ModelForm):
	kk = 5
class Meta:
      model = Post
      fields = ('title', 'text',)
	  