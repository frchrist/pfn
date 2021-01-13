from django.db import models
from django.conf import settings
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from .utils import get_client_ip

from .signals import object_views_signal

# Create your models here.

User = settings.AUTH_USER_MODEL
class ObjectViews(models.Model):
    user = models.ForeignKey(to=User, blank=1, null=1, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey("content_type", "object_id")
    timestamp = models.DateTimeField(auto_now_add=1)
    ip_adress = models.CharField(max_length=220, null=1, blank=1)

    def __str__(self):
        return "%s viewed %s users %s"%(self.content_object, self.ip_adress,self.user)

    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Object Viewed"
        verbose_name_plural = "Objects Viewed"


def object_recever(sender, instance, request, *args, **kwargs):
    cType= ContentType.objects.get_for_model(sender)
    user = None
    if request.user.is_authenticated:
        user =request.user 
    save_obj = ObjectViews.objects.create(
        user= user,
        object_id = instance.id,
        content_type = cType,
        ip_adress=get_client_ip(request)

    )
    # print(request.user)
    # print(instance)
    # print(sender)

object_views_signal.connect(object_recever)