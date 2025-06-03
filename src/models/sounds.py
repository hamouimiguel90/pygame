from pygame import mixer


class Sounds:
    def __init__(self):
        pass

    def set_background_music(self, music_path):
        mixer.music.load(music_path)
        mixer.music.set_volume(0.3) # volumen
        mixer.music.play(-1) # -1 its for repeat..

    def bullet_sound(self, bullet_path):
        sound = mixer.Sound(bullet_path)
        sound.play()

    def collision_sound(self, collision_path):
        sound = mixer.Sound(collision_path)
        sound.play()
