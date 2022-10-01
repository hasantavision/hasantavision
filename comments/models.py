from django.db import models
from django.contrib.auth import get_user_model
from ckeditor.fields import RichTextField


# Create your models here.
class Comment(models.Model):
    author = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
    )
    date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        "blog.Post",
        on_delete=models.CASCADE
    )
    comment = RichTextField(config_name='comment', max_length=1000)

    class Meta:
        ordering = ['-date']

    def __str__(self):
        return self.comment
