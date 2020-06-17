from django.db import models


class About(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='about/')

    class Meta:
        verbose_name_plural = 'About'

    def __str__(self):
        return self.title

class Choose(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()

    class Meta:
        verbose_name_plural = 'Choose'

    def __str__(self):
        return self.title

class Chef(models.Model):
    name = models.CharField(max_length=50)
    subtitle = models.CharField(max_length=50)
    bio = models.TextField()
    image = models.ImageField(upload_to='chef/')

    def __str__(self):
        return self.name
