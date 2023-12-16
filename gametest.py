import pygame

pygame.init()

# Initialize the mixer
pygame.mixer.init()

# Load music file
pygame.mixer.music.load('.\\music\\beethoven-moonlight-sonata-1-movement-op-27-nr-2-180627.mp3')  # Replace 'your_music_file.mp3' with your music file path

# Play the music (-1 means loop indefinitely)
pygame.mixer.music.play(-1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

# Stop the music when the game ends
pygame.mixer.music.stop()

pygame.quit()
