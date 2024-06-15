from django.urls import path 

from .import views 

urlpatterns = [
    path('blog/', views.BlogPostListCreate.as_view(), name='api_home'),
    path('blog/<int:pk>/', views.BlogPostRetrieveUpdateDestroy.as_view(), name='api_detail'),
    
]
