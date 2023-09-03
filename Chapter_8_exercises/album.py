
import pandas as pd

def make_album(artist_name, album_title, no_songs=None):
    song_artist = {
        'name' : artist_name,
        'album title' : album_title,
        'Number of Songs' : no_songs
    }

    return song_artist

list_of_artist = []

while True:
    name = input("Press q to quit.. \nArtist Name: ")
    title = input("Algum title: ")
    number_of_songs = input("Number of songs: ")

    #conditional
    if name == 'q' or title == 'q' or number_of_songs == 'q':
        break

    display_artist = make_album(
        album_title=title,
        artist_name=name,
        no_songs= number_of_songs
    )

    list_of_artist.append(display_artist)

df_data = pd.DataFrame(list_of_artist)

print(df_data)