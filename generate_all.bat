@echo off
REM Quick setup and video generation script for Windows

echo.
echo 🎵 Lullaby Video Generator
echo ==========================
echo.

REM Check Python version
echo Checking Python installation...
python --version

REM Install dependencies
echo.
echo Installing dependencies...
pip install -r requirements.txt

REM Generate audio files
echo.
echo Generating audio files...
python scripts/generate_audio.py

REM Generate video
echo.
echo Generating video...
python scripts/generate_video.py

echo.
echo ✓ Done! Your video is ready at: output/lullaby_video.mp4
pause
