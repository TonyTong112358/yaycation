from django.views import View
from django.http import HttpResponse

# Create your views here.

class Account(View):
    def post(self,request):
        return HttpResponse("test")