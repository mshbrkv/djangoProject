import json

from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


# Create your views here.

@csrf_exempt
def ping(request):
    with open("core/data.json", "r") as f:
        data = f.read()
    if request.method == 'POST':
        body = request.body
        body_json: dict = json.loads(body)
        data_json: dict = json.loads(data)
        data_json.update(body_json)
        with open("core/data.json", "w") as f:
            json.dump(data_json, f)
        return HttpResponse("success")
    return HttpResponse(data)
