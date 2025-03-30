from django.urls import path, include
from rest_framework import routers
from cinema.views import (
    GenreViewSet,
    ActorViewSet,
    CinemaHallViewSet,
    MovieViewSet,
    MovieSessionViewSet, OrderViewSet,
)

router = routers.DefaultRouter()
@@ -15,7 +15,8 @@
router.register("cinema_halls", CinemaHallViewSet)
router.register("movies", MovieViewSet)
router.register("movie_sessions", MovieSessionViewSet)
router.register("orders", OrderViewSet)

urlpatterns = router.urls

app_name = "cinema"
