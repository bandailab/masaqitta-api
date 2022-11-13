from . import views
from rest_framework import routers
from api.views import UserViewSet, TweetViewSet

router = routers.DefaultRouter()
router.register('user', UserViewSet)
router.register('tweet', TweetViewSet)
