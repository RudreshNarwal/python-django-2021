import uuid

from django.db import models


# Create your models here.
# models.Model is telling us  that this class inherit django Models

class Project(models.Model):
    title = models.CharField(max_length=200)  # defining value type
    description = models.TextField(null=True, blank=True)
    demo_link = models.CharField(max_length=2000, null=True, blank=True)
    source_link = models.CharField(max_length=2000, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True,
                          editable=False)  # we don't have to create an ID, as django by default will add it with incremented value. If you want to use uuid instead of that,
    # then, we have to specify and implement it sepecifically here.

    # to show projects with title name heading instead of uuid
    def __str__(self):
        return self.title
