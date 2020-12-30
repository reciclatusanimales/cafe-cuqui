from django.db import models
from django.contrib.auth.models import User
from taggit.managers import TaggableManager

class Post(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey('Category', null=True, on_delete=models.SET_NULL)
    # tags = 
    created_at = models.DateTimeField(auto_now_add=True)
    tags = TaggableManager(blank=True)

    def __str__(self):
        return self.title

class Category(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Comment by {}".format(self.author)