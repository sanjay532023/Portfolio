from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,redirect,render
from .forms import PlaylistForm,TrackForm
from .models import Playlist,Track

def home(request):
    # HOME SHOWS PLAYLIST NAMES ONLY.
    playlists=Playlist.objects.all().order_by("name")
    return render(request,"player/home.html",{"playlists":playlists})

def playlist_detail(request,pk):
    playlist=get_object_or_404(Playlist.objects.prefetch_related("tracks"),pk=pk)
    return render(request,"player/playlist_detail.html",{"playlist":playlist})

def admin_login(request):
    if request.user.is_authenticated: return redirect("dashboard")
    error=None
    if request.method=="POST":
        user=authenticate(request,username=request.POST.get("username"),password=request.POST.get("password"))
        if user and user.is_staff:
            login(request,user); return redirect("dashboard")
        error="Invalid admin credentials."
    return render(request,"player/login.html",{"error":error})

@login_required
def dashboard(request):
    if not request.user.is_staff: return redirect("home")
    if request.method=="POST":
        if "create_playlist" in request.POST:
            form=PlaylistForm(request.POST)
            if form.is_valid(): form.save(); return redirect("dashboard")
        if "upload_track" in request.POST:
            form=TrackForm(request.POST,request.FILES)
            if form.is_valid(): form.save(); return redirect("dashboard")
    return render(request,"player/dashboard.html",{
        "playlists":Playlist.objects.prefetch_related("tracks").order_by("name"),
        "playlist_form":PlaylistForm(),"track_form":TrackForm()
    })

@login_required
def delete_playlist(request,pk):
    if request.user.is_staff: get_object_or_404(Playlist,pk=pk).delete()
    return redirect("dashboard")

@login_required
def delete_track(request,pk):
    if request.user.is_staff: get_object_or_404(Track,pk=pk).delete()
    return redirect("dashboard")

def admin_logout(request):
    logout(request); return redirect("home")
