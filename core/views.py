from django.shortcuts import render

def group(request):
    return render(request, 'group/view.html')
