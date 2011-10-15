from models import Article, ArticleCreator, ArticleEditor
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.sites.models import Site
from threaded_multihost.sites import by_host
from threaded_multihost.threadlocals import get_current_user, set_current_user
import unittest

__test__ = {'API_TESTS': """

>>> a = Article(text="Look at me any user")
>>> a.save()
>>> a.user is None
True

>>> u = User(username='user')
>>> u.save()
>>> a.user = u
>>> a.save()
>>> a.user is None
False

>>> a.user.pk == u.pk
True

>>> a.user
<User: user>

>>> u = User(username='creator')
>>> u.save()
>>> set_current_user(u)
>>> b = ArticleCreator(text="Look at me creator")
>>> b.save()
>>> b.user.pk == u.pk
True
>>> b.user
<User: creator>

>>> b = ArticleCreator.objects.get(pk=b.pk)
>>> b.user.pk == u.pk
True
>>> b.user
<User: creator>

>>> c = ArticleEditor(text="Look at me editor")
>>> c.save()
>>> c.user.pk == u.pk
True
>>> c.user
<User: creator>

>>> u = User(username='editor')
>>> u.save()
>>> set_current_user(u)
>>> c.text = "Changed from editor"
>>> c.save()
>>> c.user.pk == u.pk
True
>>> c.user
<User: editor>

>>> c = ArticleEditor.objects.get(pk=c.pk)
>>> c.user.pk == u.pk
True
>>> c.user
<User: editor>

# If the fields get an AnonymousUser from threadlocals, they should handle them
# appropriately and save NULL values to the database:
>>> anon = AnonymousUser()
>>> set_current_user(anon)

>>> anonb = ArticleCreator.objects.create(text="foo")
>>> anonb.user is None
True
>>> anonb = ArticleCreator.objects.get(pk=anonb.pk)
>>> anonb.user is None
True

>>> anonc = ArticleEditor.objects.create(text="bar")
>>> anonc.user is None
True
>>> anonc = ArticleEditor.objects.get(pk=anonc.pk)
>>> anonc.user is None
True
"""}


class ThreadedMultihostTest(unittest.TestCase):
    def test_by_host(self):
        "Tests typical usage"
        site2 = Site(domain='www.example.org', name='www.example.org')
        site2.save()
        self.assertEqual(by_host('example.com').domain, 'example.com')
        self.assertEqual(by_host('www.example.com').domain, 'example.com')
        self.assertEqual(by_host('example.org').domain, 'www.example.org')
        self.assertEqual(by_host('www.example.org').domain, 'www.example.org')

    def test_by_host_unknown(self):
        "Regression test for Satchmo #1276"
        # unknown string should get default domain by settings.SITE_ID
        # but never RuntimeError: "maximum recursion depth exceeded in cmp"
        self.assertEqual(by_host('nonsense.com').domain, 'example.com')
        self.assertEqual(by_host('www.nonsense.com').domain, 'example.com')
