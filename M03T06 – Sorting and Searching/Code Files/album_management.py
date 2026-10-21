# M03T06: Sorting and Searching - Album management system
# This program demonstrates sorting and searching operations on Album objects

class Album:
    """Class representing a music album."""

    def __init__(self, album_name, album_artist, number_of_songs):
        """Initialize an Album object."""
        self.album_name = album_name
        self.number_of_songs = number_of_songs
        self.album_artist = album_artist

    def __str__(self):
        """Return string representation of Album."""
        return f"({self.album_name}, {self.album_artist}, {self.number_of_songs})"


# 3. Create albums1 list with 5 Album objects
albums1 = [
    Album("Thriller", "Michael Jackson", 9),
    Album("Back in Black", "AC/DC", 10),
    Album("The Bodyguard", "Whitney Houston", 13),
    Album("Rumours", "Fleetwood Mac", 11),
    Album("Abbey Road", "The Beatles", 17)
]

print("albums1:")
for album in albums1:
    print(album)

# 4. Sort by number_of_songs
albums1.sort(key=lambda x: x.number_of_songs)
print("\nalbums1 sorted by number_of_songs:")
for album in albums1:
    print(album)

# 5. Swap elements at index 0 and 1
albums1[0], albums1[1] = albums1[1], albums1[0]
print("\nalbums1 after swapping positions 1 and 2:")
for album in albums1:
    print(album)

# 6. Create albums2 list
albums2 = []

# 7. Add 5 Album objects to albums2
albums2.append(Album("21", "Adele", 11))
albums2.append(Album("Born in the U.S.A.", "Bruce Springsteen", 12))
albums2.append(Album("Purple Rain", "Prince", 9))
albums2.append(Album("Appetite for Destruction", "Guns N' Roses", 12))
albums2.append(Album("The Wall", "Pink Floyd", 26))

print("\nalbums2:")
for album in albums2:
    print(album)

# 8. Copy all albums from albums1 into albums2
albums2.extend(albums1)

# 9. Add two more albums
albums2.append(Album("Dark Side of the Moon", "Pink Floyd", 9))
albums2.append(Album("Oops!... I Did It Again", "Britney Spears", 16))

# 10. Sort albums2 alphabetically by album name
albums2.sort(key=lambda x: x.album_name)
print("\nalbums2 sorted alphabetically by album name:")
for album in albums2:
    print(album)

# 11. Search for "Dark Side of the Moon"
for i in range(len(albums2)):
    if albums2[i].album_name == "Dark Side of the Moon":
        print(f"\nIndex of 'Dark Side of the Moon': {i}")
        break
