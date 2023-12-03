from django.urls import include, path
from rest_framework.routers import DefaultRouter

from defects import views as dvs

router = DefaultRouter()
router.register(r"defects", dvs.DefectSet)


urlpatterns = [
    path("", include(router.urls)),

    path("defects/<slug:slug>/comment/", dvs.CommentCreateApiView.as_view(),  name="comment-create")

]



