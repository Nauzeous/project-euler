file = open("sudoku.txt")

grids = []
grid = []
for line in file:
	l = line.strip()
	if l[0] == "G":
		grids.append(grid)
		grid = []
		continue
	grid.append(l)
print(grids)

for grid in grids:
	for line in grid:
		print(line)
	print("------\n")

grid = ["000003017"
,"015009008"
,"060000000"
,"100007000"
,"009000200"
,"000500004"
,"000000020"
,"500600340"
,"340200000"]

solvegrid(grid)
