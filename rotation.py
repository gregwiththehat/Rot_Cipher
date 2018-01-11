"""Rotation Cipher
This converts a message into uppercase, then performs an
ASCII based Rotation ciper on the altered text"""

rot_num = int(input("Rotation Value? "))
message = input("What is the message to encode? ")
message = message.upper()
unencrypted = []
encrypted = []
x = 0

while x < len(message):
	unencrypted.append((message [x]))
	y = ord(message [x])
	y = y + rot_num
	
	if y == 32+rot_num:
		"""This was the only way I could think of 
		to make spaces stay spaces.
		Which is technically not good crypto."""
		
		encrypted.append((chr(32)))
		
	elif y > 90:
		
		y=y-26
		encrypted.append((chr(y)))
		
	else:
		
		encrypted.append((chr(y)))
	
	x = x + 1
	
print(unencrypted)
print(encrypted)
	
	
