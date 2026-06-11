from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
import uuid
from django.core.validators import MaxValueValidator, MinValueValidator

class Category(models.Model):
    name = models.CharField(
        max_length=100,
        unique=True
    )
    slug = models.SlugField(
        unique=True,
        blank=True
    )
    image = models.ImageField(
        upload_to='categories/',
        blank=True,
        null = True
    )
    
    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
            super().save(
                *args,
                **kwargs
            )

    def __str__(self):
        return self.name
    

class Product(models.Model):
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='products',
    )
    title = models.CharField(
        max_length=200
    )
    slug = models.SlugField(
        unique=True,
        blank=True
    )
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )
    stock = models.PositiveIntegerField(default=1)
    is_featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):

        if not self.slug:

            base_slug = slugify(
                self.title
            )

            slug = base_slug

            while Product.objects.filter(
                slug=slug
            ).exists():

                slug = f"{base_slug}-{uuid.uuid4().hex[:8]}"

            self.slug = slug

        super().save(
            *args,
            **kwargs
        )

    def __str__(self):

        return self.title

class Cart(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(
        default=1
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:
        unique_together = (
            'user',
            'product'
        )

    def __str__(self):

        return f"{self.user.username} - {self.product.title} (x{self.quantity})"
    
class Order(models.Model):

    STATUS_CHOICES = (

        ('Pending','Pending'),

        ('Processing','Processing'),

        ('Shipped','Shipped'),

        ('Delivered','Delivered')

    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    full_name = models.CharField(
        max_length=200
    )

    phone = models.CharField(
        max_length=20
    )

    address = models.TextField()

    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Pending'
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"Order #{self.id}"
    
class Wishlist(models.Model):

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    class Meta:

        unique_together = (
            'user',
            'product'
        )

    def __str__(self):

        return self.product.title
    

class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )
    rating = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(5)
        ]
    )
    comment = models.TextField()
    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return f"{self.user.username} - {self.rating}⭐"