import yaml
# from data import *

class ConfigSetting:
    def __init__(self):
        pass
    
    def read_file(self):
        with open('./data/config_setting.yml', 'r') as file:
            prime_service = yaml.safe_load(file)
        print('Power limit ',prime_service['power_limit'])
        print('Voltage limit ', prime_service['voltage_LN_limit'])
        print('Temperature limit ', prime_service['temperature_limit'])
    
    def write_file(self, power, voltage, temperature):
        data = dict(
            power_limit = int(power),
            voltage_LN_limit = int(voltage),
            temperature_limit = int(temperature),
        )
        with open('./data/config_setting.yml', 'w') as file:
            yaml.dump(data, file, default_flow_style=False)