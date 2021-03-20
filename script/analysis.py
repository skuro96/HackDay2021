import matplotlib.pyplot as plt

y = []
input_file = open('speed.txt', 'r', encoding = 'utf_8')

i = 0
while True:
	line = input_file.readline()

	if line:
		i += 1
		y.append(1 - float(line))
	else:
		break

input_file.close()

x = [j for j in range(i)]
plt.plot(x, y)
plt.show()
