from django.shortcuts import render
from django.contrib import messages
from .models import About
from .forms import CollaborateForm

# View function to display the "About Me" page
def about_me(request):
    # Check if the form has been submitted (POST request)
    if request.method == "POST":
        # Create an instance of the CollaborateForm with the submitted data
        collaborate_form = CollaborateForm(data=request.POST)
        # Validate the form data
        if collaborate_form.is_valid():
            # Save the form data to the database
            collaborate_form.save()
            # Display a success message to the user
            messages.success(
                request,
                'Collaboration request received!'
            )
    else:
        # If the request is not a POST, render an empty form
        collaborate_form = CollaborateForm()

    # Fetch the most recently updated "About" entry from the database
    about = About.objects.all().order_by('-updated_on').first()

    # Render the "about.html" template with the fetched data and form
    return render(
        request,
        "about/about.html",  # Template to render
        {"about": about, "collaborate_form": collaborate_form},  # Context data for the template
    )
