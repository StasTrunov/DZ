from django.urls import path, include
from rest_framework import routers
from second.views import UserView

router = routers.DefaultRouter()
router.register(r'users', UserView)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]