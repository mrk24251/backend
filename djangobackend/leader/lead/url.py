from rest_framework import routers
from .api import mohammadset

router= routers.DefaultRouter()
router.register('api/lead',mohammadset, 'lead')

urlpatterns = router.urls