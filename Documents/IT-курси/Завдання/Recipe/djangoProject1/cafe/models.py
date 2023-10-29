from django.db import models


# Create your models here.
class DishCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    position = models.PositiveIntegerField(unique=True)
    is_visible = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'

    class Meta:
        ordering = ('position', )

class Dish(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True, db_index=True)
    position = models.PositiveIntegerField(unique=True)
    ingredients = models.CharField(max_length=250)
    desc = models.TextField(max_length=500, blank=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    weight = models.PositiveIntegerField(blank=True)
    photo = models.ImageField(upload_to='dishes/', blank=True)
    category = models.ForeignKey(DishCategory, on_delete=models.PROTECT, related_name='dishes')

    is_visible = models.BooleanField(default=True)