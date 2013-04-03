from django.db import models


class Pesanan(models.Model):
	tanggal_pesan = models.DateTimeField('tanggal pemesanan', auto_now_add=True)
	email_pemesan = models.EmailField()
	nama_pemesan = models.CharField(max_length=141)
	selesai = models.BooleanField(default=False)
	pesanan = models.TextField()

