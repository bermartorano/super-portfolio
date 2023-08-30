from django.db import models


class Profile(models.Model):
    name = models.CharField(max_length=200, null=False, blank=False)
    github = models.URLField()
    linkedin = models.URLField()
    bio = models.TextField(
            null=False,
            blank=False,
            max_length=500,
            )

    def __str__(self) -> str:
        return self.name
