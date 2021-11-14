from django.db.models.signals import pre_save
from django.dispatch import receiver
from .models import University, FeedBackByStudent, Consultancy, HomePageInfo


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


@receiver(pre_save, sender=Consultancy)
def delete_old_image(sender, instance, *args, **kwargs):
    if instance.pk:
        existing_image = Consultancy.objects.get(pk=instance.pk)
        if instance.logo_photo and existing_image.logo_photo != instance.logo_photo:
            existing_image.logo_photo.delete(False)

@receiver(pre_save, sender=HomePageInfo)
def delete_old_image(sender, instance, *args, **kwargs):
    if instance.pk:
        existing_image = HomePageInfo.objects.get(pk=instance.pk)
        if instance.heading_first_image and existing_image.heading_first_image != instance.heading_first_image:
            existing_image.heading_first_image.delete(False)
        if instance.heading_second_image and existing_image.heading_second_image != instance.heading_second_image:
            existing_image.heading_second_image.delete(False)
        if instance.stats_image and existing_image.stats_image != instance.stats_image:
            existing_image.stats_image.delete(False)