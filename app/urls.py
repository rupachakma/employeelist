from django.contrib import admin
from django.urls import path

from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.signuppage, name="signuppage"),
    path('loginpage', views.loginpage, name="loginpage"),
    path('logoutpage', views.logoutpage, name="logoutpage"),
    path('homepage', views.homepage, name="homepage"),
    path('addpage', views.addpage, name="addpage"),
    path('updatepage/<int:id>', views.updatepage, name="updatepage"),
    path('deletepage/<int:id>', views.deletepage, name='deletepage'),
    path('update_profile', views.update_profile, name="update_profile"),
]
