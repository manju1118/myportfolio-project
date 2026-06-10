from django.db import models
from django.contrib.auth.models import User





class TodoCategory(models.Model):

    name = models.CharField(
        max_length=100
    )

    def __str__(self):

        return self.name





class Todo(models.Model):
    PRIORITY_CHOICES = (

        ('High', 'High'),

        ('Medium', 'Medium'),

        ('Low', 'Low')

    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE
    )

    title = models.CharField(
        max_length=200
    )
    
    priority = models.CharField(
        max_length=10,
        choices=PRIORITY_CHOICES,
        default='Medium'
    )

    due_date = models.DateField(
        null=True,
        blank=True
    )
    category = models.ForeignKey(

    TodoCategory,

    on_delete=models.CASCADE,

    null=True,

    blank=True

    )
    description = models.TextField()

    is_completed = models.BooleanField(
        default=False
    )

    created_at = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):

        return self.title
    

