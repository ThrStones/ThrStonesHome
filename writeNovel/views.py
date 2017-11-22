from django.shortcuts import render

# Create your views here.


def cards(request):
    """主页"""
    return render(request, 'writeNovel/cards.html')
