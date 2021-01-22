from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from .views import (
    PostListView,
    PostDetailView,
    PostCreateView,
    PostUpdateView,
    PostDeleteView
)
from . import views
urlpatterns = [
    path('', PostListView.as_view(), name='del-home'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('about/', views.about, name='del-about'),
    path('search_results/', views.search, name='searchBar'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)