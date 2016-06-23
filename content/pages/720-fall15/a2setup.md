Title: Assignment 2 Setup
Template: 720

##Goals
The goal for this task is to get more comfortable with your Photon,
and to get it set up and working reliably with your computer for local
programming and debugging.

###Grading
You'll get credit for following these instructions and being prepared
in class. You'll lose credit for not being ready to be hands-on in
class.

**Note:** Some people weren't ready last time. I'm going to be lenient
for that one, but this time I _will_ deduct points for failing to have
everything set up! So: start now, and if you are having problems, post
to [Slack](using_slack.html) right away.

##Connecting your Photon
If you got your Photon working with your computer in class (that is,
if you were able to type `particle identify` and get an answer),
great! Otherwise, get it working.

If you are using Windows, it turns out you need to install a driver.
[Here are
instructions](https://docs.particle.io/guide/getting-started/connect/photon/#installing-the-particle-driver).

##Install Particle Dev
Particle Dev is a program for writing code on your computer, so you
don't have to save all of your programs in the cloud. This step is
optional; you can also use your favorite text editor. If you'd like to
install Particle Dev, you can get a version for your operating system
[here](https://www.particle.io/dev)[^1].

##Local programming
Getting local compiling working is tricky and beyond the scope of
this class (you can read all about it
[here](https://learn.sparkfun.com/tutorials/photon-development-guide/arm-gcc-and-the-dfu-bootloader-offline)
if you want to try); but you can compile remotely and flash[^2]
locally using the `particle` utility.

First, you need some code on your computer. Using Particle Dev or your
favorite text editor, make a new directory called `blinky` and put a
file called `blinky.ino` into it with the following content:

```.c
void setup()
{
	pinMode(D7, OUTPUT);
}
void loop()
{
	digitalWrite(D7, HIGH);
	delay(1000);
	digitalWrite(D7, LOW);
	delay(1000);
}
```

Now switch to your command prompt, and run `particle compile photon
<path to your blinky folder> --saveTo blinky.bin`[^3]. This command
will compile your code remotely on Particle's servers and print
something like

```
Including:
    /private/tmp/f/blinky/blinky.ino
attempting to compile firmware
pushing file: /private/tmp/f/blinky/blinky.ino
grabbing binary from: https://api.particle.io/v1/binaries/55edacf78cc997bb1824a88f
Compile succeeded.
Saved firmware to: /private/tmp/f/blinky.bin
```

Now you're going to flash that code to your Photon over USB. Plug your
Photon into your computer and set it to DFU[^4] mode:

1. Hold down BOTH buttons
2. Release only the RESET button, while holding down the SETUP button.
3. Wait for the LED to start flashing yellow (it will flash magenta first)
4. Release the SETUP button

When it's flashing yellow, it's ready to accept code over USB. Now
you'll type `particle flash --usb blinky.bin`.
You'll see a bunch of stuff printed out, which hopefully includes
`File downloaded successfully`. You might also see a bunch of
meaningless errors (see Troubleshooting below).

At this point, your Photon should reboot, try to connect to the
Internet, and start flashing the D7 LED once per second.

##Debugging over USB
It's useful to be able to see some information about what's going on
with your program. Let's print out every time the LED turns on or off.
First, change your `blinky.ino` file to the following:

```.c
void setup()
{
	pinMode(D7, OUTPUT);
	Serial.begin(9600);
}
void loop()
{
	digitalWrite(D7, HIGH);
	Serial.println("Turned LED on!");
	delay(1000);
	digitalWrite(D7, LOW);
	Serial.println("Turned LED off!");
	delay(1000);
}
```

Now follow the procedure we did above, starting with the button
sequence to get it into DFU mode with the flashing yellow LED (here
I'm assuming I'm in the same directory as the `blinky` folder):

```
particle compile photon blinky --saveTo blinky.bin
particle flash --usb blinky.bin
```

Assuming that worked, now let's look at the output. The easiest way is
to:

1. Open up Particle Dev
2. Click on the USB icon at the bottom left of the screen
3. Find the port that your Photon is connected to (on Mac it will look
	 like `/dev/cu.usbmodem1234`)
4. Click "Connect"

On Linux (and on Mac if you didn't install Particle Dev) you can type
`screen /dev/tty...`.

You should now see `Turned LED on!` and `Turned LED off!` being
printed repeatedly.


##Troubleshooting
###dfu-util errors
If you get the errors

```
File downloaded successfully
dfu-util: Error during download get_status

Error writing firmware...dfu-util: Invalid DFU suffix signature
dfu-util: A valid DFU suffix will be required in a future dfu-util
release!!!

dfu-util: Error during download get_status
```

don't necessarily worry. The "`File downloaded successfully`" part is
the good bit, and the other errors are bugs in the code uploader.

[^1]: If you're running Linux, you can get instructions
	[here](https://github.com/spark/spark-dev#linux).
[^2]: Meaning to put the code you wrote on your Photon.
[^3]: Handy tip: on Mac, you can drag the folder from the Finder into your
	Terminal window and it will put in the path for you!
[^4]: "Device Firmware Update"---find an animated gif of the procedure
	[here](https://docs.particle.io/guide/getting-started/modes/photon/#dfu-mode-device-firmware-upgrade-)

###Flashing magenta
If you end up with a problem where your Photon doesn't seem to want to
take the code, and every time you flash it reboots and just blinks
magenta (purple), try this:

1. Put the Photon into DFU mode (flashing yellow)
2. Run `particle update`
3. Try again

##Footnotes
