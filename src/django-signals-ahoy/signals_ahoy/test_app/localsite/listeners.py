from signals_ahoy import signals
from tests.localsite.forms import ExampleForm
from django import forms
import logging
log = logging.getLogger('localsite.listeners')

def base_search_listener(sender, results={}, **kwargs):
    results['base'] = 'Base search results'

def form_initialdata_listener(sender, form=None, initial={}, **kwargs):
    log.info('form_initialdata_listener')
    initial['email'] = "a@example.com"
    initial['name'] = 'test'

def form_init_listener(sender, form=None, **kwargs):
    log.info('form_init_listener: %s', sender)
    form.fields['email'] = forms.EmailField('Email', required=True)
    
def form_validate_listener(sender, form=None, **kwargs):
    """Do custom validation on form"""
    data = form.cleaned_data
    email = data.get('email', None)
    if email != 'test@example.com':
        errors = form.errors
        if 'email' not in errors:
            errors['email'] = []
        errors['email'].append('Email must be "test@example.com"')

def form_presave_listener(sender, form=None, **kwargs):
    form.cleaned_data['presave'] = 'presave'

def form_postsave_listener(sender, form=None, data={}, **kwargs):
    form.cleaned_data['postsave'] = 'postsave'

def keywords_search_listener(sender, results={}, keywords={}, **kwargs):
        results['keywords'] = ','.join(keywords)
        
def signalled_view_listener(sender, context={}, **kwargs):
    context['data'] = "modified"

def start_listening():
    signals.application_search.connect(base_search_listener, sender=None)
    signals.application_search.connect(keywords_search_listener, sender=None)
    signals.view_prerender.connect(signalled_view_listener, sender='signalled_view')
    signals.form_init.connect(form_init_listener, sender=ExampleForm)
    signals.form_initialdata.connect(form_initialdata_listener, sender=ExampleForm)
    signals.form_validate.connect(form_validate_listener, sender=ExampleForm)
    signals.form_presave.connect(form_presave_listener, sender=ExampleForm)
    signals.form_postsave.connect(form_postsave_listener, sender=ExampleForm)
    