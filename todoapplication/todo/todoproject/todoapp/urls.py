from django.urls import path
from django.contrib import admin
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.add,name='add'),
   # path('detail/',views.detail,name='detail'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbvhome/',views.tasklistview.as_view(),name='cbvhome'),
    path('detail/<int:pk>/',views.detailview.as_view(),name='detail'),
    path('cbvupdate/<int:pk>/',views.updateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.deleteview.as_view(),name='cbvdelete')


]