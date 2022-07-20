from juke_box_songs import albums

SONG_LIST_INDEX = 3
SONG_TITLE_INDEX = 1

while True:
    print("Please Choose an album from the options below (invalid choice will exit):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print("{}: {}".format(index +1, title))

    choice = int(input())
    if 1 <= choice <= len(albums):
        songs_list = albums[choice -1][SONG_LIST_INDEX]
    else:
        break

    print('Chooce a Song:')
    for index, (track_number, song) in enumerate(songs_list):
        print('{}: {}'.format(index +1, song))

    song_choice = int(input())
    if 1 <= song_choice <= len(songs_list):
        title = songs_list[song_choice -1][SONG_TITLE_INDEX]
    else:
        break

    print('Now Playing {}'.format(title))
    print('=' * 40)
    print()
