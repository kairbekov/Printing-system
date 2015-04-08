from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response
from django.template import RequestContext
from rest_framework import routers, serializers, viewsets, generics
# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from mainapp.forms import DocumentForm
from mainapp.models import Data, Document


def home_view(request):
    if request.user.is_authenticated():
        return render(request, '../static/../templates/main_page.html')
    else:
        return HttpResponseRedirect('/mainapp/log-in')


def login_page_view(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/mainapp/home')
    return render(request, '../static/../templates/login_page.html')

class DataSerializer(serializers.HyperlinkedModelSerializer):
    # Serialize Documents
    user = serializers.StringRelatedField(many=True)
    class Meta:
        model = Data
        fields = ('id', 'user', 'data_name', 'data_type', 'data_size')

class DataList(generics.ListCreateAPIView):
    # Get List of documents
    queryset = Data.objects.all()
    serializer_class = DataSerializer

class DataDetail(generics.RetrieveUpdateDestroyAPIView):
    # Get documents by id
    queryset = Data.objects.all()
    serializer_class = DataSerializer


class UserSerializer(serializers.HyperlinkedModelSerializer):
    # Serialize users
    class Meta:
        model = User
        fields = ('id', 'username', 'first_name', 'last_name', 'email', 'password', 'is_superuser', 'is_active')

class UserList(generics.ListCreateAPIView):
    # Get list of users
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    # Get user by id
    queryset = User.objects.all()
    serializer_class = UserSerializer

def list(request):
    # Handle file upload
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        if form.is_valid():
            newdoc = Document(docfile = request.FILES['docfile'])
            newdoc.save()

            # Redirect to the document list after POST
            return HttpResponseRedirect(reverse('myapp.views.list'))
    else:
        form = DocumentForm() # A empty, unbound form

    # Load documents for the list page
    documents = Document.objects.all()

    # Render list page with the documents and the form
    return render_to_response(
        'myapp/list.html',
        {'documents': documents, 'form': form},
        context_instance=RequestContext(request)
    )