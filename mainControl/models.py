from django.urls import reverse
from django.db import models
from django.core import validators

class Students(models.Model):
    name = models.CharField(max_length=50)
    student_id = models.IntegerField()
    email = models.EmailField(validators=[validators.EmailValidator('enter a valid Email')])

    def __str__(self) -> str:
        return self.name + ' ' + str(self.student_id)

    def get_absolute_url(self):
        return reverse('mainApp:student-info2', kwargs={'pk': self.pk})

class Students_Information(models.Model):
    students_information = models.ForeignKey(Students, on_delete=models.CASCADE, related_name='student_info')

    registration_semester = models.CharField(max_length=30)
    registration_year = models.IntegerField(validators=[validators.MaxValueValidator(2030), validators.MinValueValidator(1990)])
    phone = models.IntegerField()
    date_of_birth = models.DateField()

    def __str__(self) -> str:
        return str(self.phone) + '  ' + str(self.date_of_birth)