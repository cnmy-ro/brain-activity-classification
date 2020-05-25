import numpy as np

for i in range(3):
	for j in range(5):
		np.random.seed(j)
		print(np.random.random(), '  ', end='')
	print("\n")