import simulator as sim

if __name__=='__main__':
    playlist = sim.simulator()
    playlist.add('blackbird')
    playlist.add('stair way to haven')
    playlist.add('island to the sun')
    playlist.add('crimen')
    print(playlist.playing())
    print(playlist.playing())
    print(playlist.playing())