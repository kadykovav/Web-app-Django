from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from .forms import LessonForm
from .models import Timetable

from datetime import date

TODAY = date.today()


class TimetableView(ListView):
    template_name = 'timetable/timetable_day.html'
    model = Timetable
    context_object_name = 'timetable'
    extra_context = {'today': TODAY}


class LessonCreateView(CreateView):
    form_class = LessonForm
    template_name = 'timetable/lesson_create.html'
    model = Timetable
    success_url = reverse_lazy('timetable:timetable')


class LessonUpdateView(UpdateView):
    form_class = LessonForm
    template_name = 'timetable/lesson_update.html'
    model = Timetable
    success_url = reverse_lazy('timetable:timetable')


class LessonDeleteView(DeleteView):
    model = Timetable
    success_url = reverse_lazy('timetable:timetable')
    template_name = 'timetable/lesson_update.html'
    context_object_name = 'timetable'


class LessonDetailView(DetailView):
    model = Timetable
    template_name = 'timetable/lesson_detail.html'
    context_object_name = 'timetable'
