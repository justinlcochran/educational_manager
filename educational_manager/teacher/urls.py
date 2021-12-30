from django.urls import path

from . import views

app_name = "teacher"
urlpatterns = [
    path('home/', views.home, name="teacherHome"),
    path('get_standards/', views.getStandards, name="getStandards"),
    path('know_show_chart/', views.knowShowChart, name="knowShowChart"),
    path('save_know_show_chart/', views.saveKnowShowChart, name="saveKnowShowChart"),
    path('assessment_developer/<str:pk>/', views.assessmentDeveloper, name="assessmentDeveloper"),
    path('save_question/<str:pk>/', views.saveQuestion, name='saveQuestion'),
    ]
