from django.shortcuts import render

def post_list(request):
    return render(request, 'anki/post_list.html', {})