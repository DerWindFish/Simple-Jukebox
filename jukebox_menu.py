from xml.etree.ElementTree import TreeBuilder
from juke_box_songs import albums

while True:
    print("Please Choose from the options below (invalid choice will exit):")
    for index, (title, artist, year, songs) in enumerate(albums):
        print('{}: {}'.format(index +1, title))

    break
