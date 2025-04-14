# One-Step-Learner
The purpose of this repository is to contain a training environment to produce one-step-learner agents capable of predicting the co-designer's gait state, such was walking forwards, standing still, or walking backwards.

## Directories:
- Bootstrap: Contains bootstrapping scripts to install a Python Virtual Environment, and install dependencies pertaining to the Operating System as well as the Python project.
- Collection: Contains data to train the one-step-learner agents.
- Core: Contains the fundamental components dedicated to ensuring the training environment functions, such as the IMU, Learner Model, Telemetry (Graphing), and internal Stack component.
- Learner: Contains all potential learner and trained learner models.

## Interactions:
- collect-data.py: Collects data that follows no variational data, meaning that each three data sets will share the same label.
- collect-variational-data.py: Collects data that follows a variational pattern, meaning that the three data sets will follow a pattern. (Example: standing still, walking forward, standing still)
- interact-learner.py: Provides an interface to have a learner predict or be trained on data.

## Installation:
To install the project, execute the following commands in a Linux terminal.

```bash
# Clone Repository:
git clone https://https://github.com/whs-one-step/one-step-learner && cd ./one-step-learner/

# Instructions:
chmod +x ./bootstrap/* # Transform the scripts into executables.

./bootstrap/bootstrap-raspberry.sh # Install appropriate Linux dependencies.
./bootstrap/bootstrap-environment.sh # Install appropriate Python dependencies and Virtual Environment.

venv/bin/python ./main.py # Run the python project.
```

## Framework:
No frameworks were used in the programming of this repository, as it was not forced to be structured in a specific way. However, a variety of third-party libraries were used for extensive functionality, such as training and creating models.

## Language:
Python was used to program this repository as it allowed for extreme developer productivity through the use of third-party packages.
