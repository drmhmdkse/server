from django.conf import settings
from django.urls import path, include
from django.contrib import admin
from django.conf.urls.static import static
from sozluk.views import home
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path("", home, name="anasayfa"),
    path("api/dict/", include('sozluk.api.urls')),
    path("api/account/", include('account.api.urls')),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

admin.site.site_header = "Admin Paneli"

# if settings.DEBUG==True: #TODO do not forget this
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
