# Lullaby Video Project - Quick Start Guide

## 🎵 Overview

This project generates a beautiful 90-second lullaby video with three classic baby songs:
1. **Twinkle, Twinkle, Little Star** (30 sec) - Twinkling stars animation
2. **Rock-a-bye Baby** (30 sec) - Rocking cradle animation  
3. **Hush Little Baby** (30 sec) - Soft flowing shapes animation

Each song includes:
- Auto-generated audio (using Google Text-to-Speech)
- Synchronized custom animation
- High-quality 1280x720 video at 30fps

---

## ⚡ Quick Start (5 minutes)

### For Windows Users:
```batch
generate_all.bat
```

### For Mac/Linux Users:
```bash
bash generate_all.sh
```

That's it! Your video will be created at `output/lullaby_video.mp4`

---

## 📋 Manual Installation (if automation doesn't work)

### Step 1: Install Python Dependencies
```bash
pip install -r requirements.txt
```

**Required packages:**
- moviepy (video creation)
- numpy (numerical computing)
- Pillow (image processing)
- scipy (audio generation)
- gtts (Google Text-to-Speech)
- pyttsx3 (offline TTS fallback)
- imageio + ffmpeg (video codec support)

### Step 2: Generate Audio Files
```bash
python scripts/generate_audio.py
```

This creates three MP3 files in the `audio/` folder:
- `twinkle_twinkle.mp3`
- `rock_a_bye.mp3`
- `hush_little_baby.mp3`

**Note:** This requires internet (uses Google TTS). If offline, it will generate synthetic audio instead.

### Step 3: Generate Video
```bash
python scripts/generate_video.py
```

The final video will be saved to: `output/lullaby_video.mp4`

---

## 📁 Project Structure

```
lullaby-video/
├── README.md                          # Project overview
├── QUICKSTART.md                      # Quick start guide
├── requirements.txt                   # Python dependencies
├── generate_all.sh                    # Mac/Linux automation
├── generate_all.bat                   # Windows automation
│
├── scripts/
│   ├── generate_audio.py              # Creates audio files
│   ├── generate_video.py              # Generates final video
│   ├── utils.py                       # Utility functions
│   └── animations/
│       ├── twinkle_stars.py           # Star animation
│       ├── rocking_motion.py          # Cradle animation
│       └── soft_lullaby.py            # Soft shapes animation
│
├── audio/                             # Audio files (auto-generated)
│   ├── twinkle_twinkle.mp3
│   ├── rock_a_bye.mp3
│   └── hush_little_baby.mp3
│
└── output/                            # Final video output
    └── lullaby_video.mp4              # Your generated video!
```

---

## 🎨 Customization

### Change Animation Duration
Edit `scripts/generate_video.py` and modify the duration parameter:
```python
duration=30  # Change to any value in seconds
```

### Change Video Resolution
In `scripts/generate_video.py`, modify:
```python
width, height = 1280, 720  # Change to 1920, 1080 for 4K, etc.
```

### Use Your Own Audio Files
1. Place your MP3 files in the `audio/` folder
2. Run: `python scripts/generate_video.py`
3. The script will use your files instead of generating new ones

### Adjust Animation Colors/Effects
Each animation file can be customized:
- `twinkle_stars.py` - Star colors, brightness, count
- `rocking_motion.py` - Cradle colors, rock speed
- `soft_lullaby.py` - Shape colors, animation speed

---

## 🔧 Troubleshooting

### Audio Generation Fails
**Problem:** `ModuleNotFoundError: No module named 'gtts'`

**Solution:** Install missing dependencies:
```bash
pip install gtts pyttsx3 scipy
```

### Video Generation is Slow
**Normal behavior** - First run takes time to render animations. Subsequent runs are cached.

**Tip:** Reduce resolution or duration for faster generation during testing.

### FFmpeg Error
**Solution:** Ensure ffmpeg is installed:
```bash
# On Mac (with Homebrew)
brew install ffmpeg

# On Windows (with Chocolatey)
choco install ffmpeg

# On Linux (Ubuntu/Debian)
sudo apt-get install ffmpeg
```

### No Audio in Video
This means audio files weren't found. Run:
```bash
python scripts/generate_audio.py
```

Then regenerate video:
```bash
python scripts/generate_video.py
```

---

## 📊 Video Specifications

| Property | Value |
|----------|-------|
| **Duration** | 90 seconds (3 × 30 sec) |
| **Resolution** | 1280 × 720 (HD) |
| **Frame Rate** | 30 FPS |
| **Codec** | H.264 (libx264) |
| **Audio Codec** | AAC |
| **File Format** | MP4 |
| **Approximate Size** | 15-25 MB |

---

## 💡 Tips

✅ **Best Experience:** Use the automated scripts (`generate_all.sh` or `generate_all.bat`)

✅ **First Time?** Don't worry if it takes a few minutes - rendering custom animations is normal

✅ **Reuse Audio:** Once generated, audio files are reused for faster video regeneration

✅ **Share Your Video:** The MP4 file can be played on any device and uploaded to social media

---

## 📝 License

MIT License - Feel free to use and modify for your projects!

---

## 🎬 Ready to Create Your Lullaby Video?

```bash
# Just run one of these:
generate_all.sh      # Mac/Linux
generate_all.bat     # Windows
python main.py       # Any platform
```

Happy creating! 🎵✨