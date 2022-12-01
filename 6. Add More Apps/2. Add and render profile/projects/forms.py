from django.forms import ModelForm, widgets
from django import forms
from .models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description', 'featured_image', 'demo_link', 'source_link', 'tag']
        widgets = {
            'tag': forms.CheckboxSelectMultiple(),
        }

    def __init__(self,*args,**kwargs):
        super(ProjectForm, self).__init__(*args,**kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})

        # or targeting single field
        # self.fields['title'].widget.attrs.update({
        #     'class': 'input'
        # })
