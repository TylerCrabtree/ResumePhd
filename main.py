import colorama




class Play:
    def __init__(self):
        colorama.init(autoreset=True)

    def color_magenta(self):
        magenta = colorama.Fore.MAGENTA
        return (magenta)

    def playing_around(self):
        print('hi')


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    obj = Play()
    obj.p()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
