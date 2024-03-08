from django.shortcuts import render
from .models import Cards

def post_list(request):
    posts = Cards.objects.all()
    return render(request, 'anki/post_list.html', {'posts': posts})
