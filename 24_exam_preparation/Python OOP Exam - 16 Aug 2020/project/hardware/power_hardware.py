from project.hardware.hardware import Hardware


class PowerHardware(Hardware):
    CAPACITY_POWER_PR = 0.25
    MEMORY_POWER_PR = 1.75

    def __init__(self, name: str, capacity: int, memory: int):
        super().__init__(name, "Power", int(capacity * self.CAPACITY_POWER_PR), int(memory * self.MEMORY_POWER_PR))
