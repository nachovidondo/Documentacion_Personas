from rest_framework import generics

class GeneralListApiView(generics.ListAPIView):
    serializer_class = None
    def get_queryset(self):
        return self.serializer_class.Meta.model.filter(status=True)