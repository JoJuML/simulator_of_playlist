import simulator as sim

if __name__=='__main__':
    playlist = sim.simulator()
    playlist.add('blackbird')
    playlist.add('stair way to haven')
    playlist.add('island in the sun')
    playlist.add('crimen')
    playlist.add('popular')
    print(playlist.play_list())
    print(playlist.playing())
    print(playlist.playing(False))
    print(playlist.playing(False))
    print(playlist.play_list())