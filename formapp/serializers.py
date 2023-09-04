from rest_framework import serializers
from .models import FormSubmission

class FormSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormSubmission
        fields = '__all__'


def validate_email(self, value):
        """
        Ensure that the email address is in a valid format.
        """
        from django.core.exceptions import ValidationError
        from django.utils.translation import gettext_lazy as _
        
        if not value.endswith('angethherjok@gmail.com'):  # Replace with your desired email domain
            raise ValidationError(_('Email domain must be example.com'))
        return value
