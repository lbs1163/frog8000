from django.shortcuts import render, HttpResponse, redirect
from django.template import loader
from django.utils import timezone
from message.models import Message

# Create your views here.

def index(request):
	template = loader.get_template('message/index.html')
	context = {
		'message_list': Message.objects.all()
		
	}
	return HttpResponse(template.render(context, request))

def message(request):
	if request.method == 'GET':
		return redirect(index)
	elif request.method == 'POST':
		m = Message(message_text=request.POST.get("content"), writer=request.POST.get("writer"), pub_date=timezone.now())
		m.save()
		return redirect(index)