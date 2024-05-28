import time

class bnsd {
    pass
}

kc = 'something'

dark_green = bnsd.BNColor(0, 128, 0)
light_green = bnsd.BNColor(0, 255, 0)

options = [
        ("Start", 20, 40)
        ("Ranking", 20, 60)
        ("Wrong", 20, 80)
    ]

def display_opt(highlight):
        bnsd.clear(bnsd.BNColor(0, 0, 0))
        for index, (text, x, y) in enumerate(options):
            color = light_green if index == highlight else dark_green
            bnsd.showText(text, x, y, color)
        bnsd.show()

def update_highlight(highlight, kc):
        if kc == 3:
            highlight = (highlight + 1) % len(options)
        elif kc == 1:
            highlight = (highlight - 1) % len(options)
        return highlight

def start(highlight = 1):
    while True:
        global kc
        kc = (kc + 1) % 5

        highlight = update_highlight(highlight, kc)
        display_opt(highlight)

        time.sleep(0.1)


start()