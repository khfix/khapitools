from khapi import api_core
from khapi.auth_system.permissions import ApiPermission


class ImageSearchAPI(api_core.APICore):
    def __init_subclass__(cls):
        if cls.model is None:
            raise ValueError(f"{cls.__name__} must define model class attribute")

    def post(self, request, *args, **kwargs):
        return ApiPermission.check_permissions(
            self, self.model, "ImageSearchAPI", "image_search", request, *args, **kwargs
        )
