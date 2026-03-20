from .models import Article  # Точка обязательна!
from django.shortcuts import render

def archive(request):
    return render(request, 'archive.html', {"posts": Article.objects.all()})
