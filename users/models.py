from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, **kwargs):
        super(Profile,self).save()
        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            old_size = img.size
            ratio = 300 / min(old_size)
            new_size = tuple([int(dimention * ratio) for dimention in old_size])
            img = img.resize(new_size)
            height = img.height
            width = img.width
            left = (width - 300) / 2
            right = (width + 300) / 2
            top = (height - 300) / 2
            bottom = (height + 300) / 2
            img = img.crop((left, top, right, bottom))
            # output_size = (300,300)
            # img.thumbnail(output_size)
            img.save(self.image.path)