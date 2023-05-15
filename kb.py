
import keyboard as k,time,pickle

events = k.record(until="esc")
print("Event recorded")
s = pickle.dumps(events)
print(s)
time.sleep(2)
print("Event playing")
es = pickle.loads(s)
print(es)
k.play(es,speed_factor=1)
serverEventLength = 0
def serverKeyRecorder():
    while True:
        print("[KEYBOARD] Keystrokes are getting captured (Press esc to quit capturing) ")
        events = k.record(until="esc")
        # events.append("null".encode('utf-8'))
        input()
        choice = input(f"[KEYBOARD] Proceed with captured keys? (y/n): {events}").lower()

