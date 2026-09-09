from django.db import migrations,models
import django.db.models.deletion
class Migration(migrations.Migration):
    initial=True
    dependencies=[]
    operations=[
        migrations.CreateModel(name="Playlist",fields=[
            ("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),
            ("name",models.CharField(max_length=120,unique=True)),
            ("created_at",models.DateTimeField(auto_now_add=True)),
        ]),
        migrations.CreateModel(name="Track",fields=[
            ("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),
            ("title",models.CharField(max_length=200)),
            ("audio",models.FileField(upload_to="tracks/")),
            ("uploaded_at",models.DateTimeField(auto_now_add=True)),
            ("playlist",models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name="tracks",to="player.playlist")),
        ]),
    ]
