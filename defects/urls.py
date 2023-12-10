from django.urls import include, path
from rest_framework.routers import DefaultRouter

from defects import views as dvs

router = DefaultRouter()
router.register(r"defects", dvs.DefectSet)


urlpatterns = [
    path("", include(router.urls)),

    path("defects/<slug:slug>/comment/", dvs.CommentCreateApiView.as_view(),  name="comment-create"),

    path("defects/<slug:slug>/comments/", dvs.CommentListApiView.as_view(),  name="comments-list"),

    path("comments/<uuid:uuid>/", dvs.CommentCRUDApiView().as_view(), name="comment-detail"),

    path("comments/<uuid:uuid>/vote/", dvs.CommentVoteAPIView().as_view(), name="comment-votes"),

    path('csrf_token_provider_endpoint/', dvs.CSRFproviderView.as_view(), name='csrf_token'),

]