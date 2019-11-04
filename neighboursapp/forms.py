from django import forms
from .models import Profile,Post


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['user','profile']
        
# class CommentsForm(forms.ModelForm):
#     class Meta:
#         model = Comments
#         exclude = ['project','user']
       

# class VoteForm(forms.ModelForm):
#     class Meta:
#         model = Projects
#         exclude = ['proTitle','proImage','proDesc','proLink','profile','user','posted_date','vote_submissions']

