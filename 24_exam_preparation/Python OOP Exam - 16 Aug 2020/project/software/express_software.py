from project.software.software import Software


class ExpressSoftware(Software):
    MEMORY_CONSUMPTION_EXPRESS_PR = 2

    def __init__(self, name: str, capacity_consumption: int, memory_consumption: int):
        super().__init__(name, "Express", capacity_consumption, memory_consumption)
        self.memory_consumption = self.memory_consumption * self.MEMORY_CONSUMPTION_EXPRESS_PR
