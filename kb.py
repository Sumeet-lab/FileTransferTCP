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

