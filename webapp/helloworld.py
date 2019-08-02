from django.http import HttpResponse
from django.shortcuts import render

def hello(request):
     return render(request,'index.html')

def page_not_found(request):
    from django.shortcuts import render_to_response
    response=render_to_response('404.html',{})
    response.status_code=404
    return response

def server_error(request):
    from django.shortcuts import render_to_response
    response=render_to_response('500.html',{})
    response.status_code=500
    return response
