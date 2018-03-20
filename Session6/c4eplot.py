import matplotlib
matplotlib.use("TkAgg")

from matplotlib import pyplot
# 1. prepare data
labels = ["Web", "iOS", "Android", "React Native"]
values = [40, 20, 25, 15]
colors = ["red", "purple", "pink", "grey"]
explode = [0, 0.2, 0, 0]
# 2. plot
pyplot.pie(values, labels = labels, colors = colors, explode= explode, shadow = True)
pyplot.axis("equal")

# 3. show
pyplot.show()
