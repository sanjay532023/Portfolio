from django import forms
from .models import Playlist,Track
class PlaylistForm(forms.ModelForm):
    class Meta:
        model=Playlist
        fields=["name"]
class TrackForm(forms.ModelForm):
    class Meta:
        model=Track
        fields=["title","playlist","audio"]
        widgets={"audio":forms.ClearableFileInput(attrs={"accept":".mp3,audio/mpeg"})}
