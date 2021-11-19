from django.contrib.auth.models import User
from django.db import models
from mptt.models import MPTTModel, TreeForeignKey



class Category(MPTTModel):
    name = models.CharField(max_length=100)
    slug = models.SlugField()
    parent = TreeForeignKey(
        'self',
        related_name="children",
        on_delete=models.SET_NULL,
        null=True,
        blank=True

    )

    def __str__(self):
        return self.name



class MMTPMeta:
    order_insertion_by = ['name']


class Tag(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()


    def __str__(self):
        return self.name


class Post(models.Model):
    author = models.ForeignKey(User, related_name="posts", on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='articles/')
    text = models.TextField()
    category = models.ForeignKey(
        Category,
        related_name="post",
        on_delete=models.SET_NULL,
        null=True
    )
    tags = models.ManyToManyField(Tag, related_name="post")
    # create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Cervises(models.Model):
    name = models.CharField(max_length=100)
     #serves = models.CharField(max_lenght=50)
    # prep_time = models.PositiveIntegerField(default=0)
    # procedure_time = models.PositiveIntegerField(default=0)
    classic_manicure = models.TextField()
    european_manicure = models.TextField()
    combined_manicure = models.TextField()

    post = models.ForeignKey(
        Post,
        related_name="cervises",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

class Cervises1(models.Model):
    name = models.CharField(max_length=100)
     #serves = models.CharField(max_lenght=50)
    # prep_time = models.PositiveIntegerField(default=0)
    # procedure_time = models.PositiveIntegerField(default=0)
    eyebrow_coloring = models.TextField()
    eyebrow_correction = models.TextField()
    post = models.ForeignKey(
        Post,
        related_name="cervises1",
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )











    
    




