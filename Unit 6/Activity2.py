import abc
import random


class Media(abc.ABC):
    def __init__(self, name, stars):
        self.name = name
        self.stars = stars

    @abc.abstractmethod
    def play(self):
        pass


class Movie(Media):
    def __init__(self, name, stars, director, duration):
        super().__init__(name, stars)
        self.duration = duration
        self.director = director

    def play(self):
        print(f"Playing movie {self.name}")

    def __str__(self):
        return f"{self.name} {self.stars} {self.director} {self.duration}"


class Song(Media):
    def __init__(self, name, stars, artist, album):
        super().__init__(name, stars)
        self.artist = artist
        self.album = album

    def play(self):
        print(f"Playing song {self.name}")

    def __str__(self):
        return f"{self.name} {self.stars} {self.artist} {self.album}"


media_list = []
Movie1 = Movie("The Shawshank Redemption", 5, "Frank Darabont", 142)
Movie2 = Movie("The Godfather", 5, "Francis Ford Coppola", 175)
Movie3 = Movie("The Dark Knight", 5, "Christopher Nolan", 152)
Song1 = Song("Bohemian Rhapsody", 5, "Queen", "A Night at the Opera")
Song2 = Song("Stairway to Heaven", 5, "Led Zeppelin", "Led Zeppelin IV")
Song3 = Song("Imagine", 5, "John Lennon", "Imagine")
media_list.append(Movie1)
media_list.append(Movie2)
media_list.append(Movie3)
media_list.append(Song1)
media_list.append(Song2)
media_list.append(Song3)

random_index = random.randint(0, len(media_list) - 1)
random_media = media_list[random_index]
random_media.play()
