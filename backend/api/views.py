from rest_framework import generics, status 
from rest_framework.response import Response

from.models import BlogPost

from.serializers import BlogPostSerializer

from rest_framework.views import APIView


class BlogPostListCreate(generics.ListCreateAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer 

    def delete(self, request, *args, **kwargs):
        BlogPost.objects.all().delete()
        return Response(
            status = status.HTTP_204_NO_CONTENT
        )



class BlogPostRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer 
    lookup_field = 'pk'

class BlogPostList(APIView):
    def get(self, request, format=None):
        # Get title 

        title = request.query_params.get('title', '')
        if title:
            blogposts = BlogPost.objects.filter(title__icontains=title)
        else:
            blogposts = BlogPost.objects.all()

        serializer = BlogPostSerializer(blogposts, many=True)
        return Response(serializer.data, status= status.HTTP_200_OK)


# from products.models import Product
# from products.serializers import ProductSerializer

# from rest_framework.response import Response
# from rest_framework.decorators import api_view


# # Create your views here.
# @api_view(['POST'])
# def api_home(request, *args, **kwargs):
#     # data = request.data

#     serializer = ProductSerializer(data = request.data)

#     if serializer.is_valid(raise_exception=True):
#         print(serializer.data)
#         return Response(serializer.data)

#     return Response({'invalid': 'not good data'}, status=400)

