import math
def solve_quadratic(a,b,c):

	d = b * b - 4 * a * c
	sqrt = math.sqrt(abs(d))
	
	
	if d > 0:
		print((-b + sqrt)/(2 * a))
		print((-b - sqrt)/(2 * a))
	
	elif d == 0:
		print(-b / (2 * a))
	
	else:
		return None



