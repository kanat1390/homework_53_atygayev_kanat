from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
STATUS_CHOICES = [
    ('N', 'Новая'),
    ('P', 'В процессе'),
    ('C', 'Выполнена')
]

class Todo(models.Model):
    description = models.CharField(verbose_name='Описание', max_length=300, null=False, blank=False)
    status = models.CharField(verbose_name='Статус', choices=STATUS_CHOICES, max_length=1, null=False, blank=False, default=STATUS_CHOICES[0][0])
    text = RichTextField(null=True, blank=True)
    date = models.DateField(verbose_name='Дата закрытия', null=True, blank=True)

    def __str__(self):
        return f'{self.description} - {self.status}'
    
    def get_choice(self, choice):
        return [c[0] for c in STATUS_CHOICES if c == choice]

