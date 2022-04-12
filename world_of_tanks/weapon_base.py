for_input = ('\n 1. 37 mm Gun M3 (37 mm, USA)\n'+
            ' 2. Ordnance QF 2-pounder (40 mm, UK)\n'+
            ' 3. 7.5 cm KwK 42 (75 mm, Germany)\n'+
            ' 4. M1932(19-K) (45 mm, Soviet Union)\n'+
            ' 5. 5 cm KwK 39 (50 mm, Germany)\n'+
            ' 6. Type 1 47 (47 mm, Japan)\n'+
            ' 7. AMX CN-105 F1 (105 mm, France)\n'+
            ' 8. KBA3 (125 mm, Ukraine)\n'+
            ' 9. 12.8 cm Pak 44 (128 mm, Germany)\n'+
            ' 10. 183mm Gun L4 (183 mm, UK)\n'+
            'Your choise is: ')

data_tank = {'model': input('Input name of your TANK: '),
             'weapon': input('Change gun for your TANK:\n'+ for_input),
             'type_of_armor': input('Input type_of_armor for your TANK from:\n' +
                                    ' 1. HArmor\n 2. CArmor\n 3. SArmor\n'+
                                    '\n 4. More about armors\nYour choise: '),
             'thickness': int(input('Input thickness of armor for your TANK: \n'))
            }

weapons = {
    '1': {'Name': '37 mm Gun M3', 'caliber': 37, 'gun_length': 210,
        'APCartridge': 'APCartridge for TNSh',
        'HECartridge': 'HECartridge for TNSh',
        'HEATCartridge': 'HEATCartridge for TNSh',},
    '2': {'Name': 'Ordnance QF 2-pounder', 'caliber': 40, 'gun_length': 208,
        'APCartridge': 'APCartridge for Ordnance QF 2-pounder',
        'HECartridge': 'HECartridge for Ordnance QF 2-pounder',
        'HEATCartridge': 'HEATCartridge for Ordnance QF 2-pounder',},
    '3': {'Name': '7.5 cm KwK 42', 'caliber': 75, 'gun_length': 525,
        'APCartridge': 'APCartridge for 7.5 cm KwK 42',
        'HECartridge': 'HECartridge for 7.5 cm KwK 42',
        'HEATCartridge': 'HEATCartridge for 7.5 cm KwK 42',},
    '4': {'Name': 'M1932(19-K)', 'caliber': 45, 'gun_length': 207,
        'APCartridge': 'APCartridge for M1932(19-K)',
        'HECartridge': 'HECartridge for M1932(19-K)',
        'HEATCartridge': 'HEATCartridge for M1932(19-K)',},
    '5': {'Name': '5 cm KwK 39', 'caliber': 50, 'gun_length': 210,
        'APCartridge': 'APCartridge for 5 cm KwK 39',
        'HECartridge': 'HECartridge for 5 cm KwK 39',
        'HEATCartridge': 'HEATCartridge for 5 cm KwK 39',},
    '6': {'Name': 'Type 1 47', 'caliber': 47, 'gun_length': 253,
        'APCartridge': 'APCartridge for Type 1 47',
        'HECartridge': 'HECartridge for Type 1 47',
        'HEATCartridge': 'HEATCartridge for Type 1 47',},
    '7': {'Name': 'AMX CN-105 F1', 'caliber': 105, 'gun_length': 280,
        'APCartridge': 'APCartridge for AMX CN-105 F1',
        'HECartridge': 'HECartridge for AMX CN-105 F1',
        'HEATCartridge': 'HEATCartridge for AMX CN-105 F1',},
    '8': {'Name': 'KBA3', 'caliber': 125, 'gun_length': 600,
        'APCartridge': 'APCartridge for KBA3',
        'HECartridge': 'HECartridge for KBA3',
        'HEATCartridge': 'HEATCartridge for KBA3',},
    '9': {'Name': '12.8 cm Pak 44', 'caliber': 128, 'gun_length': 702,
        'APCartridge': 'APCartridge for 12.8 cm Pak 44',
        'HECartridge': 'HECartridge for 12.8 cm Pak 44',
        'HEATCartridge': 'HEATCartridge for 12.8 cm Pak 44',},
    '10': {'Name': '83mm Gun L4', 'caliber': 183, 'gun_length': 450,
        'APCartridge': 'APCartridge for 83mm Gun L4',
        'HECartridge': 'HECartridge for 83mm Gun L4',
        'HEATCartridge': 'HEATCartridge for 83mm Gun L4',},
}