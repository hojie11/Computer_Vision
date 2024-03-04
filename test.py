from visdom import Visdom
import numpy as np

# Create a Visdom instance
viz = Visdom()

# Generate dummy data
x = np.arange(10)
y = np.random.rand(10)

# Create a line plot
viz.line(X=x, Y=y, opts=dict(title='Dummy Line Plot', xlabel='X', ylabel='Y'))