from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register(r'motels', views.MotelsViewSet)
router.register(r'towns', views.TownViewSet)
router.register(r'rooms', views.RoomViewSet)
router.register(r'amenities', views.AmenitiesViewSet)
router.register(r'comments', views.CommentsViewSet)

urlpatterns = router.urls
