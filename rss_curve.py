import matplotlib.pyplot as plt

tsv = """
0	55660.9
1	55646.504106735214
2	55638.05422485019
3	55632.76370486237
4	55629.56043669085
5	55627.87656040036
6	55626.770376008375

"""

xs = []
ys = []

lines = tsv.split("\n")
for line in lines:
    if line == "":
        continue
    
    
    if "\t" in line:
        line = line.split("\t")
    else:
        line = line.split(" ")
        # remove empty strings from line list
        line = list(filter(lambda x: x != "", line))


    x = line[0]
    y = line[1]
    x = int(x)
    y = float(y)
    xs.append(x)
    ys.append(y)

plt.plot(xs, ys)

# only show xticks from 1 to 20
plt.xticks(range(1, 21))

plt.show()
