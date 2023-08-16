from django.urls import path

from catalog.views import ContactView, IndexListView, ProductDetailView, BlogListView, BlogCreateView, BlogDetailView

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('<int:pk>/product/', ProductDetailView.as_view(), name='product'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/create/', BlogCreateView.as_view(), name='create_blog'),
    path('<int:pk>/blog/', BlogDetailView.as_view(), name='read_blog')
]