#!/bin/python

def main():
	def choose(gg, compress):
		base = len(compress(gg))
		gg.append(1)
		gr = len(compress(gg)) - base
		gg[-1] = 2
		gp = len(compress(gg)) - base
		gg[-1] = 3
		gs = len(compress(gg)) - base
		del gg[-1]
		while gr < 1 or gp < 1 or gs < 1:
			gr += 1
			gp += 1
			gs += 1
		cc = randint(0, gr + gp + gs) - gr
		return 0 if cc <= 0 else 1 if cc <= gp else 2

	from sys import argv
	aivai = "aivai" in argv
	from random import randint
	score = 0
	if aivai:
		from bz2 import compress as bz
		from zlib import compress as gz
		from itertools import repeat
		c0 = randint(0, 2)
		c1 = randint(0, 2)
		g0 = bytearray()
		g1 = bytearray()
		rounds = 256
		while True:
			for i in repeat(None, 256):
				s = ((0, -1, 1), (1, 0, -1), (-1, 1, 0))[c0][c1]
				score += s
				g0.append(c0)
				g1.append(c1)
				c0 = choose(g1, gz)
				c1 = choose(g0, bz)
			print("gz", "".join("RPS"[x] for x in g0[-256:]))
			print("bz", "".join("RPS"[x] for x in g1[-256:]))
			print(f"Tied after {rounds} rounds" if not score else f"gz leads by {score} after {rounds} rounds" if score > 0 else f"bz leads by {-score} after {rounds} rounds")
			rounds += 256
	else:
		if "bz2" in argv:from bz2 import compress
		else:from zlib import compress
		gg = bytearray()
		c = randint(0, 2)
		while True:
			g = input(f"{score} RPS?").lower()
			g = "rps".find(g)
			if g == -1:return
			s = ((0, -1, 1), (1, 0, -1), (-1, 1, 0))[g][c]
			score += s
			print(("You lose", "Tie", "You win")[s+1])
			gg.append(g)
			c = choose(gg, compress)
main()
