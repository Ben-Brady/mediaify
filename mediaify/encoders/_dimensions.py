from dataclasses import dataclass
from typing_extensions import Self

@dataclass
class Dimensions:
    x: int
    y: int

    def calculate_downscale(self, target: "Self") -> "Self":
        biggest_factor = max(
            1,
            self.x / target.x,
            self.y / target.y,
        )

        output_width = int(self.x / biggest_factor)
        output_height = int(self.y / biggest_factor)

        return Dimensions(output_width, output_height)
