from signals_ahoy import signals
from signals_ahoy.asynchronous import AsynchronousListener
from tests.customapp.signals import async_note
from urls import custompatterns
import localsite
import logging
import time

log = logging.getLogger('tests.customapp.views')

def add_custom_urls(sender, patterns=(), **kwargs):
    log.debug('adding custom urls')
    patterns += custompatterns
    
def delay_and_note(sender, note="", **kwargs):
    log.debug('delaying before adding a note')
    time.sleep(5)
    from models import Note
    Note.objects.create(note=note)
    log.debug('added a note')
    
delayedNote = AsynchronousListener(delay_and_note)

def start_listening():
    signals.collect_urls.connect(add_custom_urls, sender=localsite)
    async_note.connect(delayedNote.listen, sender=None)
