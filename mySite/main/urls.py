from django.urls import path
from . import views
from django.views.generic import ListView, DetailView
from main.models import speakers

urlpatterns = [
    path('', 
	ListView.as_view(queryset=speakers.objects.all().order_by("time")[:20],
	template_name="main/homepage.html")),
]