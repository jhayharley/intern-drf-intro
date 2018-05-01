from django.conf.urls import url, include
from rest_framework import routers
from blog import views
from blog.views import AnimeViewSet, BreedViewSet, WebsiteViewSet

router = routers.DefaultRouter()
router.register(r'animes', AnimeViewSet, base_name='animes')
router.register(r'breeds', views.BreedViewSet)
router.register(r'websites', views.WebsiteViewSet)



urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
 ]