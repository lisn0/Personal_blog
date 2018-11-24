from django.contrib import admin
from django.urls import path, include
from users import views as user_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('_register/', user_views.register, name="register"),
    path('', include('blog.urls')),
]
