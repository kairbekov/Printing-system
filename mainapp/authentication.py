from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.utils.datastructures import MultiValueDictKeyError
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login_view(request):
    username = request.GET['username']
    password = request.GET['password']
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            request.user = user
            login(request, user)
            return HttpResponseRedirect('/mainapp/home')
            #return HttpResponse("Your account is ok.")
        else:
            return HttpResponse("Your account is disabled.")
    else:
         print "Invalid login details: {0}, {1}".format(username, password)
         return HttpResponse("Invalid login details supplied.")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/mainapp/log-in')