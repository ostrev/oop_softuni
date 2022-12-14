from project.hardware.hardware import Hardware


class HeavyHardware(Hardware):
    CAPACITY_HEAVY_PR = 2
    MEMORY_HEAVY_PR = 0.75

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, "Heavy", capacity * self.CAPACITY_HEAVY_PR, int(memory * self.MEMORY_HEAVY_PR))
