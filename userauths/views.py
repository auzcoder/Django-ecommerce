from django.shortcuts import render

def register_views(request):
    return render(request, 'userauths/sign-up.html')