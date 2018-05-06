Title: Photon components
Template: 720
Date: 2017-10-12

In this assignment, you'll practice connecting extra components to your
Photon.

---

[TOC]

## Learning objectives
In our [Arduino basics](/720/arduino_basics.html) assignment, you
learned how to add sensors (light and potentiometer) and actuators
(vibration motor and LEDs) to your Photon. Now you'll take it a step
further and gain more practice adding components, this time of your
choice!

The goal of this assignment is to get you more comfortable with
hooking up things to your Photon---later you'll be making
internet-connected devices and so you will want to be familiar with
different components to do so.

## Deliverables
See the notes below for details on each deliverable, including how to
turn them in, as well as for grading criteria.

1. A working circuit that takes input and creates output according to
	 the below instructions
1. A video, with your full name written on a piece of paper visible in
	 the beginning of the video, of your working circuit
1. A top-down photo of your working circuit with the parts clearly
	 labeled
1. The code you used in your circuit
1. A textual description (in a [Slack
	 Post](https://get.slack.help/hc/en-us/articles/203950418-Compose-a-post))
	 of your circuit and how it works, as well as a list of resources
	 you used in formulating your solution

### Advice/Warning
For this project, be extra careful about what you use from internet
resources. Please ensure that you _thoroughly_ understand what it is
that you are doing. We'll be continuing to use our Photons throughout
the semester, so getting familiar and understanding the principles is
a must! It can be tempting to copy some useful code without completly
understanding how it works, but this will cause you problems later on.
As usual, the warning on the syllabus regarding [academic integrity,
cheating, and attribution](../syllabus.html#academic-integrity)
applies.

## What to do
Your overall goal is to use parts in your Maker Kit, and in the lab,
to construct a circuit and a simple Photon program that takes some
input from the world and produces some output. You can use your
Arduino basics assignment as a basis for this one!

As in the Arduino basics assignment, your goal is to connect sensors
to your Photon as well as output devices. This time, you need to use
_different_ sensors and actuators than you did last time. So you can't
use the photoresistor or potentiometer as input, and you can't use a
set of LEDs and the vibration motor as output. If you did the extra
credit by adding other components, you may not use those for this
assignment either.

For the purposes of this class, I have a bunch of parts. You can find
out what all of the parts are on the [parts list](../parts.html). In
order to use these parts, you need to check them out from the cage,
which you can access through the back door of the lab. Just ask the
student workers for the part you need. Do this well in advance because
the parts are confusing and you might need help from me.

Your assignment, then is the following:

- Pick at least two sensors (input) and at least two actuators
	(output) from your Maker Kit or from the [parts list](../parts.html)
	_that you haven't used in a previous assignment_.
- Connect them to your Photon.
- Write code to make the two inputs and the two outputs work together.
	This means that there should be some linkage between the two inputs
	and the outputs; if you have inputs I1 and I2 and outputs O1 and O2,
	I don't want to see just I1→O1 and I2→O2; I want to see something
	similar to the first assignment, where a combination of the inputs
	affects the outputs. How this happens is up to you.

## Turning in
You'll show your final output object in class on the due date. You
should turn in your photographs and files via direct message to
me in Slack by 1:59 pm on the due date.

Your video file should clearly illustrate your circuit working. Get a
friend to hold your phone or put it on a tripod so you can use both
hands to demonstrate. You should write your full name on a piece of
paper and have that at least at the beginning of the video.

Turn in a top-down photo of your circuit with the parts labeled.

Turn in your code that you used for your project.

Finally, compose a [Slack
Post](https://get.slack.help/hc/en-us/articles/203950418-Compose-a-post)
with details about how your circuit works. Also include a list of
resources you used: major places you found help, examples, and so
forth.

Please name your files `{{page.filename|rmext}}-<yourname>.<ext>`,
replacing `<yourname>` with your name and `<ext>` with your file
extension. For example, `{{page.filename|rmext}}-dan.jpg`. If you have
more than one file of a type, please add a number, as in
`{{page.filename|rmext}}-dan01.jpg`.

## Grading
See the [syllabus](/{{page.roots[0]}}/syllabus.html) for how much this
assignment contributes to your final grade. The grade for this
assignment is determined as follows:

- Circuit works as instructed (60%)
- Code compiles without errors (20%)
- Video is clear and includes your name (5%)
- Photo is clear and labeled (5%)
- Documentation is clear and describes circuit (10%)
