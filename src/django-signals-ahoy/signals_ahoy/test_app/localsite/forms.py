from django import forms
from signals_ahoy import signals
import logging
log = logging.getLogger('localsite.forms')

class ExampleForm(forms.Form):
    name = forms.CharField(max_length=30, label='Name', required=True)

    def __init__(self, *args, **kwargs):
        initial = kwargs.get('initial', {})
        signals.form_initialdata.send(ExampleForm, form=self, initial=initial)
        kwargs['initial'] = initial
        super(ExampleForm, self).__init__(*args, **kwargs)
        signals.form_init.send(ExampleForm, form=self)

    def clean(self, *args, **kwargs):
        super(ExampleForm, self).clean(*args, **kwargs)
        signals.form_validate.send(ExampleForm, form=self)
        return self.cleaned_data

    def save(self):
        data = self.cleaned_data
        signals.form_presave.send(ExampleForm, form=self)
        signals.form_postsave.send(ExampleForm, form=self)
        return self.cleaned_data
        