from django.urls import path
from .views import FormSubmissionCreateView

urlpatterns = [
    path('submit/', FormSubmissionCreateView.as_view(), name='submit-form'),
]
