from django.db import models

class Plan(models.Model):
    
    """Plan Model Definition"""
    
    date = models.DateField()
    content = models.TextField()
    isChecked = models.BooleanField(default=False)
    emoji = models.CharField(
        max_length=1,
        default="",
        blank=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.content
