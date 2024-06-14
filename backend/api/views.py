from products.models import Product
from products.serializers import ProductSerializer

from rest_framework.response import Response
from rest_framework.decorators import api_view


# Create your views here.
@api_view(['POST'])
def api_home(request, *args, **kwargs):
    # data = request.data

    serializer = ProductSerializer(data = request.data)

    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        return Response(serializer.data)

    return Response({'invalid': 'not good data'}, status=400)

