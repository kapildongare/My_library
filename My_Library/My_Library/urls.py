"""
URL configuration for My_Library project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from app import views
from user_app import views as user_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("Home/", views.welcome_page, name="home_page"),
    path("show-books/", views.show_all_books, name="show_books"),
    path("show-single-book/<int:id>/", views.show_single_book, name="show_single_book"),
    path("add-book/", views.add_single_book, name="add_single_book"),
    path("update-book/<int:id>/", views.update_single_book, name="update_single_book"),
    path("delete-book/<int:id>/", views.delete_single_book, name="delete_single_book"),
    path("soft-delete-book/<int:id>/", views.soft_delete_single_book, name="soft_delete_single_book"),
    path("form-view/", views.form_view, name="form_view"),
    path("user/signup/", user_views.user_signup, name="user_signup"),
    path("user/login/", user_views.user_login, name="user_login"),
    path("user/logout/", user_views.user_logout, name="user_logout")

]

