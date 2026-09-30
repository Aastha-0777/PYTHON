# Playlist Manager: 
# Start with a list of 5 songs. 
# Add a song, 
# remove a song, 
# and print the 
# playlist sorted A-Z.


# global list playlist

# adsong
# removesong
# print songs
# sort


# while True
#     match case

songs = ["Blinding Lights", "Levitating", "Watermelon Sugar", "Stay", "Good 4 U"]

def addSong() :

    newSong = input('Enter New Song You want to Add : ')
    songs.append(newSong)
    print(f'Song {newSong} added Successfully...')

def removeSong() :

    song = input('Enter the Song You want to Remove : ')

    for i in range(0, len(songs)) : 
        if song == songs[i] : 
            songs.remove(i)
            print(f'Song {song} Removed Successfully...')


def printSong() : 

    for i in songs : 

        print(i)

def sortSong() : 

    songs.sort()
    print('Songs Sorted Successfully....')


while True :

    print('1. Add Song')
    print('2. Remove Song')
    print('3. Print Song')
    print('4. Sort Song')
    print('5. Exit')
    choice = int(input('Enter From Above Choices : '))

    match (choice) :

        case 1 : 
            addSong()

        case 2 : 
            removeSong()

        case 3 : 
            printSong()

        case 4 :
            sortSong()

        case 5 :
            break

        case _ : 
            print('Invalid Choice...')