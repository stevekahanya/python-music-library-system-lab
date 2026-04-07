## Music Library System
A robust Python-based music analytics tool designed for MusicTech Innovations. This system encapsulates song properties and behaviors while maintaining global, real-time insights into the entire library's collection.🚀 Key FeaturesThe system provides automated data analytics through Class Attributes and Class Methods, allowing users to:Track Growth: Automatically increments the total song count as new tracks are added.
Monitor Artists & Genres: Maintains unique, duplicate-free lists of every artist and genre in the library.
Deep Analytics: Provides a distribution breakdown, counting exactly how many songs belong to each specific genre and artist.Object-Oriented Design: Utilizes an encapsulated Song class for clean and modular data management.
## System Architecture
Object RelationshipsThe application uses a Many-to-One logic for its global tracking:Songs → Library Insights: Every individual Song instance reports its data back to the Song class level.
Data Integrity: Class methods ensure that global lists (artists/genres) remain unique and free of duplicates.Data ManagementInstance Attributes: name, artist, and genre.
Class Attributes:count: Integer tracking total instances.genres / artists: Lists of unique strings.genre_count / artists_count: Dictionaries mapping categories to their frequency (e.g., {"Pop": 12}).
## Implementation
DetailsEach new song instantiation triggers a sequence of class-level updates:MethodPurposeadd_song_to_countIncrements the global count.
add_to_genresAdds new, unique genres to the master list.
add_to_artistsAdds new, unique artists to the master list.
add_to_genre_countUpdates the frequency map for genres.
add_to_artists_countUpdates the frequency map for artists.
## Getting Started
PrerequisitesPython 3.8.13
pipenv for dependency management
SetupInstall Dependencies:Bashpipenv install
Enter Virtual Environment:Bashpipenv shell
Run Tests:Bashpytest -x lib/testing/song_test.py
##  Future EnhancementsPersistence: Integration with a database or JSON storage to save library data across sessions.Recommendations: Logic to suggest songs based on the highest-ranking genres in genre_count.GUI: A visual dashboard to display the library analytics
