from. import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    # path('details/',views.details,name='details'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:id>/',views.update,name='update'),
    path('cbhome/',views.tasklistview.as_view(),name='cbhome'),
    path('cbdetail/<int:pk>/',views.taskdetailview.as_view(),name='cbdetail'),
    path('cbedit/<int:pk>/',views.taskupdateview.as_view(),name='cbedit'),
    path('cbdelete/<int:pk>/',views.taskdeleteview.as_view(),name='cbdelete'),
]

