from broadcast import emitter

import main
import math
import random

global ads
adsallow = True

def p(j):
  print(j)

def space(num: int):
  for x in range(0, num): p("")

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


def process(cmd: str):
    match cmd:
      case "help":
        p("""functions:
> SIN [sine]
> COS [cosine]
> TAN [tangent]
> FAC [factorial]
> EXT [exit]
""")
      case "SIN":
        munber = main.floatify(input("Give me the nuber: "))
        if random.randint(0, 3) == 1: ad()
        print(math.sin(munber))
        main.wait(2)
      case "COS":
        munber = main.floatify(input("Give me the nuber: "))
        if random.randint(0, 3) == 1: ad()
        print(math.cos(munber))
        main.wait(2)
      case "TAN":
        munber = main.floatify(input("Give me the nuber: "))
        if random.randint(0, 3) == 1: ad()
        print(math.tan(munber))
        main.wait(2)
      case "FAC":
        munber = main.floatify(input("Give me the nuber: "))
        if random.randint(0, 3) == 1: ad()
        if munber < 0: p("stupid (but advanced)")
        else: print(math.factorial(munber))
        main.wait(2)
      case "EXT":
        main.mode = "home"
      case _:
        p("Advanced Mode doesnt know what the heck (hell) you mean by that.")

emitter.on_message("advanced.sent", process)