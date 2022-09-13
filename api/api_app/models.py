from django.db import models


# Create your models here.
class Women(models.Model):
    title = models.CharField(max_length=250)
    content = models.CharField(max_length=200)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title[:5]


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name[:5]