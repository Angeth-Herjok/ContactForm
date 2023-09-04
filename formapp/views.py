from django.shortcuts import render
from rest_framework import generics
from .models import FormSubmission
from .serializers import FormSubmissionSerializer
from django.core.mail import send_mail

# Create your views here.

class FormSubmissionCreateView(generics.CreateAPIView):
    queryset = FormSubmission.objects.all()
    serializer_class = FormSubmissionSerializer



def perform_create(self, serializer):
        instance = serializer.save()

        # Send confirmation email to the user
        send_mail(
            'Form Submission Confirmation',
            'Thank you for submitting the form!',
            'your_email@example.com',  # Sender's email
            [instance.email],  # Recipient's email (from the submitted form)
            fail_silently=False,
        )
