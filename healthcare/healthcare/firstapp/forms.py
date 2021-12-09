from django import forms 
from .models import *
  
class XrayUploadForm(forms.ModelForm):
  
    class Meta: 
        model = XrayUpload
        fields = ['xray_image']