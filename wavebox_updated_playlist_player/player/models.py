from django.db import models
class Playlist(models.Model):
    name=models.CharField(max_length=120,unique=True)
    created_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.name
class Track(models.Model):
    title=models.CharField(max_length=200)
    audio=models.FileField(upload_to="tracks/")
    playlist=models.ForeignKey(Playlist,related_name="tracks",on_delete=models.CASCADE)
    uploaded_at=models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title
