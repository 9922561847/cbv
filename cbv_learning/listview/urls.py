from django.urls import path

from listview import views

urlpatterns=[

        path('student/',views.StudentListView.as_view(),name = 'student')
]