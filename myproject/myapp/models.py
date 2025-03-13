from django.db import models

# Create your models here

class Home(models.Model):
    CATEGORY_CHOICES = [
        ('Electronics', 'Electronics'),
        ('Property','Property'),
        ('Clothing', 'Clothing'),
        ('Furniture', 'Furniture'),
        ('Books', 'Books'),
        ('Others', 'Others'),
    ]

    item_name = models.CharField(max_length=255)
    item_category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Others')
    item_description = models.TextField()
    item_photo = models.ImageField(upload_to='images/')
    item_price = models.DecimalField(max_digits=10, decimal_places=2)
    posted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.item_name
