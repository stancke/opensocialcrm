from django.db.models import ForeignKey
from django.contrib.auth.models import User

import threadlocals


class UserField(ForeignKey):
    """ UserField

    By defaults, foreign key to User; null=True, blank=True
    """

    def __init__(self, **kwargs):
        kwargs.setdefault('to', User)
        kwargs.setdefault('null', True)
        kwargs.setdefault('blank', True)
        ForeignKey.__init__(self, **kwargs)


class CreatorField(UserField):
    """ CreatorField

    By default, sets editable=False, default=threadlocals.get_current_user
    """

    def get_current_user(self):
        user = threadlocals.get_current_user()
        if user and not user.is_authenticated():
            user = None
        return user

    def __init__(self, **kwargs):
        kwargs.setdefault('editable', False)
        kwargs.setdefault('default', self.get_current_user)
        UserField.__init__(self, **kwargs)


class EditorField(CreatorField):
    """ EditorField

    By default, sets editable=False, default=threadlocals.get_current_user

    Sets value to get_current_user() on each save of the model.
    """

    def __init__(self, **kwargs):
        super(CreatorField, self).__init__(**kwargs)

    def pre_save(self, model_instance, add):
        value = self.get_current_user()
        setattr(model_instance, self.name, value)
        if value:
            value = value.pk
        setattr(model_instance, self.attname, value)
        return value

try:
    from south.modelsinspector import add_introspection_rules
except ImportError:
    add_introspection_rules = False

if add_introspection_rules:
    add_introspection_rules([], [r"^threaded_multihost\.fields\.(User|Creator|Editor)Field"])
