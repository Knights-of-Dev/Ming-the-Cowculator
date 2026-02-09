from ..broadcast import emitter
import main
name = "Sample Module"

def on_more():
    print("""Sample's Commands:
- test [prints the fact that you are a toy]
- adbr [ad break time.]""")
    
def on_send():
    match command:
        case "test":
            recog = True
            print("You are a toy.")
        case "adbr":
            print("Ad break time.")
        case _:
            