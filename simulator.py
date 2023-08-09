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
            self.last = new
        elif self.length == 1:
            new.next = self.last
            self.last = new
        else:
            new.previous = self.last
            self.last.next = new
            self.last = new
        self.length += 1

    def playing(self):
        play = self.first
        while True:
            self.first = self.first.next
            if self.first == play:
                break
        return play