Title: Design Exercise
Template: 720

<div class="image text-center" style="position:relative">
	<img src="/files/720/fang.jpg">
	<div class='text-left' style="position:absolute; top:235px; width:100%;
	padding-left:100px; background:rgba(255,255,255,.5)">
		<h2 style="color:red; font-weight:bold; font-size:60px; margin-top:0;
		text-shadow: -1px -1px 0 #000, 1px -1px 0 #000, -1px 1px 0 #000, 1px 1px 0 #000; margin-bottom:0">
		Fang</h2>
		<h3 style="margin-top:0; color:blue; font-weight:bold;
		font-size:20px;
		text-shadow: -1px -1px 0 #fff, 1px -1px 0 #fff, -1px 1px 0 #fff, 1px 1px 0 #fff; margin-bottom:0">
		home security systems</h3>
		<i style="font-size:18px;
		text-shadow: -1px -1px 0 #fff, 1px -1px 0 #fff, -1px 1px 0 #fff, 1px 1px 0 #fff; margin-bottom:0">
		with RabidBite&trade; technology</i>
	</div>
</div>

##Goal
Your are participating in the design of an IoT home security system.
The system&mdash;**Fang&trade;**&mdash;is an improvement on
traditional home security services. Instead of being installed by a
company that comes to the home, the user orders all of the necessary
components from Fang and installs and sets them up themselves.

Your job is to design the user experience around the system. There are
several parts to the system that must all work together: the sensors,
the hub that connects the sensors to the home network, the control
centers, the app, the cloud service, and the integration with other
IoT services.

###What to do
You'll divide into teams. Each team will handle one of the sections
below, producing:

- An overview storyboard of the customer's experience setting up,
	configuring, and using that part of the product;
- sub-storyboards including sketches of UI walkthroughs; and
- paper prototypes of particularly interesting or difficult sections
	of that part of the product.

##System Components
Here are each of the components of the system and its various parts.

###Hardware
The Fang system has user-deployed wireless sensors that help the
system detect break-ins or other activity. The sensors include:

- **Motion sensors** that mount on the wall in rooms or are placed on
	shelves. They use infrared technology to sense movement.
- **Window break sensors** that use microphones to listen for
	high-pitched noises that could indicate a window breaking.
- **Door/window open sensors** that have a magnetic switch inside to
	detect when a door has been opened or closed&mdash;including
	cabinets, closests, and cupboards.
- **Cameras** that the user can access remotely to monitor an area.

The system also has alarms:

- The super-loud **Snarl&trade; siren** that can be placed on a wall
	or shelf,
- and the Fang-exclusive **<i>RabidBite&trade;</i>** technology that
	immobilizes intruders with an automatically-aimed Taser shot.

Finally, there is the **WaterDish&trade;** hub that all of the sensors
and control panels connect to, which manages the entire system and
connects to Fang's **DogPark&trade;** cloud service.

Considerations for design include:

- How to help the user understand what sensors to put where;
- how to test the sensors (e.g. is the motion sensor covering the
	entire room?);
- how to easily connect the sensors to the WaterDish hub (since each
	component can be ordered separately) and ensure that the connection
	is reliable;
- how to indicate that a battery needs to be replaced;
- and how to work with the app to indicate which sensor is which for
	setting up different rules.

###Control panels
One of the user-facing components of the Fang system is the
**ShortLeash&trade;** control panel. Although normally the system is
controlled via the user's phone, ShortLeash panels can be placed near
entries so that the system can be controlled without a phone. The
panels also can sense when a user's phone goes out of range,
indicating they have left the house. The ShortLeash panels allow the
user to:

- arm and disarm the Fang system;
- enter **FrenziedBarking&trade;** panic mode, where the alarms go off
	and the system calls the police, fire station, ambulance, and SWAT
	team;
- and receive weekly **DogTraining&trade;** tips about home security upon 
	entering or leaving the house.

Considerations for design include:

- Quickly entring FrenziedBarking mode and disabling it if
	accidentally activated;
- easily arming and disarming the system, even with full hands or in
	the dark;
- easily allowing guest access;
- and re-displaying DogTraning tips.

###Phone application
The phone application has all of the capabilities of the ShortLeash
control panels; in addition, it allows the user to perform initial
setup of the system, including:

- configuring the location of each sensor and control panel;
- configuring the sensitivity of motion sensors to avoid triggering on
	pet movement;
- setting the system master password;
- adding authorized users, both permanent (e.g. family members) and
	temporary (e.g. dog sitting service);
- and configuring actions for different events (e.g. "when the window
	break sensor goes off, call the police" or "when the liquor cabinet
	is opened and Dad is not home, send a notification to Dad").

It also:

- provides notifications of sensor and alarm events,
- and allows the user to remotely monitor the house via the cameras.

Considerations for design include:

- Assisting with setup of hardware components;
- displaying locations of different sensors;
- configuring and displaying notifications and action rules;
- handling integrations (below).

###Integration
Fang integrates with other popular IoT devices and services:

- It can use the **Nest thermostat** as an additional motion sensor,
	and can tell Nest when the alarm system has been enabled so it can
	turn off the heat or A/C;
- it can provide notifications from the **Nest smoke detector**, as
	well as calling the fire department if the action is configured;
- it integrates with **Philips Hue** light bulbs so that lights can be
	automatically turned on as part of action rules;
- and Fang can be controlled via the **Amazon Echo** with voice
	commands such as "Alexa, ask Fang about the bedroom window sensor"
	or "Alexa, tell Fang to RabidBite the intruder in the living room!"
