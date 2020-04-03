from django.db import models


class Mark(models.Model):
    value = models.CharField(max_length=32, blank=False, verbose_name=u'Оценка')

    def __str__(self):
        return self.value


class Student(models.Model):
    name = models.CharField(max_length=128, verbose_name=u'ФИО', blank=False)
    date_birth = models.DateField(blank=False)
    mark = models.ForeignKey(Mark, on_delete=models.SET_NULL, verbose_name=u"Оценка", null=True)

    def __str__(self):
        return self.name
