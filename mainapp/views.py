from django.http import Http404
from django.shortcuts import render
from rest_framework import routers, serializers, viewsets, generics
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from mainapp.models import Person


class PersonSerializer(serializers.HyperlinkedModelSerializer):
    # Serialize Persons
    class Meta:
        model = Person
        fields = ('id', 'first_name', 'last_name', 'email', 'balance', 'printed')

class PersonList(generics.ListCreateAPIView):
    # Get List of Persons
    queryset = Person.objects.all()
    serializer_class = PersonSerializer

class PersonDetail(generics.RetrieveUpdateDestroyAPIView):
    # Get Persons by id
    queryset = Person.objects.all()
    serializer_class = PersonSerializer