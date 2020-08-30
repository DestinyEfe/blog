from django.apps import AppConfig


class FormviewConfig(AppConfig):
    name = 'formview'

    def ready(self):
        import formview.signals
