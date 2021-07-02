from django.urls import path

from detailview import views

urlpatterns = [
    path('studentdetailview/<int:id>',views.StudentDetailView.as_view(),name='studentdetailview'),
    path('studentlist/',views.StuListView.as_view(),name='studentlist'),
]