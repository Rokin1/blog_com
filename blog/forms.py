from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget
from django import forms
from . models import Post, Comment
# Apply summernote to specific fields.


# class SomeForm(forms.Form):
# instead of forms.Textarea
# foo = forms.CharField(widget=SummernoteWidget())

# If you don't like <iframe>, then use inplace widget
# Or if you're using django-crispy-forms, please use this.


# class AnotherForm(forms.Form):
#     bar = forms.CharField(widget=SummernoteInplaceWidget())


# class FormFromSomeModel(forms.ModelForm):
#     class Meta:
#         model = Post
#         widgets = {
#             'foo': SummernoteWidget(),
#             'bar': SummernoteInplaceWidget(),
#         }


class PostForm(forms.ModelForm):
    content = forms.CharField(widget=SummernoteWidget(
        attrs={'width': '50%', 'height': '400px'}), label="Description", required=False)

    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': SummernoteInplaceWidget(),
        }


# class CommentForm(forms.ModelForm):
#     content = forms.CharField(widget=SummernoteInplaceWidget(

#         attrs={'required': False, 'cols': 30, 'rows': 10}
#     )
#     )

#     class Meta:
#         model = Post
#         fields = ('title', 'content')
#         widgets = {
#             'content': SummernoteInplaceWidget(),
#         }
class CommentForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Type your comment',
        'id': 'usercomment',
        'rows': '4',
    }))
    # title = forms.CharField(max_length=120)
    # content = forms.CharField(widget=SummernoteWidget(
    #     attrs={'width': '50%', 'height': '400px'}), label="Description", required=False)

    class Meta:
        model = Comment
        fields = ('content',)
