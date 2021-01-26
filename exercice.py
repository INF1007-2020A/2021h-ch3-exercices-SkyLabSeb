#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math

def square_root(a: float) -> float:
    a = a ** (1/2)

    return a


def square(a: float) -> float:
    a = a ** 2

    return a


def average(a: float, b: float, c: float) -> float:
    moyenne = (a + b + c) / 3

    return moyenne


def to_radians(angle_degs: float, angle_mins: float, angle_secs: float) -> float:
    angle_rad = (angle_degs + (angle_mins / 60) + (angle_secs / 3600)) * (math.pi/180)
    #test

    return angle_rad


def to_degrees(angle_rads: float) -> tuple:
    return 0.0, 0.0, 0.0


def to_celsius(temperature: float) -> float:
    temperature = (temperature - 32) * 5 / 9

    return temperature


def to_farenheit(temperature: float) -> float:
    temperature = (temperature * 9 / 5) + 32

    return temperature


def main() -> None:
    print(f"La racine carré de 144 est : {square_root(144)}")

    print(f"Le carré de 12 est : {square(12)}")

    print(f"Moyenne des nombres 2, 4, 6: {average(2, 4, 6)}")

    print(f"Conversion de 100 degres, 2 minutes et 45 secondes en radians: {to_radians(100, 2, 45)}")
    
    degrees, minutes, seconds = to_degrees(1.0)
    print(f"Conversion de 1 radian en degres: {degrees} degres, {minutes} minutes et {seconds} secondes")

    print(f"Conversion de 100 Celsius en Farenheit: {to_farenheit(100.0)}")
    print(f"Conversion de 451 Farenheit en Celsius: {to_celsius(451.0)}")


if __name__ == '__main__':
    main()
