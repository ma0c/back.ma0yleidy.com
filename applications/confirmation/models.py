from django.db import models

from ma0yleidy_back.base_model import BaseModel


class Confirmation(BaseModel):
    slug = models.SlugField(max_length=500, unique=True, null=True)
    is_confirmed = models.BooleanField(null=True, blank=True, default=None)
    minutes = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"Confirmation for {self.slug}"

    def __repr__(self):
        return f"self.slug"

    class Meta:
        indexes = [
            models.Index(fields=['slug'], name='unique_slug_index')
        ]
        constraints = [
            models.UniqueConstraint(fields=['slug'], name='unique_slug_constraint')
        ]
