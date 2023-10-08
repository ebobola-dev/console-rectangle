from colorama import Fore
from math import ceil as round_up, floor

COLORS = [
	Fore.RED,
	Fore.BLUE,
	Fore.GREEN,
	Fore.WHITE,
	Fore.MAGENTA,
	Fore.YELLOW,
]

def aboba(width: int, heigth: int, colors: [str], symbol: str):
	def get_color(color_index: int):
		if color_index >= len(colors):
			while color_index >= len(colors):
				color_index = color_index - len(colors)
		return colors[color_index]

	for h in range(floor(heigth / 2)):

		for w in range(h):
			print(get_color(w) + symbol, end='')

		for w in range(h, width - h):
			print(get_color(h) + symbol, end='')

		for w in range(width - h, width):
			print(get_color(width - w - 1) + symbol, end='')

		print()

	k = floor(heigth / 2)
	if k % 2 == 0:
		k -= 1
	for h in range(floor(heigth / 2), heigth):

		for w in range(k):
			print(get_color(w) + symbol, end='')

		for w in range(k, width - k):
			print(get_color(k) + symbol, end='')

		for w in range(width - k, width):
			print(get_color(width - w - 1) + symbol, end='')

		k -= 1
		print()

aboba(29, 15, COLORS, '▮')