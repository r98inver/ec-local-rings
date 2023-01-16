from itertools import combinations_with_replacement
from time import time
from math import factorial

class Monom:
	def __init__(self, a=(0,0,0), x=0, z=0):
		# a = (a_0, A, B)
		self.a = a # len(a) == 3 !!!
		self.x = x
		self.z = z

	def get_deg(self):
		# Total degree of m: deg(x) + 3deg(z)
		return self.x + 3*self.z

	def step(self):
		# Substitution of z
		# a_4 = A
		# a_6 = B
		# z = (a_0)x^3 + a_4xz^2 + a_6z^3
		# Coeffs of (x,z)
		inc = [(3,0), (1,2), (0,3)]

		if self.z == 0:
			return [(self, 1)]

		out = []

		for i,new_inc in enumerate(inc):
			# Increment counter of a_i
			new_a = []
			for j in range(3):
				if j == i:
					new_a.append(self.a[j] + 1)
				else:
					new_a.append(self.a[j])
			new_a = tuple(new_a)
			new_x = self.x + new_inc[0]
			new_z = self.z - 1 + new_inc[1]
			out.append((Monom(a=new_a, x=new_x, z=new_z), 1))		
		return out

	def __str__(self):
		a_names = ['a0','A', 'B'] #magma
		# a_names = ['a_0','A','B'] #latex	
		out = ''
		for i in range(1,3):
			if self.a[i] == 1:
				out += f'*{a_names[i]}'
			elif self.a[i] > 1:
				out += f'*{a_names[i]}^{self.a[i]}'
		if self.x == 1:
			out += '*X'
		elif self.x > 1:
			out += f'*X^{self.x}'
		if self.z == 1:
			out += '*Z'
		elif self.z > 1:
			out += f'*Z^{self.z}'
		
		if out == '':
			return out
		return out[1:]

	def __eq__(self, other):
		return self.a[1:] == other.a[1:] and self.x == other.x and self.z == other.z

	def __hash__(self):
		return hash((self.a[1:], self.x, self.z))


def main(k: int = 250):
	final = {}
	m = Monom(z=1)
	q = {}
	q[m] = 1

	intro = f"""// z coordinate as a function of x in pi^{-1}(0) in reduced form
// Usage:
/*
k := {k}; // Nilpotence degree of eps
R<A, B, X> := PolynomialRing(Integers(), 3);
I := ideal<R | X^k>;
Rk := R/I;
load "zfx_reduced.magma";
F := Rk!F;
*/

"""
	cnt = 0
	t1 = time()
	while q != {}:
		# pop_m, pop_c = q.popitem() # DFS - No pruning!!
		pop_m = next(iter(q)) # BFS - Much faster
		pop_c = q.pop(pop_m)

		cnt += 1
		if cnt == 10000:
			# Logging stuff
			t2 = time()
			print(f'{len(q) = } {len(final) = } t = {round(t2-t1, 2)}')
			# print(f'deg = {pop_m.get_deg()} {pop_c = } sample = {str(pop_m)}')
			cnt = 0

		# Compute the step
		new_mon = pop_m.step()
		for m, c in new_mon:
			# m is the monomial, c the coefficient
			# High degree
			if m.get_deg() > k:
				continue

			# No z
			if m.z == 0:
				final[m] = final.get(m, 0) + pop_c * c
				continue
			q[m] = q.get(m, 0) + pop_c * c

	# Order printable strings by degree
	degs = {}
	for i in final:
		assert i.z == 0

		deg = i.get_deg()
		# sig = '+' # <-- always positive
		coeff = final[i]
		mon = str(i)

		if coeff != 1:
			degs[deg] = degs.get(deg, '') + f'+{coeff}*{mon}'
		else:
			degs[deg] = degs.get(deg, '') + f'+{mon}'

	debug_step = 200
	next_debug = 200 # Log every time 200 degrees are loaded in magma

	# Write on file
	with open(f'zfxred_stored_{k}.magma', 'w') as fh:
		fh.write(intro)
		fh.write('F := \n')
		for d in degs:
			if d > next_debug:
				fh.write(f';\nprint "Loaded {next_debug} degrees";\nF +:= \n')
				next_debug += debug_step
			fh.write(f'\t{degs[d]}\n')
		fh.write(';')


if __name__ == '__main__':
	k = 300 # Nilpotence degree of eps
	main(k=k)