Title: Assignment 2
Template: 720

##Introduction

In [Assignment 1](assignment1.html), you learned how to get data from
the Internet and visualize it. In this assignment, you'll use your
newfound Javascript skills to interact with your Photon; you'll
also learn a bit of microcontroller programming in C.


##Goals
The main goal for this assignment is to get comfortable with the idea
and process of sending data back and forth from a physical object (the
Photon) to a computer. You'll do this via USB and/or the Particle cloud.

The learning goals for this assignment are as follows:

* Learn how to connect external components to your Photon;
* connect your Photon to your computer for two-way communication over
	USB or the cloud;
* and become more experienced with Javascript.

##What to do
You're going to connect some extra electronics to your Photon. Have a
look at the [list of parts](parts.html) that are available to see what
you can choose from. In addition, you can order extra parts if you
want from [Sparkfun](http://sparkfun.com),
[Adafruit](http://adafruit.com) or other places; note that "my parts
didn't arrive" is not a valid excuse for unfinished work, though.

Look at the Resources section below. There are a lot of useful links
to help you there. Also be sure to check out the Resources on [the
main page](index.html).

**Start now!** This is a more complex assignment than the first one.
I'm here to help but have limited time, so it's in your best interest
to run into problem earlier rather than later!

###C-level work
1. Attach a simple sensor to your Photon (for example, the light sensor).
2. Print data out over the serial port.
3. Visualize the data using either your visualization tool from the
	 first assignment (adapted and possibly improved) or another method.

In order to complete this assignment, **you will need the
supplementary files linked to in the Resources section!**

You'll be graded, in part, on the quality of your visualization; so if
you were unhappy with how your first assignment came out, this is your
chance to improve it.

###B-level work
1. Do the C-level work. Add a second sensor, visualize it too, and
	 improve the visualization to be more interesting/creative than a
	 simple line graph.
2. Adapt it to work _additionally_ with the cloud
(using, e.g., `Spark.publish()`). This means:
	- your B-level code should send data over the serial port _and_ use
		the cloud-based mechanism;
	- and you should have **two** kinds of visualizations, one which visualizes
		the serial port data and one which visualizes the cloud data.
		_(Note that the visualizations can be identical, just pulling from
		different data sources. They can be two separate files or you can
		have one file which displays both or allows the user to switch
		between the data sources.)_

###A-level work
1. Do the C-level work and the B-level work.
2. Add an output to your Photon. This could be as simple as an LED
	 (note the LED lesson in Resources) or as complex as the [Serial
	 OLED display](https://www.sparkfun.com/products/13003).
3. Have your output react to your computer, via the USB serial port
	 _or_ via the cloud (e.g. via
	 [`Spark.subscribe()`](https://docs.particle.io/reference/firmware/photon/#spark-subscribe-)
	 and [event
	 publishing](https://docs.particle.io/reference/api/#publish-an-event)).
	 It can react independently to some computer- or online-based event
	 or to the sensors attached to the Photon. In the latter case,
	 however, the data must leave the Photon to the computer or cloud
	 before it returns to cause a reaction.

##Deliverables
You'll turn in your code via your Github repository. Along with your
code, upload a Readme.md file, which Github will then display with
your repository. Include:

- A description of your circuit: what sensor you used, how you are
	reading the data from the circuit on the Photon.
- A description of your visualization: what libraries or techniques
	you used, and what differences (if any) there are from your code in
	the first assignment.
- A photograph of your completed circuit, clearly showing all of the
	elements and their connections. Annotations would be nice but are
	not required.

You will also demo your work in class.

##Tips
###Network problems
If you can't get your Photon connected to the network, you can skip
that part and use it unconnected. There's more information
[here](https://docs.particle.io/support/troubleshooting-support/photon/#device-mode-switching),
but the short version is to add the line
`SYSTEM_MODE(SEMI_AUTOMATIC);` at the top of your `.ino` file. This
will allow your code to run right away without trying to connect to
the Internet. (Obviously any cloud functions such as
`Spark.publish()` won't work if you use this solution!)

##Resources
###Software
- [Supplementary files](https://github.com/hcin720-fall15/IA2) to help
	with connecting between your local USB port and your web browser.
- If you want to send JSON back and forth from your Photon, check out
	the [SparkJson library](https://github.com/menan/SparkJson), which is
	included in Particle Build.
- A guide on [getting started with your
	Photon](https://docs.particle.io/guide/getting-started/start/photon/)
	from Particle.

###Learning about electronics
- Sparkfun is a great electronics supplier. They have some very nice
	resources for getting started with understanding hardware:
	- [What is Electricity?](https://learn.sparkfun.com/tutorials/what-is-electricity)
	- [Voltage, Current, Resistance, and Ohm's Law](http://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law)
	- [What is a circuit?](http://learn.sparkfun.com/tutorials/what-is-a-circuit)
	- [Metric Prefixes](https://learn.sparkfun.com/tutorials/metric-prefixes-and-si-units)
	- [How to Use a Breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)
	- [How to Use a Multimeter](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter)
	- [Connector Basics](https://learn.sparkfun.com/tutorials/connector-basics)
	- [Polarity](https://learn.sparkfun.com/tutorials/polarity)
	- [Series and Parallel Circuits](https://learn.sparkfun.com/tutorials/series-and-parallel-circuits)
	- [AC vs DC current](https://learn.sparkfun.com/tutorials/alternating-current-ac-vs-direct-current-dc)
- Sparkfun also has a nice-look set of [Photon
	projects](https://learn.sparkfun.com/tutorials/sparkfun-inventors-kit-for-photon-experiment-guide/all).
- Adafruit also has many useful tutorials, especially under the
	[Arduino category](https://learn.adafruit.com/category/learn-arduino?guide_page=2)
	- Including a nice lesson about
	[LEDs](https://learn.adafruit.com/adafruit-arduino-lesson-2-leds/leds)
- [Bildr](http://bildr.org) is a fantastic resource for doing lots of
	things with electronics and Arduinos. For example, they have a great
	tutorial on [hooking up a light
	sensor](http://bildr.org/2012/11/photoresistor-arduino/).
