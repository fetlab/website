Title: Using your Photon
Template: 720

##Introduction to Photons

- What do they do?
	- Explain general microcontroller concepts
		- Tiny computers
		- Very fast for certain things
		- Very, very low power
	- Explain Arduino
		- Standardized language (C++-based, called "Wiring")
		- Many, many libraries to make things easier
		- Lots of help online
		- Programs called "sketches"
	- Recap previous examples of Photon products

##Claiming a Photon

- Assuming you've installed the Particle CLI:
	- Plug in your Photon via USB.
	- Hold down the "Setup" button until the LED flashes blue.
	- In the terminal, type `particle identify`.
	- You'll see something like `Your device id is
		123456789abcdef123456789`. Copy the device id.
	- Now visit [build.particle.io](https://build.particle.io), make an
		account, and sign in.
	- Look for the gear icon <span class="fa fa-cog"></span> in the
		bottom left corner, then find the icon right above it (if you
		hover your mouse over it, it will say "Devices"). Click on that.
	- Click "Add new device" then put in the id you copied.
	- Now this Photon is associated with you and you will be able to do
		cool cloud stuff with it.


##Hello world flash LED

Here's a simple Arduino sketch to blink the LED on the Photon:

```.c
#define led D7

void setup()
{
	pinMode(led, OUTPUT);
}

void loop()
{
	digitalWrite(led, HIGH);
	delay(500);
	digitalWrite(led, LOW);
	delay(500);
}
```

Explain the parts.

##Hello world 2 flash LED from web

The Photon is extra cool because we can control it from the Internet!
Here's a version where we can turn on and off the LED via the web:

```.c
#define led D7

void setup()
{
	pinMode(led, OUTPUT);
	Spark.function("led", toggle_led);
}

void loop()
{
	//Do nothing here
}

void toggle_led(String command)
{
	if(command == "on")
	{
		digitalWrite(led, HIGH);
		return 1;
	}
	if(command == "off")
	{
		digitalWrite(led, LOW);
		return 0;
	}
	return -1;
}
```

##Other Photon tutorials

See the [Photon
Guide](https://docs.particle.io/guide/getting-started/examples/photon/)
for lots of annotated examples of how you can do stuff with the
Photon!

##How breadboards work

Check out [Sparkfun's breadboard
guide](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)!

##Flash external LED

Check it at [Photon LED flashing
guide](https://docs.particle.io/guide/getting-started/examples/photon/#blink-an-led)

##Electricity concepts

Check out [Sparkfun's electricity
guide](https://learn.sparkfun.com/tutorials/voltage-current-resistance-and-ohms-law/all)

##Connecting stuff

Let's connect a sensor!

##Debuggind with the oscilloscope

Handy! Confusing!
