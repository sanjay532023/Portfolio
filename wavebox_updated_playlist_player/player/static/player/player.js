document.addEventListener("DOMContentLoaded", () => {
    const audio = document.getElementById("audio");
    if (!audio) return;
    const tracks = [...document.querySelectorAll(".track")],
        play = document.getElementById("play"),
        stop = document.getElementById("stop"),
        prev = document.getElementById("prev"),
        next = document.getElementById("next"),
        back = document.getElementById("back"),
        seek = document.getElementById("seek"),
        volume = document.getElementById("volume"),
        title = document.getElementById("nowTitle"),
        cur = document.getElementById("current"),
        dur = document.getElementById("duration");
    let index = -1,
        seeking = false;
    const fmt = s => !Number.isFinite(s) || s < 0 ? "0:00" : `${Math.floor(s/60)}:${String(Math.floor(s%60)).padStart(2,"0")}`;

    function progress() {
        if (seeking) return;
        if (!Number.isFinite(audio.duration) || audio.duration <= 0) {
            seek.value = 0;
            cur.textContent = "0:00";
            return
        }
        seek.value = Math.min(100, Math.max(0, audio.currentTime / audio.duration * 100));
        cur.textContent = fmt(audio.currentTime)
    }

    function load(i, auto = true) {
        if (!tracks.length) return;
        index = (i + tracks.length) % tracks.length;
        tracks.forEach(t => t.classList.remove("active"));
        const t = tracks[index];
        t.classList.add("active");
        audio.src = t.dataset.src;
        audio.load();
        title.textContent = t.dataset.title || "Unknown Track";
        seek.value = 0;
        cur.textContent = "0:00";
        dur.textContent = "0:00";
        if (auto) audio.play().catch(() => {})
    }
    tracks.forEach((t, i) => t.addEventListener("click", () => load(i)));
    play?.addEventListener("click", () => {
        if (!audio.src) load(0);
        else audio.paused ? audio.play().catch(() => {}) : audio.pause()
    });
    stop?.addEventListener("click", () => {
        audio.pause();
        audio.currentTime = 0;
        seek.value = 0;
        cur.textContent = "0:00"
    });
    prev?.addEventListener("click", () => {
        if (audio.currentTime > 3) {
            audio.currentTime = 0;
            progress()
        } else load(index - 1)
    });
    next?.addEventListener("click", () => load(index + 1));
    back?.addEventListener("click", () => {
        audio.currentTime = Math.max(0, audio.currentTime - 10);
        progress()
    });
    seek?.addEventListener("pointerdown", () => seeking = true);
    seek?.addEventListener("input", () => {
        if (Number.isFinite(audio.duration) && audio.duration > 0) cur.textContent = fmt(Number(seek.value) / 100 * audio.duration)
    });

    function finishSeek() {
        if (!seeking) return;
        if (Number.isFinite(audio.duration) && audio.duration > 0) audio.currentTime = Number(seek.value) / 100 * audio.duration;
        seeking = false;
        progress()
    }
    seek?.addEventListener("change", finishSeek);
    window.addEventListener("pointerup", finishSeek);
    audio.addEventListener("timeupdate", progress);
    audio.addEventListener("loadedmetadata", () => {
        dur.textContent = fmt(audio.duration);
        progress()
    });
    audio.addEventListener("durationchange", () => dur.textContent = fmt(audio.duration));
    audio.addEventListener("play", () => play.textContent = "Ⅱ");
    audio.addEventListener("pause", () => play.textContent = "▶");
    audio.addEventListener("ended", () => load(index + 1));
    volume?.addEventListener("input", () => audio.volume = Number(volume.value));
    audio.volume = .8
})