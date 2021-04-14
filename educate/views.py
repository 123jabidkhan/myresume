from django.shortcuts import render

# Create your views here.

def skills_page(request):
    return render(request, 'educate/skills.html')