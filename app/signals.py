from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import University, FeedBackByStudent


@receiver(pre_save, sender=University)
def delete_old_image(sender, instance, *args, **kwargs):
    if instance.pk:
        existing_image = University.objects.get(pk=instance.pk)
        if instance.cover_photo and existing_image.cover_photo != instance.cover_photo:
            existing_image.cover_photo.delete(False)
        if instance.uni_logo and existing_image.uni_logo != instance.uni_logo:
            existing_image.uni_logo.delete(False)

@receiver(pre_save, sender=FeedBackByStudent)
def delete_old_image(sender, instance, *args, **kwargs):
    if instance.pk:
        existing_image = FeedBackByStudent.objects.get(pk=instance.pk)
        if instance.image and existing_image.image != instance.image:
            existing_image.image.delete(False)