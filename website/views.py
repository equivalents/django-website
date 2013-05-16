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

  sliderB = Slider.objects.get(sliderID=1)
  sliderR = Slider.objects.get(sliderID=2)
  sliderG = Slider.objects.get(sliderID=3)
  sliderP = Slider.objects.get(sliderID=4)
  preprogram1 = Preprogram.objects.get(preprogramID=1)
  preprogram2 = Preprogram.objects.get(preprogramID=2)
  preprogram3 = Preprogram.objects.get(preprogramID=3)
  pin1 = Pin.objects.get(pinID=1)
  variables = RequestContext(request, {'pin1': pin1, 'preprogram1': preprogram1, 'preprogram2': preprogram2, 'preprogram3': preprogram3, 'sliderB':sliderB, 'sliderR':sliderR, 'sliderG':sliderG, 'sliderP':sliderP})
  return render_to_response('control_page.html', variables) 
	
def gpio_control_page(request):
  
  pin1 = Pin.objects.get(pinID=1)
  if pin1.pinStatus == 'hi':
    pin1.pinStatus = 'low'
  else:
    pin1.pinStatus = 'hi'
  pin1.save()
  variables = RequestContext(request, {'pin1': pin1})
  return render_to_response('gpio_control_page.html', variables)
  
def slider_page(request):
  
  if request.method == "GET":
    get = request.GET.copy()
    if get.has_key('blue_power'):
      blue_power = get['blue_power']
      sliderB = Slider.objects.get(sliderID=1)
      sliderB.sliderValue = blue_power
      sliderB.sliderUpdate = "true"
      sliderB.save()
      variables = RequestContext(request, {'sliderB': sliderB})
    if get.has_key('red_power'):
      red_power = get['red_power']
      sliderR = Slider.objects.get(sliderID=2)
      sliderR.sliderValue = red_power
      sliderR.sliderUpdate = "true"
      sliderR.save()
      variables = RequestContext(request, {'sliderR': sliderR})
    if get.has_key('green_power'):
      green_power = get['green_power']
      sliderG = Slider.objects.get(sliderID=3)
      sliderG.sliderValue = green_power
      sliderG.sliderUpdate = "true"
      sliderG.save()
      variables = RequestContext(request, {'sliderG': sliderG})
    if get.has_key('phase_speed'):
      phase_speed = get['phase_speed']
      sliderP = Slider.objects.get(sliderID=4)
      sliderP.sliderValue = phase_speed
      sliderP.sliderUpdate = "true"
      sliderP.save()
      variables = RequestContext(request, {'sliderP': sliderP})
    if get.has_key('police'):
      police = get['police']
      preprogram1 = Preprogram.objects.get(preprogramID=1)
      preprogram1.preprogramStatus = police
      if preprogram1.preprogramStatus == 'off':
        preprogram1.preprogramValue = 0
        preprogram1.preprogramUpdate = "true"
      else:
        preprogram1.preprogramStatus == 'on'
        preprogram1.preprogramValue = 1  
      preprogram1.preprogramUpdate = "true"
      preprogram1.save()
      variables = RequestContext(request, {'preprogram1': preprogram1})
    if get.has_key('danger'):
      danger = get['danger']
      preprogram2 = Preprogram.objects.get(preprogramID=2)
      preprogram2.preprogramStatus = danger
      if preprogram2.preprogramStatus == 'off':
        preprogram2.preprogramValue = 0
        preprogram2.preprogramUpdate = "true"
      else:
        preprogram2.preprogramStatus == 'on'
        preprogram2.preprogramValue = 1 
      preprogram2.preprogramUpdate = "true"
      preprogram2.save()
      variables = RequestContext(request, {'preprogram2': preprogram2})
    if get.has_key('kill'):
      kill = get['kill']
      preprogram1 = Preprogram.objects.get(preprogramID=1)
      preprogram2 = Preprogram.objects.get(preprogramID=2)
      preprogram3 = Preprogram.objects.get(preprogramID=3)
      if preprogram3.preprogramStatus == 'kill':
        preprogram3.preprogramValue = 1
        preprogram3.preprogramUpdate = "true"
        preprogram3.preprogramStatus = 'kill'
      else:
        preprogram3.preprogramValue = 0
        preprogram3.preprogramStatus = 'kill'  
      preprogram3.preprogramUpdate = "true"
      preprogram1.preprogramStatus = 'off'
      preprogram2.preprogramStatus = 'off'
      preprogram1.save()
      preprogram2.save()
      preprogram3.save()
      variables = RequestContext(request, {'preprogram3': preprogram3})
  return render_to_response('slider_page.html', variables)
  