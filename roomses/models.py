from django.db import models

# slug model
class room(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
