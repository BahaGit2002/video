from django.db import models


class Record(models.Model):
    title = models.CharField(max_length=150)
    video_record = models.FileField(upload_to='videorecord')

    class Meta:
        verbose_name = 'Видеозапись'
        verbose_name_plural = 'Видеозаписи'

    def __str__(self):
        return self.title
