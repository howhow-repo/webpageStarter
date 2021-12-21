from web_displayer import Webdisplayer


def main():
    Webdisplayer.start('https://www.cwb.gov.tw/V8/C/')
    input()
    Webdisplayer.stop()


if __name__ == '__main__':
    main()
