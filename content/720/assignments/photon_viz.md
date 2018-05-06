Title: Photon + visualization
Template: 720
Date: 2017-10-19

In this assignment, you'll combine your knowledge of Arduino,
Javascript, and the Photon to visualize some data from the real world.

---

## Setup

Get the helper code from [this zip
file](https://github.com/hcin720-fall15/IA2/archive/update2017.zip).
After you unzip it, change into that directory and run `npm install`.

Now put this code on your photon:

```.cpp
SYSTEM_MODE(MANUAL);

void setup() // Put setup code here to run once
{
	Serial.begin(9600);
	pinMode(D7, OUTPUT);
}

void loop() // Put code here to loop forever
{
	//Print two random comma-separated values to Serial
	Serial.print(random(0,100));
	Serial.print(",");
	Serial.println(random(0,100));  //Note this is println, not print

	if(Serial.available())
	{
		int i = Serial.parseInt();
		if(i % 2)
			digitalWrite(D7, HIGH);
		else
			digitalWrite(D7, LOW);
	}
	delay(500);
}
```

Now plug your Photon in and run `node server.js`. Visit
[http://localhost:3000](http://localhost:3000) and see if it works!

If that works, the next step is to load
[http://localhost:3000/paper.html](http://localhost:3000/paper.html)
and see if that works. You can look at `paper_example.js` to see what
it's doing.

## Tips

- Any time you flash your Photon, you'll need to restart the server by
	pushing `CTRL-C` then running `node server.js` again. Otherwise it
	won't be connected to the serial port.
- You can have multiple web pages connected to the server at the same
	time and they will all get the same data. They'll all also send the
	same data to your Photon. So watch out!
- For this assignment, you don't need the code in the
	`if(Serial.available())` section of the example. Unless you'd like
	to experiment!

## What to do

This assignment, you'll update your Paper.js code to visualize sensor
data from your Photon. Visualize both of your sensors in combination.
The requirements are:

- Visualize the data from both of your Photon sensors using Paper.js.
	This can be via a graph or something more abstract.
- Your visualization can be essentially the same as with your last
	assignment, or you can do something new; you just need to make it
	make sense with both sensors.
- Update the visualization in realtime as new data is provided.

Feel free to calculate properties such as the rate of change,
positive/negative-ness, or so on, and visualize those instead or in
addition to the raw data.

You can use extra files, extra libraries, rename functions, and so
forth.

As usual, be _very clear_ about attribution, including the resources
you used for learning.

## Turning in
You'll show your final output object in class on the due date. You
should turn in your photographs and files via direct message to
me in Slack by 1:59 pm on the due date.

Your video file should clearly illustrate your circuit working in
conjunction with your visualization. Get a
friend to hold your phone or put it on a tripod so you can use both
hands to demonstrate. You should write your full name on a piece of
paper and have that at least at the beginning of the video.

Turn in a top-down photo of your circuit with the parts labeled.

Please zip up your files, including `paper-full.js` and name the zip
file according to the usual convention:
`{{page.filename|rmext}}-<yourname>.zip`. I should be able to plug in
your Photon, unzip this file, run `server.js`, and open your my web
browser and see your visualization. You might want to test this out in
a different directory to ensure it works.

Finally, compose a [Slack
Post](https://get.slack.help/hc/en-us/articles/203950418-Compose-a-post)
with details about how your circuit works. Also include a list of
resources you used: major places you found help, examples, and so
forth (for example, the AdaFruit tutorials linked above include many
helpful items relevant to this project).

## Grading
See the [syllabus](/{{page.roots[0]}}/syllabus.html) for how much this
assignment contributes to your final grade. The grade for this
assignment is determined as follows:

- Circuit works with two sensors (40%)
- Visualization visualizes both sensors (40%)
- Video is clear and includes your name (5%)
- Photo is clear and labeled (5%)
- Documentation is clear and describes circuit (10%)
