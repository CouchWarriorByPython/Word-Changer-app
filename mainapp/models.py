from django.db import models
from account.models import CustomUser
from django.contrib.auth.models import User


class Document(models.Model):
    WORK_SHIFT = (('д', 'Дневная'),
                  ('н', 'Ночная'))
    owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    description = models.CharField(max_length=255, blank=True, verbose_name='Комментарий')
    document = models.FileField(upload_to='documents/%Y/%m/%d/', verbose_name='Файл')
    work_shift = models.CharField(choices=WORK_SHIFT, default='д', max_length=1, verbose_name='Рабочая смена')
    number_check = models.CharField(max_length=50, verbose_name='Номер предписания', default='ABC123')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')

    def __str__(self):
        return f'{self.document} - {self.uploaded_at}'
