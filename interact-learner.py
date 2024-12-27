# Written by: Christopher Gholmieh
# Imports:

# Argparse:
import argparse

# Loguru:
from loguru import (logger)

# Typing:
from typing import (List)

# Core:
from core import (Learner)

# Functions:
def main() -> None:
    # Variables (Assignment):
    # Parser:
    argument_parser: argparse.ArgumentParser = argparse.ArgumentParser(
        # Description:
        description="Perform an interaction to the one-step learner."
    )

    # Learner:
    learner: Learner = Learner("./learner/one-step-learner.pkl")

    # Arguments:
    argument_parser.add_argument(
        # Flag:
        "--train",

        # Type:
        type=str,

        # Help:
        help="Train the one-step Learner with a .csv file.",
    )

    argument_parser.add_argument(
        # Flag:
        "--learner-path",

        # Type:
        type=str,

        # Help:
        help="Path to save or load the trained model.",

        # Default:
        default="./learner/one-step-learner.pkl",
    )

    argument_parser.add_argument(
        # Flag:
        "--predict",

        # Help:
        help="Predict the motion of a movement given IMU readings in the form of space-separated values.",

        # Default:
        default=False,
        
        # Action:
        action="store_true"
    )

    # Logic:
    arguments: argparse.Namespace = argument_parser.parse_args()

    # Variables (Assignment):
    learner: Learner = Learner(learner_path=arguments.learner_path)
    learner.load()

    # Logic:
    if arguments.train:
        learner.train(arguments.train)

    if arguments.predict:
        # Variables (Assignment):
        primary: List[float]  = list(map(float, input("First data set (values separated by commas): ").split(",")))
        secondary: List[float] = list(map(float, input("Second data set (values separated by commas): ").split(",")))
        tertiary: List[float] = list(map(float, input("Third data set (values separated by commas): ").split(",")))

        logger.info("Prediction result: " + learner.predict([primary, secondary, tertiary]))

# Main:
main()