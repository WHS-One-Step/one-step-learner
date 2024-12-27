# Written by: Christopher Gholmieh
# Imports:

# Core:
from core import (IMU)

# Functions:
def main() -> None:
    # Variables (Assignment):
    # IMU:
    imu: IMU = IMU(enable_predictions=False)

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
    

# Main:
main()