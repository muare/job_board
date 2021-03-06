from django.db.models import fields
from rest_framework import serializers
from rest_framework.utils import model_meta
from jobs.models import JobOffer

class JobOfferSerializer(serializers.ModelSerializer):

    class Meta:
        model = JobOffer
        fields = "__all__"