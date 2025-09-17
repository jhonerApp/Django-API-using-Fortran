from rest_framework import serializers
from .models import FortranResults

class FortranResultsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FortranResults
        exclude = ['id']
