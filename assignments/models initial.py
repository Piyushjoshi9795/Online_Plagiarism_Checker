from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
import uuid
from django.core.validators import FileExtensionValidator


class Assignment(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=600)
    date = models.DateTimeField(auto_now_add=True)
    deadline = models.DateField()
    by_teacher = models.ForeignKey(get_user_model(),
                                   on_delete=models.CASCADE, )

    class Meta:
        ordering = ('-date',)

    # class Meta:
    #     permissions = [
    #         ('special_status', 'Can read all books'),
    #     ]
    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('assignment_detail', args=[str(self.id)])


def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'assignments/user_{0}/{1}'.format(instance.student.username, filename)


class UploadedAssignment(models.Model):
    id = models.UUIDField(primary_key=True,
                          default=uuid.uuid4,
                          editable=False)
    assignment = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name='assignment')
    student = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='assignment_uploaded' )
    upload_file = models.FileField(upload_to=user_directory_path, validators=[FileExtensionValidator(allowed_extensions=['pdf', 'docx'])])
    uploaded_date = models.DateField(auto_now_add=True,
                                     db_index=True)

    class Meta:
        ordering = ('-uploaded_date',)

    # def __str__(self):
    #     return self.str('uploaded_file')

    def get_absolute_url(self):
        return reverse('uploaded_detail', args=[str(self.id)])
