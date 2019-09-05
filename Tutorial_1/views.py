from django.http import HttpResponse

def megaindex(reques):
    return HttpResponse(" yeah home")

def visithome(request):
    return  HttpResponse("vsit home")