from django.db import models

class Redmi(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='redmi_images/')
    specifications = models.TextField()
    price = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
