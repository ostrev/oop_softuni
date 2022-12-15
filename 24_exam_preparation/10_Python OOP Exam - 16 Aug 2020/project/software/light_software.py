from project.software.software import Software


class LightSoftware(Software):
    CAPACITY_CONSUMPTION_LIGHT_PR = 1.5
    MEMORY_CONSUMPTION_LIGHT_PR = 0.5

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, "Light", capacity_consumption, memory_consumption)
        self.capacity_consumption = int(self.capacity_consumption * self.CAPACITY_CONSUMPTION_LIGHT_PR)
        self.memory_consumption = int(self.memory_consumption * self.MEMORY_CONSUMPTION_LIGHT_PR)
