from Node import node_song
class simulator:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    def add(self,song):
        new = node_song(song)
        if self.length == 0:
            self.first = new
            new.previous = self.first
            self.last = new
            self.last.next = self.first
        else:
            current = self.last
            while current.next != self.last:
                current = current.next
            current.next = new
            new.next = self.last
            self.last.previous = self.first
            self.first.next = self.last
        self.length += 1

    def playing(self,change=True):
        play = self.first
        if change is True:
            self.first = self.first.previous
        else:
            self.first = self.first.next
                        
        '''while True:
            self.first = self.first.previous
            
            if self.first.previous == play:
                break'''
        return play.song