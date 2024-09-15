from django.urls import path

from . import views

app_name = 'timetable'

urlpatterns = [
    path('', views.TimetableView.as_view(), name='timetable'),
    path('lesson/create', views.LessonCreateView.as_view(), name='lesson_create'),
    path('lesson/<int:pk>/', views.LessonDetailView.as_view(), name='lesson_detail'),
    path('lesson/<int:pk>/update', views.LessonUpdateView.as_view(), name='lesson_update'),
    path('lesson/<int:pk>/delete', views.LessonDeleteView.as_view(), name='lesson_delete'),

    # path('week/', views.TimetableView.as_view(), name='timetable_week'),
    # path('month/', views.TimetableView.as_view(), name='timetable_month'),

]
