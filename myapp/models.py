from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.name


class Author(models.Model):
    name = models.CharField(max_length=14, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=14)
    content = models.TextField(max_length=1000)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    author = models.ForeignKey(Author, on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True, blank=True)

    def __str__(self):
        return f"{self.title} | author: {self.author}\n {self.created_at}"