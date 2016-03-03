from django import forms
from task.models import Task


class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        # exclude = ['author', 'updated', 'created', ]
        fields = ('title', 'description')
        widgets = {
            'title': forms.TextInput(
                attrs={'id': 'task-title', 'required': True, 'placeholder': 'The name of the Task..'}
            ),
            'description': forms.TextInput(
                attrs={'id': 'task-description', 'required': True, 'placeholder': 'Description of the Task'}
            ),
        }
