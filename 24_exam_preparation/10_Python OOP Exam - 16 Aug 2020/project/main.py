from system import System

System.register_power_hardware("HDD", 200, 200)
System.register_heavy_hardware("SSD", 400, 400)
# print(System.analyze())
System.register_light_software("HDD", "Test", 0, 10)
System.register_express_software("HDD", "Test3", 50, 100)
System.register_light_software("SSD", "Windows", 20, 50)
System.register_express_software("SSD", "Linux", 50, 100)
System.register_light_software("SSD", "Unix", 20, 50)

System.release_software_component("SSD", "Linux")
System.release_software_component("SSD", "Windows")
System.release_software_component("SSD", "Unix")
System.release_software_component("HDD", "Test")
System.release_software_component("HDD", "Test3")
print(System.system_split())
