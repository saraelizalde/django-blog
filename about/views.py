from django.shortcuts import render
from .models import About

# Create your views here.

def about_view(request):
    """
    Display the latest About page content.
    """
    about = About.objects.order_by('-updated_at').first()

    return render(
        request, 
        "about/about.html", 
        {'about': about})