from django.conf import settings
from django.utils.deconstruct import deconstructible
from storages.backends.gcloud import GoogleCloudStorage


@deconstructible
class PrivateGCSMediaStorage(GoogleCloudStorage):
    def __init__(self, *args, **kwargs):
        kwargs["bucket_name"] = getattr(settings, "GS_BUCKET_NAME")
        super().__init__(*args, **kwargs)
