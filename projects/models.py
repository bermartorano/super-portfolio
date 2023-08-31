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


class Project(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    github_url = models.URLField()
    keyword = models.CharField(max_length=500)
    key_skill = models.CharField(max_length=50)
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="projects",
        default=2,
    )

    def __str__(self) -> str:
        return self.name


class CertifyingInstitution(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    url = models.URLField(null=False, blank=False)

    def __str__(self) -> str:
        return self.name


class Certificate(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False)
    certifying_institution = models.ForeignKey(
        CertifyingInstitution,
        on_delete=models.CASCADE,
        related_name="certificates",
        blank=False,
        null=False,
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    profiles = models.ManyToManyField(
        "Profile",
        related_name="certificates",
    )
