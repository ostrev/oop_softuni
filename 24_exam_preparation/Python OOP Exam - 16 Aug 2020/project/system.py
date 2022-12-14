from project.hardware.heavy_hardware import HeavyHardware
from project.hardware.power_hardware import PowerHardware
from project.software.express_software import ExpressSoftware
from project.software.light_software import LightSoftware


class System:
    _hardware = []
    _software = []

    @staticmethod
    def register_power_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(PowerHardware(name, capacity, memory))

    @staticmethod
    def register_heavy_hardware(name: str, capacity: int, memory: int):
        System._hardware.append(HeavyHardware(name, capacity, memory))

    @staticmethod
    def register_express_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                soft = ExpressSoftware(name, capacity_consumption, memory_consumption)
                hardware.install(soft)
                System._software.append(soft)
                return
        return "Hardware does not exist"

    @staticmethod
    def register_light_software(hardware_name: str, name: str, capacity_consumption: int, memory_consumption: int):
        for hardware in System._hardware:
            if hardware.name == hardware_name:
                soft = LightSoftware(name, capacity_consumption, memory_consumption)
                hardware.install(soft)
                System._software.append(soft)
                return
        return "Hardware does not exist"

    @staticmethod
    def release_software_component(hardware_name: str, software_name: str):
        try:
            hardware = [h for h in System._hardware if h.name == hardware_name][0]
            software = [h for h in System._software if h.name == software_name][0]
            hardware.uninstall(software)
            System._software.remove(software)
        except IndexError:
            return "Some of the components do not exist"

    @staticmethod
    def analyze():
        result = 'System Analysis\n'
        result += f'Hardware Components: {len(System._hardware)}\n'
        result += f'Software Components: {len(System._software)}\n'
        total_memory_soft = 0
        total_capacity_soft = 0
        total_memory_hard = 0
        total_capacity_hard = 0
        for soft in System._software:
            total_memory_soft += soft.memory_consumption

            total_capacity_soft += soft.capacity_consumption

        for hard in System._hardware:
            total_memory_hard += hard.memory

            total_capacity_hard += hard.capacity
        result += f'Total Operational Memory: {total_memory_soft} / {total_memory_hard}\n'
        result += f'Total Capacity Taken: {total_capacity_soft} / {total_capacity_hard}'
        return result


    @staticmethod
    def system_split():
        result = ''
        for hardware in System._hardware:
            result += f'Hardware Component - {hardware.name}\n'
            light_count = len([soft for soft in hardware.software_components if soft.software_type == 'Light'])
            express_count = len([soft for soft in hardware.software_components if soft.software_type == 'Express'])
            result += f'Express Software Components: {express_count}\n'
            result += f'Light Software Components: {light_count}\n'
            total_mem_install_soft = sum([soft.memory_consumption for soft in hardware.software_components])
            result += f'Memory Usage: {total_mem_install_soft} / {hardware.memory}\n'
            total_capacity_soft = sum([soft.capacity_consumption for soft in hardware.software_components])
            result += f'Capacity Usage: {total_capacity_soft } / {hardware.capacity}\n'
            result += f'Type: {hardware.hardware_type}\n'
            names = ', '.join([soft.name for soft in hardware.software_components])
            result += f"Software Components: {names if names else None}\n"

        return result.strip()
