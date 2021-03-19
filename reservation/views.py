from django.shortcuts import render
from .models import Reservation
from .forms import ReserveTableForm
from django.http import JsonResponse
from contact.utils import api_response
from datetime import datetime
import time
import json
from contact.constants import reservation_template_slug, email_sender_url, email_sender_api_key
import urllib3

import locale

locale.setlocale(locale.LC_TIME, 'es_ES')

def reserve_table(request):
    form = ReserveTableForm()
    context = {'form': form}

    return render(request, 'reservation/reservation.html', context)

def reserve(request):
    json_response = {'success': False}    
    data = json.loads(request.body.decode("utf-8"))

    if('name' not in data): 
        json_response['msg'] = 'El campo \'name\' no puede estar vacío' 
        return api_response(json_response)
    elif('email' not in data): 
        json_response['msg'] = 'El campo \'email\' no puede estar vacío' 
        return api_response(json_response)
    elif('phone' not in data): 
        json_response['msg'] = 'El campo \'phone\' no puede estar vacío' 
        return api_response(json_response)
    elif('number_of_persons' not in data): 
        json_response['msg'] = 'El campo \'number_of_persons\' no puede estar vacío' 
        return api_response(json_response)
    elif('date' not in data): 
        json_response['msg'] = 'El campo \'date\' no puede estar vacío' 
        return api_response(json_response)
    elif('time' not in data): 
        json_response['msg'] = 'El campo \'time\' no puede estar vacío' 
        return api_response(json_response)

    name = data['name']
    email = data['email']
    phone = data['phone']
    number_of_persons = data['number_of_persons']
    date = data['date']
    time = data['time']    
    formated_date = "{} de {}".format(datetime.strptime(date, "%Y-%m-%d").strftime("%A %d"), datetime.strptime(date, "%Y-%m-%d").strftime("%B"))

    reservation = Reservation.objects.create(
        name=name,
        email=email,
        phone=phone,
        number_of_persons=number_of_persons,
        date=date,
        time=time,
    )
    reservation.save()

    params = {
        'phone': phone,
        'number_of_persons': number_of_persons,
        'formated_date': formated_date,
        'date': date,
        'time': time
    }
    
    http = urllib3.PoolManager()
    attempt_num = 0
    while attempt_num < 1:       
        body = {'name': name, 'from': email, 'params': params, 'template_slug': reservation_template_slug, 'type': 'reservation'}
        headers = {'Content-Type': 'application/json', 'api-key': email_sender_api_key}
        response = http.request(
            'POST',
            email_sender_url,
            body=json.dumps(body),
            headers=headers
        )
        if response.status == 200:
            data = json.loads(response.data.decode('utf-8'))
            return JsonResponse(data)
        else:
            attempt_num += 1
            time.sleep(5) 
    
    json_response["msg"] = "Hubo un problema con la solicitud."

    return JsonResponse(json_response)

