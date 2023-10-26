from django.views import View
from django.http import HttpResponse, JsonResponse
import json
from utils.requestParser import validate_post_field
from exceptions.inputExceptions import *
import os 

# Create your views here.

class Account(View):
    # create a password 
    def post(self,request):
        data = request.body
        # needed data
        required = ["username","email","password","phone_number"]
        try:
            data = validate_post_field(data,required)
        except invalidJsonFormatException as e:

            return JsonResponse({"message": e.message},status = e.errorCode)
        return JsonResponse(data = data, status = 201)