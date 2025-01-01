import time

class FXPrintingEffect:
    def __init__(self, text: str = "Hello World"):
        global curtext
        curtext = text

    def printwitheffect(self, effect: int):
        """
        Print Set In Class Text With Effect
        :param effect: ID Effect (Examples: 0 = Normal, 1 = Cloned x2, 2 = Two Char Per 0.2 Sec, 3 = Before Printing Two Char)
        """
        if effect==0:
            for i in curtext:
                print(i, end="")
                time.sleep(0.25)
        elif effect==1:
            for i, c in enumerate(curtext):
                try:
                    print(c, end="")
                    time.sleep(0.2)
                    print(curtext[i], end="")
                    time.sleep(0.2)
                except IndexError:
                    break
        elif effect==2:
            for i in curtext:
                print(i, end="")
                time.sleep(0.2)
        elif effect==3:
            print(curtext[0:1:], end="")
            print(curtext[1:2:], end="")
            for i in curtext[2:]:
                print(i, end="")
                time.sleep(0.25)
    def unprintwitheffect(self, effect: int):
        """
        Unprint Set In Class Text With Effect
        :param effect: ID Effect (Examples: 0 = Normal, 1 = Cloned x2, 2 = Two Char Per 0.2 Sec)
        """
        if effect==0:
            for i in curtext:
                print("\b", end="")
                time.sleep(0.25)
        elif effect==1:
            for i, c in enumerate(curtext):
                try:
                    print("\b", end="")
                    time.sleep(0.2)
                    print("\b", end="")
                    time.sleep(0.2)
                except IndexError:
                    break
        elif effect==2:
            for i in curtext:
                print("\b", end="")
                time.sleep(0.2)

    curtext = "Hello World"