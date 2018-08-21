from django.conf.urls import patterns, url

from rest_framework.routers import DefaultRouter

from roadmap.views import APIViewSet

router = DefaultRouter()
router.register(r'api/projects', APIViewSet)

urlpatterns = patterns(
    'roadmap.views',
    url(r'^$', 'dashboard', name='dashboard'),
)

urlpatterns += router.urls
