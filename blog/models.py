from django.db import models

from django_extensions.db.fields import AutoSlugField

from organizer.models import Startup, Tag


class Post(models.Model):
    title = models.CharField(max_length=63)
    slug = AutoSlugField(
        max_length=63,
        populate_from=['title'],
    )
    text = models.TextField()
    pub_date = models.DateField('Date Published')
    tags = models.ManyToManyField(Tag,
                                  related_name="blog_posts")
    startups = models.ManyToManyField(Startup,
                                      related_name="blog_posts")

    class Meta:
        get_latest_by = 'pub_date'
        ordering = ['-pub_date', 'title']
        # Shows in admin view
        verbose_name = 'Blog Post'

    def __str__(self):
        date_string = self.pub_date.strftime("%Y-%m-%d")
        return f"{self.title} on {date_string}"
