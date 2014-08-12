# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Nutritionist.address'
        db.add_column(u'app_nutritionist', 'address',
                      self.gf('django.db.models.fields.CharField')(default=' ', max_length=255),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Nutritionist.address'
        db.delete_column(u'app_nutritionist', 'address')


    models = {
        u'account.user': {
            'Meta': {'object_name': 'User'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'app.availability': {
            'Meta': {'object_name': 'Availability'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'friday_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'friday_early': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'friday_evening': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'monday_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'monday_early': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'monday_evening': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'nutritionist': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'nutritionist_availability'", 'null': 'True', 'to': u"orm['app.Nutritionist']"}),
            'saturday_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'saturday_early': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'saturday_evening': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sunday_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sunday_early': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'sunday_evening': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thursday_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thursday_early': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'thursday_evening': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tuesday_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tuesday_early': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tuesday_evening': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wednesday_afternoon': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wednesday_early': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wednesday_evening': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'app.consultation': {
            'Meta': {'object_name': 'Consultation'},
            'consultation': ('django.db.models.fields.DateTimeField', [], {}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'nutritionist': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'nutritionist_consultation'", 'null': 'True', 'to': u"orm['app.Nutritionist']"}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'blank': 'True', 'related_name': "'user_consultation'", 'null': 'True', 'to': u"orm['account.User']"})
        },
        u'app.credential': {
            'Meta': {'object_name': 'Credential'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'description': ('django.db.models.fields.CharField', [], {'max_length': '1024'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'nutritionist': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'nutritionist_credential'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['app.Nutritionist']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'app.demographic': {
            'Meta': {'object_name': 'Demographic'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'nutritionist': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'nutritionist_demographic'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['app.Nutritionist']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'app.healthsurvey': {
            'Meta': {'object_name': 'HealthSurvey'},
            'anything_else': ('django.db.models.fields.CharField', [], {'max_length': '4096', 'null': 'True', 'blank': 'True'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'dietary_restrictions': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'dob': ('django.db.models.fields.DateField', [], {}),
            'exercise_freq': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'gender': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            'health_goals': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '10'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'weight': ('django.db.models.fields.IntegerField', [], {})
        },
        u'app.nutritionist': {
            'Meta': {'object_name': 'Nutritionist'},
            'address': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'consultation_description': ('django.db.models.fields.CharField', [], {'max_length': '4096'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'headshot': ('django.db.models.fields.files.ImageField', [], {'default': "'/nutritionist_headshots/none.jpg'", 'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'meeting_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'nutritionist_type': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'skype_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'state': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'tag_phrase': ('django.db.models.fields.CharField', [], {'max_length': '2048'}),
            'users': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'nutritionist_users'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['account.User']"}),
            'zip': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'app.specialty': {
            'Meta': {'object_name': 'Specialty'},
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modified': ('model_utils.fields.AutoLastModifiedField', [], {'default': 'datetime.datetime.now'}),
            'nutritionist': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'nutritionist_specialty'", 'null': 'True', 'symmetrical': 'False', 'to': u"orm['app.Nutritionist']"}),
            'type': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['app']