Title: Class 7 Electronics Notes
Template: 720

##How to read a circuit diagram

As usual, [Sparkfun has a great
tutorial](https://learn.sparkfun.com/tutorials/how-to-read-a-schematic)
on how to read a circuit diagram!

##How to read a datasheet

Let's pull up some datasheets for our various items. You'll see the
quality varies widely. These are all parts from your Sparkfun kit.

- [LED](https://www.sparkfun.com/datasheets/Components/LED/COM-00533-YSL-R531R3D-D2.pdf)
- [7-segment LED](https://cdn.sparkfun.com/datasheets/Components/LED/YSD-160AR4B-8.pdf)
- [555 timer](https://www.sparkfun.com/datasheets/Components/General/ne555.pdf)
- [Photoresistor](http://cdn.sparkfun.com/datasheets/Sensors/LightImaging/SEN-09088.pdf)

Things you'll often find in datasheets:

- Physical measurements of the device
- Amount of input voltage/current needed
- Amount of power it uses
- How to hook it up
- Information on how to use it in manufacturing
- Max/min temperature
- How it works inside

##How to find out how to hook up something

Find the part on [Sparkfun](http://sparkfun.com),
[Adafruit](http://adafruit.com), or elsewhere. Look for tutorials.
Look for comments. Search for libraries.

Example: [humidity and temperature
sensor](https://www.sparkfun.com/products/10167).

1. Visit [Sparkfun page](https://www.sparkfun.com/products/10167)
2. Check out the [datasheet](http://cdn.sparkfun.com/datasheets/Sensors/Weather/RHT03.pdf).
	 It looks awfully complex to communicate with.
3. Oh, some [sample code](http://www.sparkfun.com/datasheets/Sensors/Temperature/DHT22.doc).
	 Ugh.
4. Some [code on Github](https://github.com/sparkfun/RHT03/blob/master/Firmware/RHT03_Example/RHT03_Example.ino).
	 Looks possible.
5. Let's check out [the comments](https://www.sparkfun.com/products/10167)
	 section first.
6. Someone mentions an [Adafruit
	 library](https://github.com/adafruit/DHT-sensor-library). That
	 looks more promising.
7. Oops, how to hook it up? Back to the datasheet!
8. Wait, does Adafruit have any more information? [Yes, they
	 do!](http://www.adafruit.com/products/393). It's not the same part,
	 but some guy in the comments said they were basically the same.
	 Let's give it a try.
