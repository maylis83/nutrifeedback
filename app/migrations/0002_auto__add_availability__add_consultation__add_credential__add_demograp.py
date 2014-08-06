# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Availability'
        db.create_table(u'app_availability', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('monday_early', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('monday_afternoon', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('monday_evening', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tuesday_early', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tuesday_afternoon', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('tuesday_evening', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('wednesday_early', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('wednesday_afternoon', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('wednesday_evening', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('thursday_early', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('thursday_afternoon', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('thursday_evening', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('friday_early', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('friday_afternoon', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('friday_evening', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('saturday_early', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('saturday_afternoon', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('saturday_evening', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sunday_early', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sunday_afternoon', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sunday_evening', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('nutritionist', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='nutritionist_availability', null=True, to=orm['app.Nutritionist'])),
        ))
        db.send_create_signal(u'app', ['Availability'])

        # Adding model 'Consultation'
        db.create_table(u'app_consultation', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='user_consultation', null=True, to=orm['account.User'])),
            ('nutritionist', self.gf('django.db.models.fields.related.ForeignKey')(blank=True, related_name='nutritionist_consultation', null=True, to=orm['app.Nutritionist'])),
            ('consultation', self.gf('django.db.models.fields.DateTimeField')()),
        ))
        db.send_create_signal(u'app', ['Consultation'])

        # Adding model 'Credential'
        db.create_table(u'app_credential', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.CharField')(max_length=1024)),
        ))
        db.send_create_signal(u'app', ['Credential'])

        # Adding M2M table for field nutritionist on 'Credential'
        m2m_table_name = db.shorten_name(u'app_credential_nutritionist')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('credential', models.ForeignKey(orm[u'app.credential'], null=False)),
            ('nutritionist', models.ForeignKey(orm[u'app.nutritionist'], null=False))
        ))
        db.create_unique(m2m_table_name, ['credential_id', 'nutritionist_id'])

        # Adding model 'Demographic'
        db.create_table(u'app_demographic', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'app', ['Demographic'])

        # Adding M2M table for field nutritionist on 'Demographic'
        m2m_table_name = db.shorten_name(u'app_demographic_nutritionist')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('demographic', models.ForeignKey(orm[u'app.demographic'], null=False)),
            ('nutritionist', models.ForeignKey(orm[u'app.nutritionist'], null=False))
        ))
        db.create_unique(m2m_table_name, ['demographic_id', 'nutritionist_id'])

        # Adding model 'Nutritionist'
        db.create_table(u'app_nutritionist', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('first_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('last_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('nutritionist_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('meeting_type', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('tag_phrase', self.gf('django.db.models.fields.CharField')(max_length=2048)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('state', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('zip', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('consultation_description', self.gf('django.db.models.fields.CharField')(max_length=4096)),
            ('skype_name', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'app', ['Nutritionist'])

        # Adding M2M table for field users on 'Nutritionist'
        m2m_table_name = db.shorten_name(u'app_nutritionist_users')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('nutritionist', models.ForeignKey(orm[u'app.nutritionist'], null=False)),
            ('user', models.ForeignKey(orm[u'account.user'], null=False))
        ))
        db.create_unique(m2m_table_name, ['nutritionist_id', 'user_id'])

        # Adding model 'Specialty'
        db.create_table(u'app_specialty', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('created', self.gf('model_utils.fields.AutoCreatedField')(default=datetime.datetime.now)),
            ('modified', self.gf('model_utils.fields.AutoLastModifiedField')(default=datetime.datetime.now)),
            ('type', self.gf('django.db.models.fields.CharField')(max_length=255)),
        ))
        db.send_create_signal(u'app', ['Specialty'])

        # Adding M2M table for field nutritionist on 'Specialty'
        m2m_table_name = db.shorten_name(u'app_specialty_nutritionist')
        db.create_table(m2m_table_name, (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('specialty', models.ForeignKey(orm[u'app.specialty'], null=False)),
            ('nutritionist', models.ForeignKey(orm[u'app.nutritionist'], null=False))
        ))
        db.create_unique(m2m_table_name, ['specialty_id', 'nutritionist_id'])


    def backwards(self, orm):
        # Deleting model 'Availability'
        db.delete_table(u'app_availability')

        # Deleting model 'Consultation'
        db.delete_table(u'app_consultation')

        # Deleting model 'Credential'
        db.delete_table(u'app_credential')

        # Removing M2M table for field nutritionist on 'Credential'
        db.delete_table(db.shorten_name(u'app_credential_nutritionist'))

        # Deleting model 'Demographic'
        db.delete_table(u'app_demographic')

        # Removing M2M table for field nutritionist on 'Demographic'
        db.delete_table(db.shorten_name(u'app_demographic_nutritionist'))

        # Deleting model 'Nutritionist'
        db.delete_table(u'app_nutritionist')

        # Removing M2M table for field users on 'Nutritionist'
        db.delete_table(db.shorten_name(u'app_nutritionist_users'))

        # Deleting model 'Specialty'
        db.delete_table(u'app_specialty')

        # Removing M2M table for field nutritionist on 'Specialty'
        db.delete_table(db.shorten_name(u'app_specialty_nutritionist'))


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
        u'app.nutritionist': {
            'Meta': {'object_name': 'Nutritionist'},
            'city': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'consultation_description': ('django.db.models.fields.CharField', [], {'max_length': '4096'}),
            'created': ('model_utils.fields.AutoCreatedField', [], {'default': 'datetime.datetime.now'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
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