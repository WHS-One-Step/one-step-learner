# Written by: Christopher Gholmieh
# Imports:

# Phidget:
from Phidget22.Devices.Accelerometer import (Accelerometer)

# Telemetry:
from ..telemetry import (Telemetry)

# Learner:
from ..learner import (Learner)

# Typing:
from typing import (Callable, Dict, List)

# Loguru:
from loguru import (logger)

# Stack:
from ..stack import (Stack)


# IMU:
class IMU:
    # Initialization:
    def __init__(self, enable_predictions: bool = False, learner_path: str = "learner/one-step-learner.pkl"):
        # Constants:
        # Predictions:
        self.enable_predictions: bool = enable_predictions

        # Telemetry:
        self.telemetry: Telemetry = Telemetry()

        # Learner:
        self.learner = Learner(learner_path)
        self.learner.load()

        # Gadgets:
        self.gadgets: Dict[str, Callable] = {
            # Accelerometer:
            "accelerometer": Accelerometer()
        }

        # Stack:
        self.stack: Stack = Stack(maximum_length=3)

    # Methods:
    def initialize_handlers(self) -> None:
        # Acceleration:
        def on_acceleration_change_handler(
            # Accelerometer:
            accelerometer: Accelerometer,

            # Acceleration:
            acceleration: List[float],

            # Timestamp:
            timestamp: float
        ) -> None:
            # Variables (Assignment):
            # Message:
            message: str = "{} | {}".format(
                # Acceleration:
                ",".join(map(str, acceleration)),

                # Timestamp:
                timestamp
            )

            # Logging:
            logger.info(message)

            # Logic:
            self.telemetry.append(acceleration)
            self.stack.append(acceleration)

            # Predictions:
            if self.enable_predictions:
                if len(self.stack) == 3:
                    logger.info("[*] Prediction: {}".format(
                        self.learner.predict(self.stack.buffer)
                    ))
                else:
                    logger.info("[*] Not enough data to perform a prediction.")

        # Accelerometer:
        self.gadgets["accelerometer"].setOnAccelerationChangeHandler(
            on_acceleration_change_handler
        )

    def initialize_gadgets(self) -> None:
        # Initialization:
        for gadget in self.gadgets.values():
            # Attachment:
            gadget.openWaitForAttachment(1000)

            # Interval:
            gadget.setDataInterval(1000)

    def terminate(self) -> None:
        # Termination:
        for gadget in self.gadgets.values():
            # Close:
            gadget.close()

        # Telemetry:
        if input(
            "[?] Would you like to view two dimensional telemetry of X Accelerations over time? [y/N]: "
        ).strip().lower() in "yes":
            self.telemetry.graph_two_dimensional()