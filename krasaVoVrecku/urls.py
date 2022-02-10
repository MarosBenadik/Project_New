
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path("accounts/", include("django.contrib.auth.urls")),
    path('admin/', admin.site.urls),
    path('users/', include('users.urls')),
    path('', include('landing.urls')),
    path('krasavovrecku/feed/', include('mainfeed.urls')),
    path('directmessages/', include('directmessages.urls')),
    path('questions/', include('question.urls')),
    path('booking/', include('booking.urls')),
    path('users/api/', include('users.api.urls')),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)