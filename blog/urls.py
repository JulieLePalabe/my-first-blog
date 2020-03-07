from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
	path('post/<pk>/remove/', views.post_remove, name='post_remove'),

	path('article/', views.article_list, name='article_list'),
	path('article/<int:pk>/', views.article_detail,name='article_detail'),
	path('article/new/', views.article_new, name='article_new'),
	path('article/<int:pk>/edit/', views.article_edit,name='article_edit'),
	path('article/<pk>/remove/', views.article_remove,name='article_remove'),
] 
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)