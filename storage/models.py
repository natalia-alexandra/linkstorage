from django.db import models
from django.utils import timezone
# from urllib.parse import urlparse


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
    description = models.TextField(blank=True)
    # link_path = models.URLField(max_length=250, unique=True)
    link_path = models.CharField(max_length=250)
    cover = models.ImageField(
        upload_to='assets/', blank=True,  default="assets/default-img.jpg")
    cover_url = models.CharField(
        max_length=500,  default="assets/default-img.jpg", blank=True)
    alt = models.CharField(max_length=255)
    category = models.ForeignKey(Category, related_name='category',
                                 null=True, on_delete=models.CASCADE)
    private = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    # def url_text(request, self):
    #     parsed_url = urlparse(self.link_path)
    #     return parsed_url.hostname.replace("www.http://localhost:8000/storage/", "") + "/..."


# favorites
class Favorites(models.Model):
    favorites = models.ManyToManyField(Storage, related_name='favorites')
    # favorite = models.ForeignKey(
    # 'Storage', related_name='favorites', null=True, on_delete=models.CASCADE)
