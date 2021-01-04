from colorama import Fore, Back, Style

print(Back.BLUE + 'This is a review/practice to see what I remember from the other day!' + Style.RESET_ALL + '\n')

square = input('Would you like to print a square?: ')

if 'yes' in square.lower():
	w = int(input('Please specify the width of your square: '))
	h = int(input('Please specify the height of your square: '))
	print('\n' + Fore.RED + 'Be there or be square' + Style.RESET_ALL)
	print('x' * w)
	for i in range(h-2):
		print('x' + ('-' * (w-2)) + 'x')
	print('x' * w)
else:
	print('\n Well okay then...')
ask = input('\n' + Back.BLUE + 'Is there any other shape that you would like me to print?:' + Style.RESET_ALL + ' ')

while ask != 'no':
	if 'triangle' in ask.lower():
		ht = int(input('Please specify a height for your triangle: '))
		print('\n' + Fore.GREEN + 'A different kind of pyramid scheme' + Style.RESET_ALL)
		for j in range(ht):
			print(' '*(ht-j-1) + '^'*((2*j)+1))
		ask = input('\n' + Back.BLUE + 'Is there any other shape that you would like me to print?:' + Style.RESET_ALL + ' ')
	elif 'diamond' in ask.lower():
		half = int(input('Please insert a number: '))
		print('\n' + Fore.YELLOW + "Diamonds are a girl's best friend" + Style.RESET_ALL)
		for k in range(half):
			print(' '*(half-k-1) + '*'*((2*k)+1))
		for k in range(half):
			print(' '*(k+1) + '*'*((2*((half-1)-k))-1))
		ask = input('\n' + Back.BLUE + 'Is there any other shape that you would like me to print?:' + Style.RESET_ALL + ' ')
	elif 'circle' in ask.lower():
		d = int(input('What is the diametre of your circle? '))
		print('\n' + Fore.CYAN + 'A tautological argument' + Style.RESET_ALL)
		print(' ' + 'o'*(d-2) + ' ')
		for l in range(d-2):
			print('o' + ' '*(d-2) + 'o')
		print(' ' + 'o'*(d-2) + ' ')
		ask = input('\n' + Back.BLUE + 'Is there any other shape that you would like me to print?:' + Style.RESET_ALL + ' ')
	else:
		ask = input('\n' + Back.BLUE + 'Apologies, this shape is yet to be registered with our system. We have options of a triangle, diamond, or circle though if you would like?:' + Style.RESET_ALL + ' ')

print('\n' + Fore.MAGENTA + 'Bye for now then!' + Style.RESET_ALL)
