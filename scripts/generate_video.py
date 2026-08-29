"""Main script to generate the complete lullaby video"""

import os
from moviepy.editor import concatenate_videoclips, CompositeAudioFileClip, AudioFileClip
from animations.twinkle_stars import create_twinkle_stars_clip
from animations.rocking_motion import create_rocking_motion_clip
from animations.soft_lullaby import create_soft_lullaby_clip


def generate_lullaby_video(output_path='output/lullaby_video.mp4'):
    """Generate the complete lullaby video with all three songs"""
    
    # Create output directory if it doesn't exist
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    print("Generating lullaby video...")
    
    # Video settings
    width, height = 1280, 720
    fps = 30
    
    # Create animation clips
    print("Creating animation clips...")
    
    # Clip 1: Twinkle, Twinkle, Little Star (30 seconds)
    print("  - Twinkle Stars animation...")
    twinkle_clip = create_twinkle_stars_clip(duration=30, fps=fps, width=width, height=height)
    
    # Clip 2: Rock-a-bye Baby (30 seconds)
    print("  - Rocking Motion animation...")
    rock_clip = create_rocking_motion_clip(duration=30, fps=fps, width=width, height=height)
    
    # Clip 3: Hush Little Baby (30 seconds)
    print("  - Soft Lullaby animation...")
    hush_clip = create_soft_lullaby_clip(duration=30, fps=fps, width=width, height=height)
    
    # Concatenate video clips
    print("Concatenating clips...")
    final_clip = concatenate_videoclips([twinkle_clip, rock_clip, hush_clip])
    
    # Check if audio files exist
    audio_path = 'audio'
    twinkle_audio = os.path.join(audio_path, 'twinkle_twinkle.mp3')
    rock_audio = os.path.join(audio_path, 'rock_a_bye.mp3')
    hush_audio = os.path.join(audio_path, 'hush_little_baby.mp3')
    
    # Add audio if files exist
    if os.path.exists(twinkle_audio) and os.path.exists(rock_audio) and os.path.exists(hush_audio):
        print("Adding audio tracks...")
        try:
            twinkle_sound = AudioFileClip(twinkle_audio)
            rock_sound = AudioFileClip(rock_audio)
            hush_sound = AudioFileClip(hush_audio)
            
            # Set audio to respective clips
            twinkle_clip = twinkle_clip.set_audio(twinkle_sound)
            rock_clip = rock_clip.set_audio(rock_sound)
            hush_clip = hush_clip.set_audio(hush_sound)
            
            # Reconcat with audio
            final_clip = concatenate_videoclips([twinkle_clip, rock_clip, hush_clip])
        except Exception as e:
            print(f"Warning: Could not load audio files: {e}")
            print("Continuing with video only...")
    else:
        print(f"Note: Audio files not found in {audio_path}/")
        print("Generate the video with animations only.")
        print("Place audio files in the audio/ directory and regenerate for full experience.")
    
    # Write to file
    print(f"Writing video to {output_path}...")
    final_clip.write_videofile(output_path, fps=fps, codec='libx264', audio_codec='aac', verbose=False, logger=None)
    
    print(f"✓ Video generated successfully: {output_path}")
    print(f"Duration: 90 seconds (3 songs × 30 seconds each)")


if __name__ == '__main__':
    generate_lullaby_video()
