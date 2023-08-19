from Node import node_song
'''this class will work like a playlist instance'''
class simulator:
    def __init__(self):
        self.first = None #this is for the first song added
        self.last = None #this is for the last song added
        self.probe = None #this will be for the song on playing
        self.length = 0 #this will count the number of songs

    def add(self,song):
        new = node_song(song)
        '''is added on the playlist on circular mode
        with the first and last element conected between them'''
        if self.length == 0:
            new.next = new
            new.previous = new
            self.first = new
            self.last = new
        elif self.length == 1:
            self.last = new
            self.last.next = self.first
            self.last.previous = self.first
            self.first.next = self.last
            self.first.previous = self.last
        else:
            current = self.first
            while current != self.last:
                current = current.previous
            current.previous = new
            new.next = current
            new.previous = self.first
            self.last = new
            self.first.next = self.last
        '''with this varable (self.probre) will be the first song added'''
        self.probe = self.first
        self.probe.previous = self.first.previous
        self.probe.next = self.first.next

        self.length += 1

    '''on this method the bool true in next will work for change the song after the first song added,
    if the bool is false then is the opposite dirrection and the second bool in delete will remove a song
    if that´s true or not if this´s false'''
    def playing(self,next=True,delete=False):
        '''this will preview if the playlist is empty'''
        if self.length == 0:
            raise Exception("the list is empty")
        
        play = self.probe #to play in the current song

        if next:
            self.probe = self.probe.previous
        else:
            self.probe = self.probe.next

        if delete:
            if play == self.first:
                self.first = self.first.previous
                self.last.previous = self.first
                self.first.next = self.last
            elif play == self.last:
                self.last = self.last.next
                self.first.next = self.last
                self.last.previous = self.first
            else:
                current = play.previous
                current2 = play.next
                current.next = current2
                current2.previous = current 

            self.length -= 1 #if deleted is true the counter would be less because a song was deleted

        return play.song
    '''on this method will show a list with total songs added and numbers of songs'''
    def play_list(self):
        if self.length == 0:
            raise Exception("the list is empty")
        lista = []
        current = self.last
        while current.next != self.last:
            lista.append(current.song)
            current = current.next
        lista.append(self.first.song)
        return f"the list is {lista} and amound of songs {self.length}"