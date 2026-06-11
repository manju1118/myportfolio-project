from django.db import models
from django.utils.text import slugify
import uuid

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