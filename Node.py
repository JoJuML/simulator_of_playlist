'''this is a doble way of node for playlist'''
class node_song:
    def __init__(self,song,previous=None,next=None):
        self.song = song
        self.previous = previous
        self.next = next