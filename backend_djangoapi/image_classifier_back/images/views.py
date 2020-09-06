from django.shortcuts import render
from .serializers import ImageSerializer
from .models import Image


# Create your views here.

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Image.objects.all().order_by('-uploaded')
    serializer_class = ImageSerializer