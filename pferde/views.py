from .serializers import PferdSerializer
from rest_framework import generics
from .models import Pferd

# Create your views here.


class PferdList(generics.ListCreateAPIView):
    queryset = Pferd.objects.all()
    serializer_class = PferdSerializer


class PferdDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pferd.objects.all()
    serializer_class = PferdSerializer

# Create your views here.
