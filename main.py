"""
Lullaby Video Generator - Main Entry Point
Creates a beautiful 90-second video with three lullabies and synchronized animations
"""

import os
import sys
from pathlib import Path

# Add scripts directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'scripts'))

from generate_audio import create_audio_files
from generate_video import generate_lullaby_video


def main():
    """Main entry point - coordinates audio and video generation"""
    print("\n" + "="*60)
    print("🎵 LULLABY VIDEO GENERATOR 🎵")
    print("="*60 + "\n")
    
    # Step 1: Create audio files
    print("STEP 1: Generating Audio Files")
    print("-" * 60)
    if not create_audio_files():
        print("\n⚠️  Audio generation failed. Continuing with silent video...")
    
    # Step 2: Create video
    print("\n\nSTEP 2: Generating Video")
    print("-" * 60)
    output_file = 'output/lullaby_video.mp4'
    generate_lullaby_video(output_file)
    
    # Final message
    print("\n" + "="*60)
    if os.path.exists(output_file):
        file_size = os.path.getsize(output_file) / (1024 * 1024)
        print("✅ SUCCESS!")
        print(f"📁 Video saved: {output_file}")
        print(f"📊 File size: {file_size:.1f} MB")
        print("🎬 Ready to watch!")
    else:
        print("❌ Video generation failed!")
    print("="*60 + "\n")


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⏹️  Generation cancelled by user")
        sys.exit(0)
    except Exception as e:
        print(f"\n\n❌ Error: {e}")
        import traceback
        traceback.print_exc()
        sys.exit(1)
