from django.db import models

class ImagePicker(models.Model):
    image = models.ImageField()

    def get_url(self):
        return self.image.url
