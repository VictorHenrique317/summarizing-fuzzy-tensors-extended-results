import matplotlib.pyplot as plt

tsv = """
0	7644.666
1	7154.2200454188105
2	6665.539769956308
3	6178.025753920034
4	5691.180321637844
5	5205.298683134938
6	4720.42570994993
7	4236.121232713996
8	3753.567896167258
9	3271.9059479885173
10	2793.243585685371
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
