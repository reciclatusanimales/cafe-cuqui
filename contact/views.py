from django.shortcuts import render, redirect
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from .forms import ContactForm
from .utils import api_response, 
import requests
import time
import json
from .constants import contact_template_slug, email_sender_url

def contact(request):
    form = ContactForm

    context = {'form': form}
    return render(request, 'contact/contact.html', context)

def send_email(request):
    json_response = {'success': False}

    data = json.loads(request.body.decode("utf-8"))

    if('subject' not in data): 
        json_response['msg'] = 'El campo \'subject\' no puede estar vacío' 
        return api_response(json_response)
    elif('email' not in data): 
        json_response['msg'] = 'El campo \'email\' no puede estar vacío' 
        return api_response(json_response)
    elif('content' not in data): 
        json_response['msg'] = 'El campo \'content\' no puede estar vacío' 
        return api_response(json_response)

    name = data['name']
    email = data['email']
    subject = data['subject']
    content = data['content']

    attempt_num = 0
    while attempt_num < 1:       
        body = {'name': name, 'from': email, 'subject': subject, 'content': content, 'template_slug': contact_template_slug}
        response = requests.post(email_sender_url, data = json.dumps(body))
        if response.status_code == 200:
            data = response.json()
            return JsonResponse(data)
        else:
            attempt_num += 1
            time.sleep(5) 

    return JsonResponse(json_response)