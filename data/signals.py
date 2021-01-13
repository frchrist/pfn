from django.dispatch import Signal

object_views_signal = Signal(providing_args=["instance", "request"])
