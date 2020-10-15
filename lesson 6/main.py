from cars import Passenger_Car
from ships import Sailboat
from planes import Airplane
from exceptions import LightsAlreadyOnError
from parts import CarEngine, Bumper

if __name__ == '__main__':
    vwpolo = Passenger_Car('VW Polo', 1_740, 6.2)
    print('Created:', vwpolo, 'with sound ', end='')
    vwpolo.beep()
    vwpolo.bumper = Bumper(1234)
    print('bumper installed)')
    vwpolo.engine = CarEngine(1400, 4, 7000)
    vwpolo.engine.start()
    print('engine started')
    print('try to turn lights... ', end='')
    vwpolo.turn_lights_on()
    print('done')
    try:
        print('try to turn lights again...')
        vwpolo.turn_lights_on()
    except LightsAlreadyOnError:
        print('oops, lights already on')
    finally:
        vwpolo.turn_lights_off()
    print('can drive for 250km: ', vwpolo.can_drive_for_distance(250))
    print('fill ip 20 litres')
    vwpolo.fill_up(20)
    print('can drive for 250km: ', vwpolo.can_drive_for_distance(250))

    speedboat = Sailboat('Cayman 75 HT', 32_000, 52_000)
    print('Created:', speedboat, 'with sound ', end='')
    speedboat.beep()

    plane = Airplane('Boeing 777-200', 139_225, 13_140)
    print('Created:', plane, 'with sound ', end='')
    plane.beep()
