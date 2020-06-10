from django import forms


class TestForm(forms.Form):
    name = forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Votre Nom'}))
    email = forms.EmailField(label='', max_length=50, widget=forms.TextInput(attrs={'placeholder': 'Votre Mail'}))
    subject = forms.CharField(label='', max_length=255, widget=forms.TextInput(attrs={'placeholder': 'Objet Du Contact'}))
    message = forms.CharField(label='', widget=forms.Textarea(attrs={'placeholder': 'Votre Message'}))
