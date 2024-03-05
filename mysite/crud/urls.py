from django.urls import path
from .views import *
# from rest_framework import routers 
# router = routers.DefaultRouter() 
# router.register(r'geeks', BookListViewSet) 

urlpatterns = [
    path('', index.as_view(),name='index'),
    path('index/<int:pk>/', index.as_view(),name='index'),
    path('register/', Register.as_view(),name='register'),
    path('delete_user/',Delete_user.as_view(),name='delete_user'),
    path('edit_user/<int:pk>',EditUser.as_view(),name='edit_user'),
    # path('books/', BookList.as_view(), name='book-list'),
    # path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
]

# urlpatterns += router.urls
