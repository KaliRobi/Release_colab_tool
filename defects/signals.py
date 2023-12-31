from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.crypto import get_random_string
from django.utils.text import slugify
from defects.models import Defect

# when pre_save is triggered on Defect this will be called 
@receiver(pre_save, sender=Defect)
def unique_identifier_generator(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        slug = slugify(instance.defect_number)
        random_string = get_random_string(length=6)
        instance.slug = slug + "-" + random_string