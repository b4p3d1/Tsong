import pygame
import os
import random

# Initialize pygame
pygame.init()

# Get the folder location from the user
folder_location = input("Enter the folder location: ")

# Get a list of all the audio files in the folder
audio_files = [file for file in os.listdir(folder_location) if file.endswith('.mp3') or file.endswith('.wav') or file.endswith('.flac')]

if len(audio_files) == 0:
    print("No audio files found in the folder.")
    exit()

# Set the current track to the first track in the list
current_track = 0

# Shuffle the audio files
random.shuffle(audio_files)

# Load the audio file
pygame.mixer.music.load(os.path.join(folder_location, audio_files[current_track]))

# Play the audio file
pygame.mixer.music.play()

# Run the game loop
while True:
    # Check for user input
    command = input("Enter a command (play, pause, stop, next, previous, current, skip, volume up, volume down, shuffle): ")
    
    if command == 'play':
        # Play the audio file
        pygame.mixer.music.unpause()
    elif command == 'pause':
        # Pause the audio file
        pygame.mixer.music.pause()
    elif command == 'stop':
        # Stop the audio file and exit the game loop
        pygame.mixer.music.stop()
        break
    elif command == 'next':
        # Go to the next track
        current_track = (current_track + 1) % len(audio_files)
        pygame.mixer.music.load(os.path.join(folder_location, audio_files[current_track]))
        pygame.mixer.music.play()
    elif command == 'previous':
        # Go to the previous track
        current_track = (current_track - 1) % len(audio_files)
        pygame.mixer.music.load(os.path.join(folder_location, audio_files[current_track]))
        pygame.mixer.music.play()
    elif command == 'current':
        # Display the name of the current track
        print("Current track:", audio_files[current_track])
    elif command == 'skip':
        # Get the time to skip to from the user
        time = int(input("Enter the time to skip to (in milliseconds): "))
        pygame.mixer.music.set_pos(time)
    elif command == 'volume up':
        # Increase the volume by 0.1
        volume = pygame.mixer.music.get_volume()
        if volume < 1.0:
            pygame.mixer.music.set_volume(min(volume + 0.1, 1.0))
    elif command == 'volume down':
        # Decrease the volume by 0.1
        volume = pygame.mixer.music.get_volume()
        if volume > 0.0:
            pygame.mixer.music.set_volume(max(volume - 0.1, 0.0))
    elif command == 'shuffle':
        # Shuffle the audio files
        random.shuffle(audio_files)
        current_track = 0
        pygame.mixer.music.load(os.path.join(folder_location, audio_files[current_track]))
        pygame.mixer.music.play()
