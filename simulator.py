from Node import node_song
class simulator:
    def __init__(self):
        self.first = None
        self.last = None
        self.probe = None
        self.length = 0
    
    def add(self,song):
        new = node_song(song)
        if self.length == 0:
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

        self.length += 1

    def playing(self,change=True):
        
        play = self.probe
        if change is True:
            self.probe = self.probe.previous
        else:
            self.probe = self.probe.next
                        
        '''while True:
            self.first = self.first.previous
            if self.first.previous == play:
                break'''
        return play.song
    
    def play_list(self):
        lista = []
        current = self.last
        while current.next != self.last:
            lista.append(current.song)
            current = current.next
        lista.append(self.first.song)
        return lista