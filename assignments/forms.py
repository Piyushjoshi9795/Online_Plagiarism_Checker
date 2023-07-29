from .models import UploadAssignment, GiveAssignment
from django import forms


class DateInput(forms.DateInput):
    input_type = 'date'


class AssignmentUploadForm(forms.ModelForm):
    class Meta:
        model = UploadAssignment
        fields = ['upload_file', ]


class AssignmentGiveForm(forms.ModelForm):
    class Meta:
        model = GiveAssignment
        fields = ['subject', 'title', 'description', 'deadline']
        widgets = {
            'deadline': DateInput(),
        }


class StatusChangeForm(forms.ModelForm):
    class Meta:
        model = UploadAssignment
        fields = ['status']
