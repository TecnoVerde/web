from django.db import models

class login(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'login'

    def __str__(self):
        return self.name
    
    
