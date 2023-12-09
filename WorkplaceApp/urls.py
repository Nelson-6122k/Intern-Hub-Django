from django.urls import path
from . import views


urlpatterns = [
    path('', views.login,name="login"),
    path('acctype', views.selectacctype, name="acctype"),
    path('stuacc', views.createstuacc, name="stuacc" ),
    path('comacc', views.createcomacc, name="comacc" ),
    path('stufeed/<str:stuid>/', views.stufeed, name="stufeed"),
    path('addpost/<str:comid>/', views.comaddpost, name="addpost"),
    path('mypost/<str:comid>/', views.mypost, name="mypost"),
    path('addtofav/<str:stuid>,<str:fid>/', views.addtofav, name="addtofav"),
    path('stufav/<str:stuid>/', views.stufav, name="stufav"),
    path('removefrmfav/<str:stuid>,<str:fid>/', views.removefrmfav, name="removefrmfav"),
    path('logout/', views.logout, name="logout"),
    path('editpost/<str:comid>,<str:fid>/', views.editpost, name="editpost"),
    path('deletepost/<str:comid>,<str:fid>/', views.deletepost, name="deletepost"),
    path('apply/<str:stuid>,<str:fid>/', views.apply, name="apply"),
    path('comnotifications/<str:comid>/', views.ComNotifications, name="ComNotifications"),
    path('markasreadCom/<str:comid>,<str:notid>/', views.markasreadCom, name="markasreadCom"),
    path('StuNotifications/<str:stuid>/', views.StuNotifications, name="StuNotifications"),
    path('markasreadStu/<str:stuid>,<str:notid>/', views.markasreadStu, name="markasreadStu"),
    path('commsg/<str:comid>/', views.commsg, name="commsg"),
    path('comchat/<str:comid>,<str:senderid>/', views.comchat, name="comchat"),
    path('msgseen/<str:comid>,<str:msgid>/', views.msgseen, name="msgseen"),
    path('stumsg/<str:stuid>/', views.stumsg, name="stumsg"),
    path('stumsgseen/<str:stuid>,<str:msgid>/', views.stumsgseen, name="stumsgseen"),
    path('stuchat/<str:stuid>,<str:senderid>/', views.stuchat, name="stuchat"),
    path('viewCompany/<str:stuid>,<str:comid>/', views.viewCompany, name="viewCompany"),
]