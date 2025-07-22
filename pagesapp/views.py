from django.shortcuts import render

# Create your views here.

# pagesapp/views.py
def notice_view(request):
    return render(request, 'pagesapp/notice.html')

def partnership_view(request):
    return render(request, 'pagesapp/partnership.html')

def about_view(request):
    return render(request, 'pagesapp/about.html')