# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Pesanan'
        db.create_table(u'pemesanan_pesanan', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('tanggal_pesan', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('email_pemesan', self.gf('django.db.models.fields.EmailField')(max_length=75)),
            ('nama_pemesan', self.gf('django.db.models.fields.CharField')(max_length=141)),
            ('selesai', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('pesanan', self.gf('django.db.models.fields.TextField')()),
        ))
        db.send_create_signal(u'pemesanan', ['Pesanan'])


    def backwards(self, orm):
        # Deleting model 'Pesanan'
        db.delete_table(u'pemesanan_pesanan')


    models = {
        u'pemesanan.pesanan': {
            'Meta': {'object_name': 'Pesanan'},
            'email_pemesan': ('django.db.models.fields.EmailField', [], {'max_length': '75'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nama_pemesan': ('django.db.models.fields.CharField', [], {'max_length': '141'}),
            'pesanan': ('django.db.models.fields.TextField', [], {}),
            'selesai': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'tanggal_pesan': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['pemesanan']