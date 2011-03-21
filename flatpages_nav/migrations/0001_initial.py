# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding model 'FlatpagesNav'
        db.create_table('flatpages_nav_flatpagesnav', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('flatpage', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['flatpages.FlatPage'])),
            ('in_main_nav', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('in_footer_nav', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('order', self.gf('django.db.models.fields.IntegerField')()),
            ('active', self.gf('django.db.models.fields.BooleanField')(default=True)),
        ))
        db.send_create_signal('flatpages_nav', ['FlatpagesNav'])


    def backwards(self, orm):
        
        # Deleting model 'FlatpagesNav'
        db.delete_table('flatpages_nav_flatpagesnav')


    models = {
        'flatpages.flatpage': {
            'Meta': {'ordering': "('url',)", 'object_name': 'FlatPage', 'db_table': "'django_flatpage'"},
            'content': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'enable_comments': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'registration_required': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sites': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['sites.Site']", 'symmetrical': 'False'}),
            'template_name': ('django.db.models.fields.CharField', [], {'max_length': '70', 'blank': 'True'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '200'}),
            'url': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'})
        },
        'flatpages_nav.flatpagesnav': {
            'Meta': {'ordering': "('order',)", 'object_name': 'FlatpagesNav'},
            'active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'flatpage': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['flatpages.FlatPage']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'in_footer_nav': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'in_main_nav': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'order': ('django.db.models.fields.IntegerField', [], {})
        },
        'sites.site': {
            'Meta': {'ordering': "('domain',)", 'object_name': 'Site', 'db_table': "'django_site'"},
            'domain': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        }
    }

    complete_apps = ['flatpages_nav']
