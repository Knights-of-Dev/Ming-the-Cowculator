import random
from time import sleep
import os
from broadcast import emitter
import re

global ads
adsallow = True

def intify(b):
  if type(b) == float or type(b) == int: return(int(b))
  elif type(b) == str: 
    if re.fullmatch(r"^[1234567890]+$", b): return(int(b))
    elif re.fullmatch(r"^[1234567890.]+$", b): return(int(float(b)))
  else: return 0

def boolify(a):
  if a == "True" or a == "true" or a == "1" or a == True or a == 1 or a == 1.0: return True
  else: return False

def floatify(s):
  if type(s) == int:
    return(float(s))
  elif type(s) == bool:
    if s: return 1.0
    else: return 0.0
  elif type(s) == str:
    return intify(s)
  else: return 0.0

def p(j):
  print(j)

def wait(n: int):
  sleep(n)

def waitf(h: float):
  sleep(h)

def space(num: int):
  for x in range(0, num): p("")

def printext(w: str):
  with open(w, 'r', encoding='utf-8', errors='ignore') as f :
    print(f.read())

def scanfor(folder: str, ext: str, mode="c"):
  all = os.listdir(folder)
  j = [f for f in all if f.endswith(ext)]
  match mode:
    case "c": return len(j)
    case "l": return j
    case _: return 0

def ad():
  global adsallow
  if adsallow:
    space(15)
    ads = 0
    ads = scanfor("ads", ".txt")
    printext(f"ads/ad{random.randint(1, ads)}.txt")
    print("")
    p("---== AD BREAK INITIALIZED ==---")
    p("You may continue your program in 5"); wait(1)
    p("You may continue your program in 4"); wait(1)
    p("You may continue your program in 3"); wait(1)
    p("You may continue your program in 2"); wait(1)
    p("You may continue your program in 1"); wait(1)
    p("")
    p("")
  

if __name__ == "__main__":
  printext("icon.txt")

  command = ""
  mode = "home"

  already = False

  recog = False

  while command != "exit!":
    if random.randint(0, 3) == 3 and already:
      print("I don't feel like sending that right now.")
    else:
      match mode:
        case "home":
          already = True
          command = str(input("home>>> "))
          if random.randint(0, 4) == 1: ad()
          recog = False
          emitter.broadcast("sent.home", command)
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
              waitf(0.5)
              if not recog: p("That command doesnt exist.")
        case "calc":
          p("""choose a mode:
  1: add
  2: subtrackt
  3: di vid e
  4: mmuullttiippllyy
  5: exit
  6: 67!!!
  7: 67!!!
  8: square rooooot""")
          command = str(input("calculator>>> "))
          if random.randint(0, 4) == 1: ad()
          if command == "6" or command == "7":
            for x in range(random.randint(10, 100)): p("67!!"); waitf(0.01)
          elif command == "5": mode = "home"
          else:
            if command == "1" or command == "2" or command == "3" or command == "4" or command == "8":
              mode = "calc.inner"
              cmode = command
            else:
              p("stupid")
        case "calc.inner":
          one = floatify(input("give me the first number >>> "))
          two = floatify(input("give me the second number >>> "))
          reccommend = {
            "1": [2, 3, 4],
            "2": [1, 4, 8],
            "3": [8],
            "4": [3, 1, 4, 8],
            "8": [3, 1, 4, 6]
          }
          modekey = ["undefined", "ADD", "SUBTRACT", "DIVIDE", "MULTIPLY", "undefined", "SIXSEVENIFY", "SIXSEVENIFY", "SQUAREROOT"]
          if (random.randint(0, 1) == 1) or (one == two):
            p(f"Hmm. It seems that your current mode is {modekey[int(cmode)]}. Did you mean to do {modekey[random.choice(reccommend[cmode])]}?")
            sleep(2)
          else:
            if random.randint(0, 4) == 1: ad()
            match cmode:
              case "1":
                print(f"{one} PLUS {two} IS {one + two}")
              case "2":
                print(f"{one} MINUS {two} IS {one - two}")
              case "3":
                if two == 0:
                  p("stupid")
                else:
                  print(f"{one} DIVIDED BY {two} IS {one / two}")
              case "4":
                print(f"{one} TIMES {two} IS {one * two}")
              case "8":
                if one < 0 or two < 0:
                  print("stupid")
                else:
                  print(f"SQUARE ROOT OF {one} IS {one ** 0.5}")
                  print(f"SQUARE ROOT OF {two} IS {two ** 0.5}")
              case _:
                print(f"{one}{two}")
            wait(2)
            mode = "home"
        case _:
          p("wtf")
    if random.randint(0, 2) == 1: p("Mooooo!")

  print("thank you for using MING!")
  wait(1)