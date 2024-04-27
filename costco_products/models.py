from django.db import models


# Create your models here.
# Needs Users
class Product(models.Model):
    GRAM = 'g'
    KILO = 'kg'
    OUNCE = 'oz'
    MILL = 'ml'

    WEIGHT_CHOICES = [
        (GRAM, 'Grams'),
        (KILO, 'Kilos'),
        (OUNCE, 'OZ'),
        (MILL, 'mL'),
    ]

    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    weight = models.FloatField()
    weight_unit = models.CharField(max_length=64, choices=WEIGHT_CHOICES, default=GRAM)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField(auto_now_add=True)
    updates_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        PriceHistory.objects.create(
            parent_product=Product.objects.get(id=self.id),
            price=self.current_price
        )


    def __str__(self):
        return f"{self.name} ({self.id})"


class PriceHistory(models.Model):
    parent_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.parent_product.name} ({self.price})"
