## Getting Started

### Installation

To install `khapitools`, `khapi`, `ImageHash`, and `Pillow`, use the following commands in your terminal:

```bash
pip install khapitools
pip install khapi
pip install ImageHash
pip install Pillow
```
Visit [Khapi](https://github.com/khfix/django-khapi)
for installing khapi.


### Example

```python

# app/models.py
from django.db import models
from khapi.methods import khapi_upload_path

class YourModel(models.Model):
    photo = models.ImageField(upload_to=khapi_upload_path)

# app/views.py
from khapitools.views import ImageSearchAPI
from .models import YourModel  

class YourModelImageSearchAPI(ImageSearchAPI):
    model = YourModel 

# app/urls.py
from khapi.khapi_start import khapi_cache_start
from . import views
from django.urls import path

khapi_cache_start()

urlpatterns = [
    path(views.TestImageSearchAPI.as_api(), name="image-search"),
]

```
### API POST Request

In your API POST request, send the image file as the value with "Image" as the key name. The API will return [mention the expected result].

![Postman Image Upload](images/postman_image_upload.png)





### License

This project is licensed under the MIT License.

### Support

For questions or issues, please open an issue or contact us at [hamza.alkhatib.se@gmail.com](mailto:hamza.alkhatib.se@gmail.com)



### Acknowledgments
Thanks to the Django community.


