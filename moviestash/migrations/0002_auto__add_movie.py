# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Movie'
        db.create_table(u'moviestash_movie', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('title', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('studio', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('director', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('producer', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
            ('genre', self.gf('django.db.models.fields.CharField')(default='', max_length=100)),
        ))
        db.send_create_signal(u'moviestash', ['Movie'])


    def backwards(self, orm):
        # Deleting model 'Movie'
        db.delete_table(u'moviestash_movie')


    models = {
        u'moviestash.movie': {
            'Meta': {'ordering': "('title',)", 'object_name': 'Movie'},
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'director': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'genre': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'producer': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'studio': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'default': "''", 'max_length': '100'})
        }
    }

    complete_apps = ['moviestash']