from django.shortcuts import render
from main.models import Speakers
from django.views.generic import ListView, DetailView
from main.forms import PostForm
import datetime



def index(request):
	speak = Speakers.objects.order_by('time')
	return render(request, 'main/homepage.html', {'speak': speak})
	
def add(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			spk = form.save(commit=False)
			now = datetime.datetime.now()
			spk.time = now
			spk.save()
			form = PostForm()
			return render(request, 'main/add.html', {'form': form, 'ans': 'Добавлено!'})
		else:
			return render(request, 'main/add.html', {'form': form, 'ans': 'Форма не валидна'})
	else:
		form = PostForm()
		return render(request, 'main/add.html', {'form': form})

	
