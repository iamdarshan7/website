from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import University


@receiver(pre_save, sender=University)
def delete_old_image(sender, instance, *args, **kwargs):
    if instance.pk:
        existing_image = University.objects.get(pk=instance.pk)
        if instance.cover_photo and existing_image.cover_photo != instance.cover_photo:
            existing_image.cover_photo.delete(False)
        if instance.uni_logo and existing_image.uni_logo != instance.uni_logo:
            existing_image.uni_logo.delete(False)