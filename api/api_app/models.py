from django.db import models


class Women(models.Model):
    title = models.CharField(max_length=250, help_text='Имя женщины')
    content = models.CharField(max_length=200)
    time_create = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title[:2]


class MarriedWomen(Women):
    title = models.CharField(max_length=250, help_text='Имя заможней женщины')


class DivorcedWomen(Women):
    title = models.CharField(max_length=250, help_text='Имя разведенной женщины')


class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name[:5]


class Record(models.Model):
    # id will be created automatically
    name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)
