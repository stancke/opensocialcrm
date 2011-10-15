from django.db import models
from threaded_multihost import fields


class Article(models.Model):
	user = fields.UserField(related_name='articles')
	text = models.TextField()

	def  __unicode__(self):
		return self.text


class ArticleCreator(models.Model):
	user = fields.CreatorField(related_name='created_articles')
	text = models.TextField()

	def  __unicode__(self):
		return self.text


class ArticleEditor(models.Model):
	user = fields.EditorField(related_name='edited_articles')
	text = models.TextField()

	def  __unicode__(self):
		return self.text

