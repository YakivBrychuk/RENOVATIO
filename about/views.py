from django.shortcuts import render
from django.contrib import messages
from .models import About
# from .forms import CollaborateForm
# Create your views here.


def about_view(request):
    if request.method == "POST" and 'collaborate_form' in globals():
        collaborate_form = CollaborateForm(data=request.POST)
        if collaborate_form.is_valid():
            collaborate_form.save()
            messages.success(
                request,
                'Collaboration request received! I endeavor to respond within 2 working days.'
            )
    else:
        collaborate_form = CollaborateForm() if 'CollaborateForm' in globals() else None

    about = About.objects.all().order_by('-updated_on').first()
    return render(
        request,
        "about/about.html",
        {"about": about, "collaborate_form": collaborate_form},
    )
