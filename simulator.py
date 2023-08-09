from Node import node_song
class simulator():
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
    
    def add(self,song):
        new = node_song(song)
        if self.length == 0:
            self.first = new
            new.next = self.first
            self.last.previous = self.first
            self.last = new
        else:
            current = self.last
            while current.next != self.last:
                current = current.next 
            current.next = new
            new.next = self.last
        self.length += 1

    def playing(self,change=True):
        if change is True:
            pass
        play = self.first
        while True:
            self.first = self.first.previous
            
            
            if self.first == play:
                break
        return play