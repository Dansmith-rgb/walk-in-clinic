from rest_framework import viewsets
from rest_framework import filters
from .serializers import RegisterSerializer
from .models import Register, Signin
from django_filters.rest_framework import DjangoFilterBackend



class RegisterViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer
    #Register.objects.all().filter(name__name__in=['name','password'])
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['name', 'password', 'id']

class SigninViewSet(viewsets.ModelViewSet):
    queryset = Register.objects.all()
    serializer_class = RegisterSerializer