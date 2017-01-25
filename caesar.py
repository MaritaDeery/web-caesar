def alphabet_position(letter):
	total_pos = 0
	for l in letter:
		l = ord(l)
		if 65 <= l <= 90:
			pos = l - 65
		else:
			pos = l - 97
		total_pos = total_pos + pos + 1
	return(total_pos - 1)
 #print(alphabet_position(" "))


def rotate_character(char, rot):
	if not char.isalpha():
		return char
	if char.islower():
		return chr(((alphabet_position(char) + rot) % 26) + ord('a'))
	if char.isupper():
		return chr(((alphabet_position(char) + rot) % 26) + ord('A'))
# print(rotate_character('', ''))

def encrypt(text, rot):
	cipher = ""
	for char in text:
		cipher = cipher + rotate_character(char, rot)				
	return cipher	

