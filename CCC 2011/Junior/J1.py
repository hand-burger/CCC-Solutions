number_of_antennas = input('How many antennas?\n')
number_of_eyes = input('How many eyes?\n')

if int(number_of_antennas) >= 3 and int(number_of_eyes) <= 4:
    print('TroyMartian')
if int(number_of_antennas) <= 6 and int(number_of_eyes) >= 2:
    print('VladSaturnian')
if int(number_of_antennas) <= 2 and int(number_of_eyes) <= 3:
    print('GraemeMercurian')