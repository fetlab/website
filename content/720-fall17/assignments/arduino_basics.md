Title: Arduino
Template: 720
Date: 2017-09-19

In this assignment, you'll learn the basics of Arduino hardware and
programming.

---

[TOC]

## Learning objectives
The goal of this assignment is to get started being comfortable with
simple electronics. We'll hook up some parts to our microcontroller
and get an idea of how it all works.

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
resources. Pleae ensure that you _thoroughly_ understand what it is
that you are doing. We'll be continuing to use our Photons throughout
the semester, so getting familiar and understanding the principles is
a must! It can be tempting to copy some useful code without completly
understanding how it works, but this will cause you problems later on.
As usual, the warning on the syllabus regarding [academic integrity,
cheating, and attribution](../syllabus.html#academic-integrity)
applies.

## What to do
Your overall goal is to use the parts in your Maker Kit to construct a
circuit and a simple Photon program that take some input from the
world and produces some output.

### Setting up the Photon
The [Particle
Photon](https://www.particle.io/products/hardware/photon-wifi-dev-kit)
is an amazing little board with incredible wireless capabilities that
we'll be using throughout the course. To start with, though, we're
going to disable that WiFi functionality and learn some basics of
microcontrollers.

First, visit [build.particle.io](http://build.particle.io) and create
an account. We won't use this page again for a while, but you'll need
your password.

Next, we'll need to be able to talk to the Photon through USB ports.

If you use Windows, follow the instructions in [Connecting your Device
over
USB](https://docs.particle.io/guide/getting-started/connect/photon/).

If you use MacOS, life will be a lot easier if you install Homebrew.
Go [here](https://brew.sh/) and follow the instructions to install.
Next, at the command prompt, do `brew install npm dfu-util`.

Finally, for both Windows and Mac, do `npm install -g particle-cli`
and then `particle login`, logging in with the username/password you
created above.

### Compiling and flashing code
Here's a quick intro to getting code onto your Photon; you'll learn
more about this in detail with the readings below.

On the command line, type `particle project create`. Give your project
a name and note where it got saved. Now, open up that directory, look
inside `src`, and, using your favorite text editor[^1], open up the `.ino`
file. Replace the contents of that file with the following:

```.c
SYSTEM_MODE(MANUAL);

void setup()
{
  pinMode(D7, OUTPUT);
}

void loop()
{
  digitalWrite(D7, HIGH);
  delay(500);
  digitalWrite(D7, LOW);
  delay(500);
}
```

Now, back in the console, change to the directory that your project
folder is located in. Type `particle compile photon
<your_project_name_here>`. It will do some stuff, then will output a
filename something like `photon_firmware_1505237346558.bin`.

Finally, let's flash this to your Photon. Put your Photon into [DFU
Mode](https://docs.particle.io/guide/getting-started/modes/photon/#dfu-mode-device-firmware-upgrade-)
and then type `particle flash --usb photon_firmware_<number>.bin`. If
all goes well, your Photon should restart and start flashing a blue
light.

[^1]: If you don't have one, some people like [Sublime
	Text](https://www.sublimetext.com/). Be careful using things like
	Windows Notepad or Mac OS TextEdit because they may not treat plain
	text correctly or might add odd extensions to the filename.

### Learning
Read the following Photon resources:

- [Photon: working with projects and libraries](https://docs.particle.io/guide/tools-and-features/cli/photon/#working-with-projects-and-libraries)
- [Photon: device modes](https://docs.particle.io/guide/getting-started/modes/photon/)
- The "Blink an LED" example at [Photon: annotated examples](https://docs.particle.io/guide/getting-started/examples/photon/)

Read the following circuitry resources:

- [Electricity primer](electricity.pdf) (from [Richard
	Squier](http://people.cs.georgetown.edu/~squier/) at Georgetown
	University; [original link](http://people.cs.georgetown.edu/~squier/Teaching/ComputerSystemsArchitecture/520-2013-CourseDocuments/Lec-1-electricityPrimer.pdf))
- [What is a Circuit?](https://learn.sparkfun.com/tutorials/what-is-a-circuit)
- [How to Use a Breadboard](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)
- [How to use a Multimeter](https://learn.sparkfun.com/tutorials/how-to-use-a-multimeter)
- [Polarity](https://learn.sparkfun.com/tutorials/polarity)
- [Series and Parallel Circuits](https://learn.sparkfun.com/tutorials/series-and-parallel-circuits)
- [How to Read a Schematic](https://learn.sparkfun.com/tutorials/how-to-read-a-schematic)

Check the following out for reference purposes:

- [Metric Prefixes and SI Units](https://learn.sparkfun.com/tutorials/metric-prefixes-and-si-units)
- [Connector Basics](https://learn.sparkfun.com/tutorials/connector-basics)
- [Alternating Current vs Direct Current](https://learn.sparkfun.com/tutorials/alternating-current-ac-vs-direct-current-dc)

### Helpful links
- [Particle Maker Kit contents and
	info](https://docs.particle.io/datasheets/particle-shields/#photon-maker-kit-contents)
- [Particle Photon language
	reference](https://docs.particle.io/reference/firmware/photon/)
- [Arduino language
	reference](https://www.arduino.cc/en/Reference/HomePage) (better
	organized than Photon's)
- [How to build a vibration motor
	circuit](http://learningaboutelectronics.com/Articles/Vibration-motor-circuit.php)
- [AdaFruit Arduino
	tutorials](https://learn.adafruit.com/series/learn-arduino)

### Assignment
Your Maker Kit has several components that can serve as input devices:
photoresistors, a potentiometer, temperature sensors, buttons,
switches, and a PIR sensor. It also has a number of output devices: a
piezo buzzer, LEDs, an RGB LED, a vibration motor, a servo, and an
OLED display.

Your goal for this assignment is to use two or more of the input
devices to get some properties about the world into your Photon, process
them somehow, and then display those properties with the output
devices.

Your basic assignment is to use the light sensor and four LEDs to
display the light level from 0--100%, and use the potentiometer to
change the light threshold at which the vibration motor will vibrate.

Once you have that going, you can start switching out components if
you like, or changing how the system's code operates.

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
forth (for example, the AdaFruit tutorials linked above include many
helpful items relevant to this project).

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

### Bonus points
You will get 1 extra point on your final grade if you do all of the
above---including documentation---and then change your circuit
significantly to include at least one different input, one different
output, and a different functionality.

##Footnotes
