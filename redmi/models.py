from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

SIM_CARDS = (
    ('O!', 'O!'),
    ('BEELINE', 'BEELINE'),
    ('Mega com', 'Mega com'),
)


class Redmi(models.Model):
    name = models.CharField(max_length=200, verbose_name='Название')
    image = models.ImageField(upload_to='redmi_images/', verbose_name='Фото')
    specifications = models.TextField(verbose_name='Характеристека')
    sim_card = models.CharField(max_length=10, choices=SIM_CARDS, verbose_name='Sim_card')
    price = models.IntegerField(default=0, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Redmi"
        verbose_name_plural = "редми"


class Comment(models.Model):
    post = models.ForeignKey('Redmi', on_delete=models.CASCADE, related_name='comments')  # Связь с моделью постов
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'Comment by {self.author} on {self.post}'

    class Meta:
        ordering = ['-created_at']



