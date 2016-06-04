from rest_framework import serializers

from app.models import *

class ProviderSerializer(serializers.ModelSerializer):

    class Meta:
        model=Provider
        fields=('provider_id', 'name', 'email', 'phone_number', 'language', 'currency')
