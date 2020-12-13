from django.shortcuts import render_to_response
# Create your views here.
from .models import me

def index(request):
	mes = me.objects.all()
	return render_to_response('cms/menu.html',locals())
