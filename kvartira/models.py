from django.db import models


class Kvartira(models.Model):
    title = models.CharField(max_length=30)
    deck = models.TextField()
    locashion = models.CharField(max_length=100)
    image = models.ImageField(upload_to="kvartira-imges/",blank=True, null= True, default="default/kvartira.jpg")
    price = models.DecimalField(max_digits=12, decimal_places=2)
    created_at = models.TimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title