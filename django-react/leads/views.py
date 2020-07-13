from django.shortcuts import render
from rest_framework import generics
from .serializers import LeadSerializer
from .models import Lead

class LeadListCreate(generics.ListCreateAPIView):
    queryset = Lead.objects.all()
    serializer_class = LeadSerializer

    

