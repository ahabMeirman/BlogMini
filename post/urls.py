from django.urls import path
from post.views import *

from django.contrib.auth.decorators import login_required#декоратор огроничения доступа, здксь не используется @, а просто обьект на который есть огроничение захватывается в кавычки

urlpatterns = [
	path('', PostView.as_view(), name = 'post_view_url' ),
	path('create/', PostCreate.as_view(), name = 'post_create_url' ),
	path('<str:title>/', PostViewDetail.as_view(), name = 'view_post_detail_url'),	
]