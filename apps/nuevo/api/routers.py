
from rest_framework.routers import DefaultRouter
from apps.nuevo.api.views.views import PersonaViewset,ProfesionesViewset

router = DefaultRouter()
router.register(r'persona', PersonaViewset, basename = "persona")
router.register(r'profesiones',ProfesionesViewset,basename = "profesiones")

urlpatterns = router.urls



