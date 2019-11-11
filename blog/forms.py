from django import forms
from captcha.fields import CaptchaField
class UserForm(forms.Form):
    username = forms.CharField(label='用户名', max_length=128, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label='密  码', max_length=256, widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    captcha = CaptchaField(label='验证码')

class PostForm(forms.Form):
    title = forms.CharField(label='标题', max_length=128, widget=forms.TextInput)
    text = forms.CharField(label='内容', widget=forms.Textarea)