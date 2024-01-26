from dataclasses import dataclass


@dataclass
class Step:
    action: str
    target: str
