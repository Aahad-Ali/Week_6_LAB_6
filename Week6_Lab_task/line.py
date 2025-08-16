from dataclasses import dataclass
from point import Point


@dataclass(frozen=True)
class Line:
    start: Point
    end: Point