from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.urls import path, include
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', home_view, name='home'),
    path("register/", register_view, name="register"),
    path("login/", login_view, name="login"),
    path("logout/", user_logout, name="logout"),
    path("profile/", profile, name="profile"),
    path("shops/", shops, name="shops"),
    path("shop/<str:u_name>/", shop_page, name="shop_page"),
    path("update_shop/<str:u_name>/", update_shop, name="update_shop"),
    path('update_user/<int:user_id>/', update_user, name='update_user'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
