from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home_page(request):
	context = {}
	items = []
	if request.method == 'POST':
		item.append(request.POST.get('item_text'))
		# context['new_item_text'] = request.POST.get('item_text')
	context['items'] = items

	return render(request, 'home.html', context)