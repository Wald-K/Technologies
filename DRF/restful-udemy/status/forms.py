from django import forms

from .models import Status

class StatusForm(forms.ModelForm):
    class Meta:
        model = Status
        fields = [
            'user',
            'content',
            'image'
        ]

    def clean_content(self):
        data = self.cleaned_data.get('content')
        if len(data) > 100:
            raise forms.ValidationError('Content to long. Max content length is 100')
        return data


    def clean(self):
        cleaned_data = super().clean()

        content = cleaned_data.get('content', None)
        if content == '':
            content = None

        image = cleaned_data.get('image', None)
        if image == '':
            image = None

        if (content is None) and (image is None):
            raise forms.ValidationError('Content or image is required')



