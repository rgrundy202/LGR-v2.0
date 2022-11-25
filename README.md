# LGR-v2.0

## Summary
This project represents an updated version of the Rangers Goal horn (See [LGR-v1.0](https://github.com/rgrundy202/LGR-v1.0)). It is currently in the process of being rewritten from the Arduino language to the more versatile, and most importantly object oriented, language of Python. The code will be implemented on a ESP8266 board running Micropython.

## Goals
The goal of this project is to create an internet connected device that will set off a horn and flash a bright light whenever the specified NHL team scores. The project will also display the current game staistics including period, time left, score, powerplay, and shots. These will be displayed on a small LCD. The code will be run on an ESP8266 module running micropython. 

## Construction
The main difference in terms of design from the previous version is the introduction of the game object. Using this object, all required data can be pulled faster and more orderly than in the previous project. The project has also been consolidated from two board to one, eliminating the need for the serial connection. See [LGR-v1.0](https://github.com/rgrundy202/LGR-v1.0) for more information.

