from django.urls import path

from . import views

app_name = "teacher"
urlpatterns = [
    path('home/', views.home, name="teacherHome"),
    path('get_standards/', views.getStandards, name="getStandards"),
    path('know_show_chart/', views.knowShowChart, name="knowShowChart"),
    path('save_know_show_chart/', views.saveKnowShowChart, name="saveKnowShowChart"),
    path('assessment_developer/<str:pk>/<str:assessment_id>', views.assessmentDeveloper, name="assessmentDeveloper"),
    path('save_question/<str:pk>/<str:assessment_id>', views.saveQuestion, name="saveQuestion"),
    path('create/', views.create, name="create"),
    path('know_show_selector/', views.knowShowSelector, name="knowShowSelector"),
    path('get_know_show/<str:code>/', views.getKnowShow, name="getKnowShow"),
    path('instantiate_assessment/<str:pk>/', views.createAssessment, name="createAssessment")
    ]
