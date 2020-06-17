from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ContactForm

def contact(request):
    form = ContactForm

    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            subject = form.cleaned_data['subject']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            try:
                send_mail(subject, message, 'no-reply@reciclatusanimales.com', [email])
                return redirect('contact:success')
            except BadHeaderError:
                return HttpResponse('Invalid header')

    else:
        form = ContactForm()

    context = {'form': form}
    return render(request, 'contact/contact.html', context)

def success(request):
    return HttpResponse('Your email has been sent')
