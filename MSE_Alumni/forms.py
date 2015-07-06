'''
Created on Jun 15, 2015

@author: alvinchen
'''
from django import forms
from multiupload.fields import MultiFileField
from multiuploader.forms import MultiuploaderField

class UploadForm(forms.Form):
    attachments = MultiFileField(min_num=1, max_num=3, max_file_size=1024*1024*5)

class PostMessageForm(forms.Form):
    text = forms.CharField(label=u'Question', widget=forms.Textarea)
    uploadedFiles = MultiuploaderField(required=False)