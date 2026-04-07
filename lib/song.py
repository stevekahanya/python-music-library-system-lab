class Song:
    # --- Class Attributes ---
    # Tracks total number of song instances created
    count = 0
    # Stores unique names of all genres
    genres = []
    # Stores unique names of all artists
    artists = []
    # Maps genre names to the number of songs in that genre
    genre_count = {}
    # Maps artist names to the number of songs they have
    artist_count = {}

    def __init__(self, name, artist, genre):
        # Instance attributes
        self.name = name
        self.artist = artist
        self.genre = genre
        
        # Trigger class methods to update global insights upon creation
        Song.add_song_to_count()
        Song.add_to_genres(genre)
        Song.add_to_artists(artist)
        Song.add_to_genre_count(genre)
        Song.add_to_artists_count(artist)

    # --- Class Methods ---
    
    @classmethod
    def add_song_to_count(cls):
        # Increments total song count
        cls.count += 1

    @classmethod
    def add_to_genres(cls, genre):
        # Adds genre if it's not already in the list to maintain uniqueness
        if genre not in cls.genres:
            cls.genres.append(genre)

    @classmethod
    def add_to_artists(cls, artist):
        # Adds artist if not already in the list to avoid duplicates
        if artist not in cls.artists:
            cls.artists.append(artist)

    @classmethod
    def add_to_genre_count(cls, genre):
        # Increments the genre key, or initializes it to 1 if new
        if genre in cls.genre_count:
            cls.genre_count[genre] += 1
        else:
            cls.genre_count[genre] = 1

    @classmethod
    def add_to_artists_count(cls, artist):
        # Increments the artist key, or initializes it to 1 if new
        if artist in cls.artist_count:
            cls.artist_count[artist] += 1
        else:
            cls.artist_count[artist] = 1