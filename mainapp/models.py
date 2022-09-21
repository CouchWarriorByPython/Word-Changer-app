from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=255, blank=True, verbose_name='Комментарий')
    document = models.FileField(upload_to='documents/%Y/%m/%d/', verbose_name='Файл')
    uploaded_at = models.DateTimeField(auto_now_add=True, verbose_name='Дата загрузки')

    def __str__(self):
        return f'{self.document} - {self.uploaded_at}'
