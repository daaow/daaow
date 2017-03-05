from django.shortcuts import render

def index(request):
    context = {
        'text': 'hello world'
    }
    return render(request, 'score/index.html', context)
