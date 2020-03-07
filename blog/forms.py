from django import forms

from .models import Post
from .models import Article

class PostForm(forms.ModelForm):
	
    class Meta:
        model = Post
        fields = ('title', 'text','cover')
        
class ArticleForm(forms.ModelForm):
	
	class Meta:
		model = Article
		fields = ('title','img_article')