from django.urls import path
from . import views


urlpatterns = [

	path('customlanding/', views.home, name="home"),
	path('login/', views.loginPage, name="login"),
	path('register/', views.register, name="register"),
	path('logout/', views.logoutPage, name="logout"),

	path('admin/', views.admin, name="admin"),
	path('hmanlanding/', views.hman, name="hman"),



]