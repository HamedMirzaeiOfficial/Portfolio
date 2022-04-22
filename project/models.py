from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(activate=True)


class Project(models.Model):
    title = models.CharField(max_length=300)
    slug = models.SlugField(max_length=250, unique_for_date='created_on')
    body = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images')
    created_on = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
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
            super(Project, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('blog:post_detail',
                       args=[self.created_on.year,
                             self.created_on.month,
                             self.created_on.day,
                             self.slug])
