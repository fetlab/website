Title: Assignment 2
Template: 720
NoRightSidebar: True

[TOC]

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
* learn basic C skills;
* and become more experienced with Javascript.

##Grading
This assignment counts for 33% towards your final grade. It also
includes an extra 5% credit towards your final grade if you do really
great. The grading for this assignment will be in two parts. First 25%
of the assignment (or 8.25% of your final grade) is based on you
showing up in class with the things requested in **[Important
dates](#important-dates)** below.  The remaining 90% is assigned
based on your completed work, under **[Evaluation](#evaluation)##[^1].

[^1]: Yes, this adds up to 115%. 100% of 33% is 33%; 15% of 33% is
about 5%, which is the extra credit. I'm doing it like this, rather
than assigning extra credit to a particular class, to give you more of
a chance to get a good grade overall.

##Important dates
For this assignment, we'll have several quick check-in points to help
you know what to do when. Each one will be due in class, and we will
troubleshoot problems. The procedure will be:

1. Everyone will show me what they have and very briefly bring up
	 about any problems they ran into.
1. After everyone has talked, we will troubleshoot common and simple
	 problems.
1. Then we'll go on to trickier problems.
1. _If_ there is time, we'll talk about the milestone for next time.
	 If not, you need to be independent and be prepared anyway.

Being prepared with each of these deadlines will form part of your
grade for this assignment.

<table class="table table-condensed">
	<tr>
		<th style="width:15%">Date</th>
		<th>Points</th>
		<th>Thing to do by this date</th>
	</tr>
	<tr><td>Thu 9/29 </td><td>5%</td><td>Pick one input and one output part from parts list</td></tr>
	<tr><td>Tue 10/4 </td><td>5%</td><td>Design your circuit and sketch your program flow; <a href="#get-chrome-serial-working">get Chrome serial working with demo program</a></td></tr>
	<tr><td>Thu 10/6 </td><td>5%</td><td>Wire up your input circuit on the breadboard and have working basic input code as illustrated by serial output via <code>particle serial monitor</code></td></tr>
	<tr><td>Tue 10/11</td><td>&mdash;</td><td>Classes on Monday schedule; extra office hours during class time</td></tr>
	<tr><td>Thu 10/13</td><td>5%</td><td>Wire up output circuit on the breadboard</td></tr>
	<tr><td>Tue 10/18</td><td>5%</td><td>Working basic output code</td></tr>
	<tr><td>Thu 10/25</td><td>90%</td><td>Rest of assignment due:<br>
	<i>Input visualization  (35%)<br>
	Output visualization (35%)<br>
	Extra I/O            (15%)<br>
	Deliverables         ( 5%)</i></td></tr>
</table>


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


###Steps
####Pick parts
Visit the [list of parts](parts.html) and pick one input and one
output part you'd like to work with. Be sure to click on links for the
parts you're interested in and read about them, especially any
connection guides associated with them. Adafruit parts often have
comprehensive tutorials, and Sparkfun parts often have hookup guides.
Take into account the complexity of hooking up the part, the amount of
programming necessary, and whether there are extra components needed.

Note that for both input and output, I would like to see more than
binary. That is, if you're going to use a button or switch for input,
you should have several, and if you're going to use an LED for output,
you should have several.

####Design circuit
Plan what your circuit will look like. Draw it on paper or use
[Fritzing](http://fritzing.org/home/). It doesn't have to be amazing
or pretty---the idea is for you to think about what you're going to do
before you start plugging things in. If you like, draw two versions,
one for the input and one for the ouput. Think about whether you
will have the right number of connections on your Photon to accomplish
what you want to do.

####Plan program
Plan how your program will work. Sketch out the general flow of what
it will do. Look up what libraries you will need and read about how
they work.

####Wire up and test input
Wire up the input part of your circuit on your breadboard.
Double-check your connections against your plan.

Write a program for your Photon to read your input and print the data
out over the serial port (use `particle serial monitor` to see the
output once the program is running). See if it works.

####Wire up and test output
Take a photo or two of your working input circuit so you can recreate
it later if you accidentally break something. Wire up the output part
of your circuit on your breadboard. Double-check your connections
against your plan.

Write a program for your Photon to generate some output. At this
point, don't try to combine it with the input program. See if it
works.

####Get Chrome + Serial working
You'll need to be sure that your Photon is sending some stuff over the
serial port. You can check the [Particle Reference Documentation for
serial
ports](https://docs.particle.io/reference/firmware/core/#serial) for
more information. Here is a very basic program that will print a
random number to the serial port once per second, while flashing the
onboard blue LED so you know the program is running:

```.c
//A #define statement is like a variable that doesn't need to change.
// I'm using it here so I can easily change which LED is flashing
// later; for example, if I hooked up an LED to D0, I could just make
// one change here.
#define LED D7

//Here I'll define how long (in ms) it should be between flashes of the LED
#define LED_FLASH_TIME 500

//And how long in between printing to the serial port
#define SERIAL_PRINT_TIME 1000

void setup()
{
	//Set up the Photon to talk over the USB serial port. 9600 is how
	// fast your Photon will communicate over the serial port. You don't
	// need to change it. You'll notice this value used in the Chrome
	// serial code, though.
	Serial.begin(9600);

	//Set up the LED for ouput
	pinMode(D7, OUTPUT);
	
	//Make sure the LED starts in the off state
	digitalWrite(LED, LOW);
}

//Keep track of how long it's been since we last did stuff
unsigned long timeSinceLastFlash = 0;  //How long since we flashed LED?
unsigned long timeSinceLastPrint = 0;  //How long since we last printed?

//Keep track of the current LED state
unsigned int ledState = LOW;

void loop()
{
    //The millis() function returns how many milliseconds since the
    // program started running. We'll use this instead of delay()
    // since delay() keeps the Photon from doing anything else.
    unsigned long now = millis();
    
    //If it's been more than 500ms since the last flash, we'll change
    // the LED state from off to on or from on to off.
    if(now - timeSinceLastFlash > LED_FLASH_TIME)
    {
        //"!" means "not", so we switch the value of ledState to its
        // opposite value
        ledState = !ledState;
        digitalWrite(LED, ledState);  //Set the new state
        timeSinceLastFlash = now;     //The last change was just now
    }
	
    if(now - timeSinceLastPrint > SERIAL_PRINT_TIME)
    {
    	//Print a random number between 0 and 1024 to the serial port
    	Serial.print("Random number: ");
    	Serial.println(random(1024));
    	timeSinceLastPrint = now;
    }
}
```

Follow the instructions in Step 5 at [this
page](https://developer.chrome.com/apps/first_app#five) to get your
copy of Chrome set up for app development. Then, visit [this GitHub
repository](https://github.com/hcin720-fall16/chrome-serial) and
follow the instructions there to get serial port reading set up in
Chrome.


####Complete assignment
Now you should have the tools available to complete the assignment.
Read through the **Evaluation** section below to find out what to do.

##Evaluation
25% of your grade for this assignment will come from following the
instructions under **[Important dates](#important-dates)**. Note the
points for this assignment add up to 115%. This assignment is normally
worth 33% of your final grade, so if you do everything to reach 115%,
you'll get 5% extra credit towards your final grade.

###Input visualization (35%)
Visualize the data from your input sensor using either your
visualization tool from the first assignment (adapted and possibly
improved) or a new visualization method. You'll be graded, in part,
on the quality of your visualization; so if you were unhappy with how
your first assignment came out, this is your chance to improve it.

###Output visualization (35%)
Also display some data from the internet on your output. This can
react independently to some computer- or online-based event or to the
sensors attached to the Photon. In the latter case, however, the data
must leave the Photon to the computer or cloud before it returns to
cause a reaction. You can use any online data service such as
[data.sparkfun.com](http://data.sparkfun.com) or
[PubNub](https://www.pubnub.com/).

###Extra I/O (15%)
Add at least one extra non-binary input and one extra non-binary
output to your circuit. Make your circuit do something interesting
and/or useful (beyond just simply displaying the input).

###Deliverables (5%)
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

Ensure that your images appear inline with the Readme file when you
load up your repository.

You will also demo your work in class.

##Tips
###Problems?
Are you stuck? Confused? Sad? Enraged? _Please come see me!_ Or send
me a Slack message! I would much rather spend time with you figuring
out what's going on than have you turn in something that doesn't work.

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
- You might need to do multiple things at once on your Photon. Visit
	AdaFruit's tutorial on [Multi-tasking the
	Arduino](https://learn.adafruit.com/multi-tasking-the-arduino-part-1/)
	for many useful tips.
- A guide on [using
	IFTTT](https://docs.particle.io/guide/tools-and-features/ifttt/) with
	our Photon: simple triggers for events.
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
