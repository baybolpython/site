from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Xiaomi(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

SIM_CARDS = (
    ('O!', 'O!'),
    ('BEELINE', 'BEELINE'),
    ('Mega com', 'Mega com'),
)


class Redmi(models.Model):
    name = models.CharField(max_length=200, verbose_name='Имя')
    image = models.ImageField(upload_to='redmi_images/', verbose_name='Фото')
    specifications = models.TextField(verbose_name='Характеристека')
    sim_card = models.CharField(max_length=10, choices=SIM_CARDS, verbose_name='Sim_card')
    price = models.IntegerField(default=0, verbose_name='Цена')
    created_at = models.DateTimeField(auto_now_add=True)
    # xiaomi = models.ForeignKey(Xiaomi, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Redmi"
        verbose_name_plural = "редми"





class Comment(models.Model):
    redmi = models.ForeignKey(Redmi, on_delete=models.CASCADE, related_name='redmi', null=True)
    text = models.TextField()
    stars = models.PositiveIntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)], null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.stars} - {self.redmi}"

    class Meta:
        verbose_name = "Коментарий"
        verbose_name_plural = "Коментарии"