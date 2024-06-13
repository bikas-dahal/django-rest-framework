from django.forms.models import model_to_dict

from products.models import Product
from products.serializers import ProductSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['GET', 'POST'])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by('?').first()
    data = {}
    if instance:
        # data = model_to_dict(model_data, fields=['id', 'title'])
        data = ProductSerializer(instance).data
    return Response(data)

 
# def api_home(request, *args, **kwargs):
#     model_data = Product.objects.all().order_by('?').first()
#     data = {}
#     if model_data:
#         data = model_to_dict(model_data, fields=['id', 'title'])
#     return JsonResponse(data)