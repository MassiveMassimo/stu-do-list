from django.forms import ModelForm
from .models import Community

class CommunityForm(ModelForm):
  class Meta:
    model = Community
    fields = "__all__"