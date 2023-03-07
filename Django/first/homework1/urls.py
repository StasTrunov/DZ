from django.urls import path, include
from rest_framework import routers
from homework1.views import FPlayerView

router = routers.DefaultRouter()
router.register(r'fplayers', FPlayerView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]