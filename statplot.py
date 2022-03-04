import matplotlib
import sys
import matplotlib.pyplot as plt


print("Zanvok Office StatPlot")
print("-"*30)
print()
print()
print("""
[1] Plot a new Pie Chart
[2] Plot a new Histogram
[3] Version
	""")

select = ""
while select != 'quit' or select != 'exit':
	select = input("Enter a value > ")

	if select == '1':
		activities = []
		n = int(input("Enter number of activities/labels: "))
		for i in range(0,n):
			print()
			print("Enter activities/labels: ".format(i+1))
			elm = input()
			activities.append(elm)
			print()
		
		print()
		slices = []
		for j in range (0,n):
			print("Enter portions covered by each activity/label: ".format(j+1))
			eln = int(input())
			slices.append(eln)

		print()
		colors = []
		for k in range (0,n):
			print("Enter colors: ".format(k+1))
			elo = input()
			colors.append(elo)

		print()
		print("Plotting your Pie Chart...")
		print()
		plt.pie(slices, labels = activities, colors=colors,
				startangle=90, shadow = True,
				radius = 1.2, autopct = '%1.1f%%')

		# plotting legend
		plt.legend()

		# showing the plot
		plt.show()

	elif select == '2':
		histogram = []
		import numpy as np
		n = int(input("Enter number of activites/labels: "))
		for i in range(0,n):
			print("Enter values: ".format(i+1))
			elm = input()
			histogram.append(elm)
			x = np.random.normal(histogram)
			plt.hist(x)
			plt.show()
			print("Plotted Histogram...!")

	elif select == '3' or select == 'ver':
		print("Zanvok StatPlot for Office")
		print("Ver: 22.2.3 '2022'")
	else:
		print("Not yet Programmed..!")
