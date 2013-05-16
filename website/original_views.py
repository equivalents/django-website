# Create your views here.
#from website.forms import *
from website.models import *
from django.template import RequestContext
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.template import Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

def main_page(request):
  return render_to_response(
    'main_page.html', RequestContext(request)
  )
  
def logout_page(request):
  logout(request)
  return HttpResponseRedirect('/')
  
def user_page(request, username):
  try:
    user = User.objects.get(username=username)
  except:
    raise Http404('Requested user not found.')
  template = get_template('user_page.html')
  variables = RequestContext(request, {
    'username': username
  })
  output = template.render(variables)
  return HttpResponse(output)
 
@login_required
def control_page(request):
  if request.method == 'POST':   
    pin1 = Pin.objects.get(pinID=1)
    pin2 = Pin.objects.get(pinID=2)
	
    if 'pin1Status' in request.POST:
      if pin1.pinStatus == 'hi':
        pin1.pinStatus = 'low'
      else:
        pin1.pinStatus = 'hi'
      pin1.save()
	 
    if 'pin2Status' in request.POST:
      if pin2.pinStatus == 'hi':
        pin2.pinStatus = 'low'
      else:
        pin2.pinStatus = 'hi'
      pin2.save()
	  
    pin_list = Pin.objects.all()
    variables = RequestContext(request, {'pin_list': pin_list})
    return render_to_response('control_page.html', variables)
  else:
    pin_list = Pin.objects.all()
    variables = RequestContext(request, {'pin_list': pin_list})
    return render_to_response('control_page.html', variables) 
  