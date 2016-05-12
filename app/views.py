from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'page/base.html')

def group(request):
    return render(request, 'group/view.html')
