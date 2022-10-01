from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.db import models
from django.urls import reverse
from ckeditor.fields import RichTextField
from taggit.managers import TaggableManager
from taggit.models import GenericUUIDTaggedItemBase, TaggedItemBase
from django_extensions.db.fields import AutoSlugField
import uuid


class UUIDTaggedItem(GenericUUIDTaggedItemBase, TaggedItemBase):
    class Meta:
        verbose_name = _("Tag")
        verbose_name_plural = _("Tags")


# Create your models here.
class Post(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False
    )
    title = models.CharField(max_length=200)
    date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    slug = AutoSlugField(populate_from='title')
    feature_image = models.ImageField(upload_to="blog/feature_images/", null=True, blank=True)
    body = RichTextField()
    tags = TaggableManager(through=UUIDTaggedItem)
    clap = models.IntegerField(default=0)
    visited = models.IntegerField(default=0)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.title

    def slugify_function(self, content):
        return content.replace(' ', '-').lower()

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'slug': self.slug})
