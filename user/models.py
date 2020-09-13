from django.db import models
from django.utils.text import slugify

# Create your models here.
class Tshirt(models.Model):
    label = models.CharField(max_length=50, null=False, unique=True)
    img_url = models.ImageField(upload_to ='tshirts/')

    def __str__(self):
        return f"{self.label}"

class TshirtRoom(models.Model):
    name = models.CharField(max_length=50, null=False)
    tshirt = models.ForeignKey(Tshirt, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=100, unique=True)

    def _get_unique_slug(self):
        slug = slugify(self.name)
        unique_slug = slug
        num = 1
        while TshirtRoom.objects.filter(slug=unique_slug).exists():
            unique_slug = '{}-{}'.format(slug, num)
            num += 1
        return unique_slug

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = self._get_unique_slug()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name}"

class Friend(models.Model):
    name = models.CharField(max_length=50, null=False)
    tshirt_room = models.ForeignKey(TshirtRoom, on_delete=models.CASCADE)
    key_points = models.TextField()
    ip = models.CharField(max_length=20)
    color = models.CharField(max_length=10, default='#000000')

    def __str__(self):
        return f"{self.name}"