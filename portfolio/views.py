from django.shortcuts import render
from django.shortcuts import get_object_or_404

from portfolio.models import *

# Create your views here.

def index(request):
	template = 'pages/index.html'
	cts = ContentType.objects.filter(show = True)
	var = {
		'cts':cts,
	}
	return render(request, template, var)
	
def ctype(request, ctype_id):
	template = 'pages/ctype.html'
	ct = get_object_or_404(ContentType, pk=ctype_id)
	var = {
		'ct':ct,
	}
	return render(request, template, var)
