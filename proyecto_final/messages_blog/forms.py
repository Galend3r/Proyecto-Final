from django import forms

class MessageForms(forms.Form):
    from_message = forms.CharField(max_length=50)
    to = forms.CharField(max_length=50)
    message = forms.CharField(max_length=400)