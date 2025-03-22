import yaml
# from data import *

class ConfigService:
    def __init__(self):
        pass
    
    def read_file(self):
        with open('./config/config_service.yml', 'r') as file:
            data = yaml.safe_load(file)
        # print('Power limit ',prime_service['power_limit'])
        # print('Voltage limit ', prime_service['voltage_LN_limit'])
        # print('Temperature limit ', prime_service['temperature_limit'])
        return (
            data['resistor_settings']['r1'], data['resistor_settings']['r2'], data['resistor_settings']['r3'], 
            data['resistor_settings']['r4'], data['resistor_settings']['r5'], data['resistor_settings']['r6'],
            data['resistor_settings']['r7'], data['resistor_settings']['r8'], data['resistor_settings']['r9'],
            data['resistor_settings']['r10'], data['resistor_settings']['r11'], data['resistor_settings']['r12'],
            data['resistor_threshold_allow']['min'], data['resistor_threshold_allow']['max'],
            data['emergency_settings']['current_limit'], data['emergency_settings']['voltage_LN_limit'],
            data['emergency_settings']['temperature_limit']
        )
    def read_file2(self):
        with open('./config/config_service.yml', 'r') as file:
            data = yaml.safe_load(file)
        # print('Power limit ',prime_service['power_limit'])
        # print('Voltage limit ', prime_service['voltage_LN_limit'])
        # print('Temperature limit ', prime_service['temperature_limit'])
        return [
            data['resistor_settings']['r1'], data['resistor_settings']['r2'], data['resistor_settings']['r3'], 
            data['resistor_settings']['r4'], data['resistor_settings']['r5'], data['resistor_settings']['r6'],
            data['resistor_settings']['r7'], data['resistor_settings']['r8'], data['resistor_settings']['r9'],
            data['resistor_settings']['r10'], data['resistor_settings']['r11'], data['resistor_settings']['r12'],
            data['resistor_threshold_allow']['min'], data['resistor_threshold_allow']['max'],
            data['emergency_settings']['current_limit'], data['emergency_settings']['voltage_LN_limit'],
            data['emergency_settings']['temperature_limit']
        ]
        

    
    def write_file(self, r1, r2, r3, r4, r5, r6, r7, r8, r9, r10, r11, r12, min, max, current, voltage, temperature):
        data = dict(
            resistor_settings = dict(
                r1 = float(r1),
                r2 = float(r2),
                r3 = float(r3),
                r4 = float(r4),
                r5 = float(r5),
                r6 = float(r6),
                r7 = float(r7),
                r8 = float(r8),
                r9 = float(r9),
                r10 = float(r10),
                r11 = float(r11),
                r12 = float(r12),
            ), 
            resistor_threshold_allow = dict(
                min = int(min),
                max = int(max)
            ),
            emergency_settings = dict(
                current_limit = int(current),
                voltage_LN_limit = int(voltage),
                temperature_limit = int(temperature)
            )
        )
        with open('./config/config_service.yml', 'w') as file:
            yaml.dump(data, file, default_flow_style=False)