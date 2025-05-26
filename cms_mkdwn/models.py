from django.db import models
from django.urls import reverse

# Create your models here.


class MarkdownContent(models.Model):
    order = models.IntegerField()
    title = models.CharField(max_length=100)
    content = models.TextField()
    source_fp = models.FilePathField("")

    class Meta:
        verbose_name_plural = "Markdown Content"

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Access the detail record of this content
        """

        return reverse("cms_mkdwn:content-detail", args=[str(self.pk)])
