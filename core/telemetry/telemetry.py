# Written by: Christopher Gholmieh
# Imports:

# Matplotlib:
# Figure:
from matplotlib.figure import Figure

# Plot:
import matplotlib.pyplot as plot

# Typing:
from typing import (List)

# Stack:
from ..stack import (Stack)


# Telemetry:
class Telemetry:
    # Initialization:
    def __init__(self) -> None:
        # Stack:
        self.stack: Stack = Stack(maximum_length=100)

    # Methods:
    def append(self, acceleration: List[float]) -> None:
        # Logic:
        self.stack.append(acceleration)

    def graph_three_dimensional(self) -> None:
        # Validation:
        if len(self.stack) == 0:
            raise ValueError("[!] There is no data available to graph..")

        # Variables (Assignment):
        # Data:
        data: List[List[float, float, float]] = self.stack.buffer

        # Accelerations:
        x_accelerations = [point[0] for point in data]
        y_accelerations = [point[1] for point in data]
        z_accelerations = [point[2] for point in data]

        # Figure:
        figure: Figure = plot.figure()

        # Axes:
        axes = figure.add_subplot(111, projection="3d")

        # Logic:
        # Plot:
        axes.plot(x_accelerations, y_accelerations, z_accelerations, marker="o", label="3D Acceleration")

        # Labels:
        axes.set_xlabel("X Acceleration")
        axes.set_ylabel("Y Acceleration")
        axes.set_zlabel("Z Acceleration")

        axes.set_title("3D Acceleration Data")

        # Plot:
        plot.show()

    def graph_two_dimensional(self) -> None:
        # Validation:
        if len(self.stack) == 0:
            raise ValueError("[!] There is no data available to graph..")

        # Variables (Assignment):
        # Data:
        data: List[List[float, float, float]] = self.stack.buffer

        # Accelerations:
        x_accelerations = [point[0] for point in data]

        # Logic:
        # Figure:
        plot.figure()

        # Plot:
        plot.plot(range(len(x_accelerations)), x_accelerations, marker="o", label="X Acceleration")

        # Labels:
        # Title:
        plot.title("X Accelerations / Time")

        # X: 
        plot.xlabel("Sequence")

        # Y:
        plot.ylabel("X Acceleration")

        # Legend:
        plot.legend()

        # Plot:
        plot.show()