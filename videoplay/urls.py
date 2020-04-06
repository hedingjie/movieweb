from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.conf.urls import include, url
from . import views
from rest_framework.routers import DefaultRouter

# Routers（路由）提供了一种简单的方法来自动生成URL配置
router = DefaultRouter()
router.register(r'movie', views.SnippetViewSet)


urlpatterns=[
    path('',views.login,name='login'),
    path('regist/',views.regist,name='regist'),
    path('movie/',views.index,name='movie'),
    path('movie/video/<int:id>/',views.play,name='play'),
    # url(r'^movie/video_(?P<id>\d{1,2}).html$', views.play),
    url(r'^', include(router.urls)),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)