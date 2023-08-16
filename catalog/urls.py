from django.urls import path

from catalog.views import ContactView, IndexListView, ProductDetailView, BlogListView, BlogCreateView, BlogDetailView, \
    BlogUpdateView, BlogDeleteView, ProductCreateView, ProductUpdateView, ProductDeleteView

urlpatterns = [
    path('', IndexListView.as_view(), name='index'),
    path('contacts/', ContactView.as_view(), name='contacts'),
    path('<int:pk>/product/', ProductDetailView.as_view(), name='product'),
    path('blog/', BlogListView.as_view(), name='blog'),
    path('blog/create/', BlogCreateView.as_view(), name='create_blog'),
    path('blog/view/<int:pk>/', BlogDetailView.as_view(), name='read_blog'),
    path('blog/edit/<int:pk>/', BlogUpdateView.as_view(), name='update_blog'),
    path('blog/delete/<int:pk>/', BlogDeleteView.as_view(), name='delete_blog'),
    path('product/create/', ProductCreateView.as_view(), name='product_create'),
    path('product/<int:pk>/update/', ProductUpdateView.as_view(), name='product_update'),
    path('product/<int:pk>/delete/', ProductDeleteView.as_view(), name='product_delete'),
]