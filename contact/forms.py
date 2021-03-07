from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(required=False, label="Nombre")
    email = forms.EmailField(required=True, label="Email")
    subject = forms.CharField(label="Asunto")
    content = forms.CharField(required=True, widget=forms.Textarea, label="Mensaje")
