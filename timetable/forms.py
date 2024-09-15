from django import forms

from .models import Timetable


class LessonForm(forms.ModelForm):
    class Meta:
        model = Timetable
        fields = ['start', 'end', 'teacher', 'student', 'comment']
        widgets = {
            'start': forms.DateTimeInput(attrs={'class': 'form-control',
                                                'type': 'datetime-local'}),
            'end': forms.DateTimeInput(attrs={'class': 'form-control',
                                              'type': 'datetime-local'}),
            'teacher': forms.Select(attrs={'class': 'form-select'}),
            'student': forms.Select(attrs={'class': 'form-select'}),
            'comment': forms.Textarea(attrs={'class': 'form-control'})
        }
        labels = {
            'start': 'Начало',
            'end': 'Конец',
            'teacher': 'Учитель',
            'student': 'Ученик',
            'comment': 'Комментарий',
        }

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     a = self.fields['teacher']
    #     print(a)
