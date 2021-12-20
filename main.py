from web_displayer import Webdisplayer


def main():
    Webdisplayer.start('www.google.com')
    input()
    Webdisplayer.stop()

if __name__ == '__main__':
    main()
