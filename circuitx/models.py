from django.db import models

# Create your models here.

class TrainerSpeciality(Choices):
    running = Choice(value="Choice", name="Choice")

class Trainer(models.Model):
    name = models.CharField(max_length=254)
    types = models.CharField(max_length=255, choices=TrainerSpeciality.choices)
    description = models.TextField()
    price_per_hour = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name