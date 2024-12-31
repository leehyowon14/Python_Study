m = True

while m:

    def make_album(musician_name, album_title, number = None ):
        album = {'musician': musician_name, 'album_title': album_title }
        
        if number != '0':
            album['number'] = number

        return album
    print("\nIf you want to stop enter 'q' ")

    a = input("\nEnter the musician name: ")
    if a == 'q':
        break

    b = input("\nEnter the album title: ")
    if b == 'q':
        break

    d = input("\nEnter the number of songs: ")
    if d == 'q':
        break

    c = make_album(a,b,d)

    print('\n',c)