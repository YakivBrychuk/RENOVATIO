from django.db import models
from cloudinary.models import CloudinaryField

# Models: About, CollaborateRequest


class About(models.Model):
    """
    Model to store 'About Me' information.
    - title: Title or heading for the about section.
    - profile_image: Profile image uploaded to Cloudinary.
    - updated_on: Timestamp of the last update.
    - content: Detailed text content about the user.
    """
    title = models.CharField(max_length=200)
    profile_image = CloudinaryField('image', default='placeholder')
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        # Return a string representation for admin and debugging
        return self.title


class CollaborateRequest(models.Model):
    """
    Model to store collaboration requests.
    - name: Name of the person making the request.
    - email: Contact email address.
    - message: Collaboration message or proposal.
    - read: Status to track if the message has been read.
    """
    name = models.CharField(max_length=200)
    email = models.EmailField()
    message = models.TextField()
    read = models.BooleanField(default=False)

    def __str__(self):
        # Return a string representation for admin and debugging
        return f"Collaboration request from {self.name}"
