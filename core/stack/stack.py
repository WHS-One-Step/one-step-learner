# Written by: Christopher Gholmieh
# Imports:

# Typing:
from typing import (List, Any)


# Stack:
class Stack:
    # Initialization:
    def __init__(self, maximum_length: int) -> None:
        # Constants:
        # Maximum:
        self.maximum_length: int = maximum_length

        # Buffer:
        self.buffer: List[Any] = []

    # Methods:
    def append(self, item: Any) -> None:
        # Validation:
        if len(self.buffer) == self.maximum_length:
            self.buffer.pop(0)

        # Logic:
        self.buffer.append(item)

    def __len__(self) -> int:
        return len(self.buffer)