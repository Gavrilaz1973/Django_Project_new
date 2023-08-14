from django.urls import path

from catalog.views import contacts, product, index

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('<int:pk>/product/', product, name='product')
]