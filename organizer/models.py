from django.db import models


class Tag(models.Model):
    name = models.CharField(
        max_length=31,
        unique=True,
    )
    slug = models.SlugField(
        max_length=31,
        unique=True,
        help_text='A label for URL config.'
    )

    # Note: default ordering incurs costs with multiple associated FKs
    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name


class Startup(models.Model):
    name = models.CharField(
        max_length=31,
        db_index=True,
    )
    slug = models.SlugField(
        max_length=31,
        unique=True,
        help_text='A label for URL config.'
    )
    description = models.TextField()
    founded_date = models.DateField('Date Founded')
    contact = models.EmailField()
    # Default length is 200 char - too small
    website = models.URLField(max_length=255)
    tags = models.ManyToManyField(Tag)

    class Meta:
        ordering = ['name']
        get_latest_by = 'founded_date'

    def __str__(self):
        return self.name


class NewsLink(models.Model):
    title = models.CharField(max_length=31)
    slug = models.SlugField(max_length=31)
    pub_date = models.DateField('Date Published')
    link = models.URLField(max_length=255)
    startup = models.ForeignKey(
        Startup, on_delete=models.CASCADE
    )

    class Meta:
        ordering = ['-pub_date']
        get_latest_by = 'pub_date'
        # Ensures that when slug and startup are used together, they must be unique in the db
        unique_together = ['slug', 'startup']
        verbose_name = 'News Article'

    def __str__(self):
        # Using formatted string literal to easily insert Python variables
        return f"{self.startup}: {self.title}"
