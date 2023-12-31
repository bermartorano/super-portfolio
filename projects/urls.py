from django.urls import path, include
from rest_framework import routers
from .views import (
    ProfileViewSet,
    ProjectViewSet, CertificateViewSet, CertifyingInstitutionViewSet)
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)

router = routers.DefaultRouter()
router.register(r"profiles", ProfileViewSet)
router.register(r"projects", ProjectViewSet)
router.register(r"certificates", CertificateViewSet)
router.register(r"certifying-institutions", CertifyingInstitutionViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path(
        "token/", TokenObtainPairView.as_view(), name="token-obtain-pair"
    ),
    path(
        "token/refresh/", TokenRefreshView.as_view(), name="token-refresh"
    ),
    path("token/verify/", TokenVerifyView.as_view(), name="token-verify"),
]
