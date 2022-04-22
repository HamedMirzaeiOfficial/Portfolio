from django.db import models
from django.utils.text import slugify
from django.urls import reverse


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(activate=True)


class Category(models.Model):
    name = models.CharField(max_length=50)
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-last_modified', )

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=250, unique_for_date='created_on')
    image = models.ImageField(upload_to='image')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    category = models.ForeignKey("Category", related_name='posts', on_delete=models.CASCADE)
    active = models.BooleanField(default=True)

    objects = models.Manager()  # The default manager.
    published = PublishedManager()  # Our custom manager.

    class Meta:
        ordering = ('-last_modified', )

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
            super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.created_on.year,
                             self.created_on.month,
                             self.created_on.day,
                             self.slug])


class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=200, blank=True)
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    active = models.BooleanField(default=True)
    parent = models.ForeignKey('self', null=True, blank=True, related_name='replies', on_delete=models.CASCADE)

    class Meta:
        ordering = ('-created_on', )

    def __str__(self):
        return f'Comment by {self.name}'


class Advertise(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images')
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    class Meta:
        ordering = ('-last_modified', )

    def __str__(self):
        return self.title





