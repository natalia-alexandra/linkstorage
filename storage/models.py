from django.db import models
from django.utils import timezone


# category
class Category(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


# storage
class Storage(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    link_path = models.URLField(max_length=250, unique=True)
    cover = models.ImageField(upload_to='assets/', blank=True)
    cover_url = models.CharField(max_length=500, default=None, blank=True)
    alt = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='category',
                                 null=True, on_delete=models.CASCADE)
    private = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


# favorites
class Favorites(models.Model):
    favorites = models.ManyToManyField(Storage, related_name='favorites')
    # favorite = models.ForeignKey(
    # 'Storage', related_name='favorites', null=True, on_delete=models.CASCADE)
