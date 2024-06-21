from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import json
from .chatbot import predict_class, get_response, intents

# Create your views here.
def answer(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        insts = predict_class(data['content'])
        res = get_response(insts, intents)
        message = {"role":"assistant","content":res}
        return JsonResponse(message)
