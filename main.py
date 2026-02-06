import random
from time import sleep
import os

global ads
adsallow = False

def p(j):
  print(j)

def wait(n: int):
  sleep(n)

def waitf(h: float):
  sleep(h)

def space(num: int):
  for x in range(0, num):
    p("")

def printext(w: str):
  with open(w, 'r', encoding='utf-8', errors='ignore') as f :
    print(f.read())

def ad():
  global adsallow
  if adsallow:
    space(15)
    ads = 0
    all = os.listdir("ads")
    texts = [f for f in all if f.endswith('.txt')]
    ads = len(texts)
    printext(f"ads/ad{random.randint(1, ads)}.txt")
    print("")
    p("---== AD BREAK INITIALIZED ==---")
    p("You may continue your program in 5")
    wait(1)
    p("You may continue your program in 4")
    wait(1)
    p("You may continue your program in 3")
    wait(1)
    p("You may continue your program in 2")
    wait(1)
    p("You may continue your program in 1")
    wait(1)
    p("")
    p("")
  

printext("icon.txt")

command = ""
mode = "home"

already = False

while command != "exit!":
  if random.randint(0, 3) == 3 and already:
    print("I don't feel like sending that right now.")
  else:
    match mode:
      case "home":
        already = True
        command = str(input("home>>> "))
        match command:
          case "help":
            printext("help.txt")
          case "info":
            printext('about.txt')
          case "calc":
            mode = "calc"
            p("calculator mode!")
          case "exit":
            ad()
            break
          case _:
            p("That command doesnt exist.")
      case "calc":
        p("""choose a mode:
  1: add
  2: subtrackt
  3: di vid e
  4: mmuullttiippllyy
  5: exit
  6: 67!!!
  7: 67!!!""")
        command = str(input("calculator>>> "))
        if command == "6" or command == "7":
          for x in range(random.randint(10, 100)): p("67!!"); waitf(0.01)
        elif command == "5": mode = "home"
        else:
          if command == "1" or command == "2" or command == "3" or command == "4":
            mode = "calc.inner"
            cmode = command
          else:
            p("stupid")
      case "calc.inner":
        one = float(input("give me the first number >>> "))
        two = float(input("give me the second number >>> "))
        modekey = ["undefined", "ADD", "SUBTRACT", "DIVIDE", "MULTIPLY"]
        if (random.randint(0, 1) == 1) or (one == two):
          p(f"Hmm. It seems that your current mode is {modekey[int(cmode)]}. Did you mean to do {modekey[random.randint(1, 4)]}?")
          sleep(2)
        else:
          match cmode:
            case "1":
              print(f"{one} PLUS {two} IS {one + two}")
            case "2":
              print(f"{one} MINUS {two} IS {one - two}")
            case "3":
              if two == 0:
                print("stupid")
              else:
                print(f"{one} DIVIDED BY {two} IS {one / two}")
            case "4":
              print(f"{one} TIMES {two} IS {one * two}")
            case _:
              print(f"{one}{two}")
          wait(4)
          mode = "home"
      case _:
        p("wtf")
  if random.randint(0, 4) == 1: ad()
  if random.randint(0, 2) == 1: p("Mooooo!")

print("thank you for using MING!")
wait(1)