from django.urls import path, re_path
from hello import views, views2

app_name = 'hello'
urlpatterns = [
    path('', views.index, name='index'),
    path('userlistformview/', views2.UserListFormView.as_view(), name='userlistFormview'),
    path('useraddformview/', views2.UserAddFormView, name='useraddFormview'),
    re_path('userdetailformview/(?P<pk>[0-9]{1,})?', views2.UserDetailFormView.as_view(), name='userdetailFormview'),
    # re_path('usermodformview/(?P<pk>[0-9]{1,})?', views2.UserModFormView, name='usermodFormview'),
    
    # path('js/', views2.JsView.as_view(), name='js'),
]
