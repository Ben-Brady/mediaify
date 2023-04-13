import shutil

def assert_ffmpeg_installed():
    if not shutil.which("ffmpeg"):
        raise RuntimeError("ffmpeg is not installed")
    if not shutil.which("ffprobe"):
        raise RuntimeError("ffprobe is not installed")
