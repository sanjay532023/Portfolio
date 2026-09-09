from django.urls import path
from . import views
urlpatterns=[
    path("",views.home,name="home"),
    path("playlist/<int:pk>/",views.playlist_detail,name="playlist_detail"),
    path("admin-login/",views.admin_login,name="admin_login"),
    path("dashboard/",views.dashboard,name="dashboard"),
    path("logout/",views.admin_logout,name="logout"),
    path("delete-playlist/<int:pk>/",views.delete_playlist,name="delete_playlist"),
    path("delete-track/<int:pk>/",views.delete_track,name="delete_track"),
]
