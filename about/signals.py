from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import AboutUs

@receiver(pre_save, sender=AboutUs)
def delete_old_image(sender, instance, *args, **kwargs):
    if instance.pk:
        existing_image = AboutUs.objects.get(pk=instance.pk)
        if instance.image and existing_image.image != instance.image:
            existing_image.image.delete(False)