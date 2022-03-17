from django.urls import path
from mainControl import views

app_name = 'mainApp'

urlpatterns = [
    path("", views.home, name="home"),
    path("srform/", views.studentRegistrationForm, name="srform"),
    path('allStudents/', views.allStudents, name='allStudents'),
    path('sInformation/', views.siForm, name='informationForm'),
    path('class-view/', views.IndexView.as_view(), name='class-view'),
    path('list-view/', views.StudentListView.as_view(), name='list-view'),
    path('student-info/<int:pk>/', views.SiViews, name='student-info'),
    path('student-info2/<pk>/', views.SiView2.as_view(), name='student-info2'),
    path("srform2/", views.AddStudent.as_view(), name="srform2"),
]