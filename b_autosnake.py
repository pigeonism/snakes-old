# auto snake, opens a_snakestry.py and attempts to play
# SEE 'xev' cmd for keycodes needed



#!/usr/bin/env python
from Xlib import X, XK, error, display
import Xlib.ext.xtest
from time import sleep # for waiting inbetween sim keys

# set display var
d = display.Display()
s = d.screen()
root = s.root

def key_nav(current_direction):
	print("SO it begins... ")
	print("Current direction is: ", current_direction)

	#os.system( "python a_snakestry.py"  ) # system call or exec?

	# c++ XKeyEvent event = createKeyEvent(display, winFocus, winRoot, true, KEYCODE, 0);
	#root.warp_pointer(x_region, y_region)

	# 114 right, 116 down, 113 left, 111 up

	if current_direction == "D":
		# go RIGHT, then UP
		Xlib.ext.xtest.fake_input(d,Xlib.X.KeyPress, 114) 
		d.sync()
		Xlib.ext.xtest.fake_input(d,Xlib.X.KeyRelease, 114)
		d.sync()

		Xlib.ext.xtest.fake_input(d,Xlib.X.KeyPress, 111) 
		d.sync()
		Xlib.ext.xtest.fake_input(d,Xlib.X.KeyRelease, 111)
		d.sync()

	if current_direction == "U":
		# go RIGHT, then down
		Xlib.ext.xtest.fake_input(d,Xlib.X.KeyPress, 114) 
		d.sync()
		Xlib.ext.xtest.fake_input(d,Xlib.X.KeyRelease, 114)
		d.sync()

		Xlib.ext.xtest.fake_input(d,Xlib.X.KeyPress, 116) 
		d.sync()
		Xlib.ext.xtest.fake_input(d,Xlib.X.KeyRelease, 116)
		d.sync()


	if current_direction == "R":
		# go up then left
		Xlib.ext.xtest.fake_input(d,Xlib.X.KeyPress, 111) 
		d.sync()
		Xlib.ext.xtest.fake_input(d,Xlib.X.KeyRelease, 111)
		d.sync()

		# LEFT
		Xlib.ext.xtest.fake_input(d,Xlib.X.KeyPress, 113) 
		d.sync()
		Xlib.ext.xtest.fake_input(d,Xlib.X.KeyRelease, 113)
		d.sync()
		
	if current_direction == "L":
		# go up then right
		Xlib.ext.xtest.fake_input(d,Xlib.X.KeyPress, 111) 
		d.sync()
		Xlib.ext.xtest.fake_input(d,Xlib.X.KeyRelease, 111)
		d.sync()

		# r
		Xlib.ext.xtest.fake_input(d,Xlib.X.KeyPress, 114) 
		d.sync()
		Xlib.ext.xtest.fake_input(d,Xlib.X.KeyRelease, 114)
		d.sync()
		
		

	#sleep(1)
	# DOWN
	#Xlib.ext.xtest.fake_input(d,Xlib.X.KeyPress, 116) 
	#d.sync()
	#Xlib.ext.xtest.fake_input(d,Xlib.X.KeyRelease, 116)
	#d.sync()

	#sleep(1)
	# LEFT
	#Xlib.ext.xtest.fake_input(d,Xlib.X.KeyPress, 113) 
	#d.sync()
	#Xlib.ext.xtest.fake_input(d,Xlib.X.KeyRelease, 113)
	#d.sync()

	#sleep(1)
	# Down.
	#Xlib.ext.xtest.fake_input(d,Xlib.X.KeyPress, 116) 
	#d.sync()
	#Xlib.ext.xtest.fake_input(d,Xlib.X.KeyRelease, 116)
	#d.sync()

	#sleep(1)


	print("did it? yes. Finished.")
