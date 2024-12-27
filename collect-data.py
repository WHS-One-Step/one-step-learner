# Written by: Christopher Gholmieh
# Imports:

# Typing:
from typing import (List)

# Logger:
from loguru import (logger)

# Core:
from core import (IMU)

# CSV:
from csv import (writer)


# Functions:
def main() -> None:
    # Variables (Assignment):
    # Labels:
    labels: List[str] = ["walking backward", "standing still", "walking forward"]

    # Label:
    label: str = input("[?] What label would you like to use for your data: ").strip().lower()

    # Logic:
    # Validation:
    if label not in labels:
        raise ValueError("[!] An appropriate label was not given.")

    # Variables (Assignment):
    # IMU:
    imu: IMU = IMU(
        # Predictions:
        enable_predictions=False,

        # Learner:
        learner_path="learner/one-step-gyroscope-learner.pkl",

        # Collect:
        collect=True
    )

    # Initialization:
    # Gadgets:
    imu.initialize_gadgets()

    # Handlers:
    imu.initialize_handlers()
    
    # Logic:
    try:
        input("[*] Press enter to terminate the program.." + "\n")
    except (Exception, KeyboardInterrupt):
        pass

    imu.terminate()

    # Collection:
    with open("collection/imu-data.csv", "w", newline="") as CSV:
        # Variables (Assignment):
        # Writer:
        file_writer = writer(CSV)

        # Logic:
        # Headers:
        file_writer.writerow([
            # Acceleration:
            "acceleration_x", "acceleration_y", "acceleration_z",

            # Rotation:
            "angular_rotation_x", "angular_rotation_y", "angular_rotation_z",

            # Label:
            "label"
        ])

        # Data:
        for acceleration_vector, angular_rotation_vector in zip(
            imu.acceleration_data, imu.gyroscope_data
        ):
            file_writer.writerow(
                acceleration_vector + angular_rotation_vector + [label]
            )

    # Close:
    CSV.close()

    # Logging:
    logger.info("[*] Saved successfully to collection/imu-data.csv")


# Main:
main()