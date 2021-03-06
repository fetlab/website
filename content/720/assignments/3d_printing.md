Title: Fusion 360/3D printing
Template: 720
Date: 2017-09-12

For this assignment, you'll install and start learning Autodesk Fusion
360, a free (for us!) professional-level 3D modeling program.

---

[TOC]

## Learning objectives
The idea behind this assignment is to introduce you to 3D modeling and
get you comfortable with the idea of designing for 3D printing.

## Deliverables
See the notes below for details on each deliverable, including how to
turn them in, as well as for grading criteria.

1. An **interesting** design for a **wearable object** that is
	 **three-dimensional** and **3D-printable**. Please note
	 the particular requirement under [Turning in](#turning-in) of
	 adding your name to the design file.
2. The object you designed **printed out** on a 3D printer.
3. Several high-quality **photographs** of your printed object from
	 different angles.

## What to do
### Installation
First, you'll need to install Fusion. Visit the [page for
education](https://www.autodesk.com/products/fusion-360/students-teachers-educators)
to find out what to do; you'll have to create an account. Problems?
Discuss on [Slack](using_slack.html)!

Next, follow the instructions [on this
page](https://knowledge.autodesk.com/support/fusion-360/learn-explore/caas/sfdcarticles/sfdcarticles/How-to-change-the-orientation-of-the-origin-planes-in-Fusion-360.html)
to set the default modeling orientation to make 3D printing easier.
(You'll need to make a new file after you do this to make it work.)

Other programs you will want to install are
[Meshmixer](http://www.meshmixer.com/) and
[LulzBot Cura](https://www.lulzbot.com/cura).

### Setting up Cura
We'll set up three different printers in Cura for the three printers
in the lab.

#### LulzBot Mini
1. Start Cura; It will ask you which kind of printer you have.
1. Select "LulzBot Mini". Click Next.
1. Select "Standard LulzBot Mini". Click Finish.

#### LulzBot Taz 4
1. From the "Machine" menu, select "Add new machine".
1. Select "LulzBot TAZ 4 or 5". Click Next.
1. Select "Stock TAZ 4 (PET & v1)". Click Finish.

#### Qidi X-One
1. Save [this file](/720/files/Qidi_X_One_Profile.ini) to your
	 computer.
1. From the "Machine" menu, select "Add new machine".
1. Select "Other Printers". Click Next. 
1. On the next screen, with the list of printers, select "Other (Ex:
	 RepRap, MakerBot, Witbox)". Click Next.
1. On the next screen, select "julia". click Next.
1. Click Finish.
1. Select the Machine menu, then "Machine settings".
1. Change the following three settings to **150**:
	- "Maximum width (mm)"
	- "Maximum depth (mm)"
	- "Maximum height (mm)"
1. Ensure that the "Heated bed" checkbox is activated.
1. Click "Change machine name" and change the name to "Qidi X-One".
1. Click "Ok".
1. From the "File" menu, select "Open Profile". Select the
	 `Qidi_X_One_Profile.ini` file you saved earlier.

### Learning
Now, you'll need to learn how to use Fusion.

- Watch and follow along in tutorials:
	- At [Learn Fusion 360 in 60 Minutes](http://help.autodesk.com/view/fusion360/ENU/),
		watch at least:
		- Foundational Concepts ([captioned](/720/files/Foundation-Captioned.mov))
		- Sketch ([captioned](/720/files/Sketch-Captioned.mov))
		- Model ([captioned](/720/files/Model-Captioned.mov))
	- [Fusion 360 for Beginners Webinar](https://www.youtube.com/watch?v=gu7Nm0ygaow&t=1501s) ([captioned](/720/files/Fusion 360 for Beginners Webinar-Captioned.mov))
	- [Designing an Arduino Uno Enclosure with Fusion 360](https://www.youtube.com/watch?v=E0bhdr84FNU) ([captioned](/720/files/Arduino-Captioned.mov))
- Text-based help is also available at the Fusion 360 help site; a
	good place to start is [Getting to Know Fusion
	360](http://help.autodesk.com/view/fusion360/ENU/?guid=GUID-1C665B4D-7BF7-4FDF-98B0-AA7EE12B5AC2).

### Design assignment
Your goal is to design something that you can 3D print that is
wearable. The thing you design must adhere to the following
requirements.

- 3D-printable:
	- your design should be informed by the things we discussed in class
		about what makes an object able to be printed or not; and
	- your actual printed object should be essentially identical to your
		design (that is, the features in the design you turned in should
		show up in the object you turn in).
- Three-dimensional: your design and printed object should not be
	something that would be (easily) producable on the laser cutter, but
	should take full advantage of the 3D printer's ability to make 3D
	objects.
- Wearable: your design must be something wearable. It can strap on
	your wrist, hang around your neck, slip on your finger, go through a
	buttonhole, clip on your pocket, hang from your ear, or be wearable
	in some other way.
- Interesting and/or creative: don't turn in something that you spent
	10 minutes on. I'll be able to tell! Use your creativity---get
	inspired by objects online or in the world.

### Printing
You should print your design to turn in. You'll want to do some test
prints early to ensure that you are able to print your object, and to
avoid a rush to the printers as the deadline approaches.

Here are some tips for printing:

- Pay attention to overhangs. As we discussed in class, too much
	overhang will cause your print to fail. We also talked about methods
	to check _before you print_ whether you have too much overhang; for
	example, Meshmixer will analyze the amount of overhang you have.
- Check the slice preview. By using the "Layers" view option in Cura,
	you can look at the layers of your print job---make sure it looks
	correct!
- Check the estimated time. Cura isn't very good at estimating time to
	print, but it can give you a rough lower bound; multiplying by 1.5
	or 2 will give you a better idea. Make sure your print job isn't
	going to take 8 hours! If it is, try making your object smaller or
	using less infill.

#### Saving an STL file from Fusion 360
In order to print your object, you'll need to send it to Cura. First,
in Fusion, select the "Make" button in the toolbar. This should bring
up a little window labeled "3D print". It defaults to being in
selection mode; you will need to select the object(s) you want to
print. The easiest method is to open the "Bodies" folder on the left
and select your object that way.

Make sure that the "Send to 3D Print Utility" box is _not_ checked.
Click "OK" and you'll be able to save the file.

#### Using Cura
In Cura, you can click the "Load Model" button to load your STL file.
It will automatically slice the model for you; you can click the "View
Mode" button in the upper-left to change to the "Layers" view. You can
also change to "Overhang" view to see an analysis of overhang.

Once you're ready to print, select the "Save gcode" button and save
the `.gcode` file.

#### Printing
To print on the Qidi, you'll need to get the SD card from the left
side of the printer and put your file on it. When you put the card
back in, **note that it goes in upside-down!** Then navigate through the
menu to find your `gcode` file and print.

To print on the LulzBot printers, you'll use a web interface. The
LulzBot Mini's site is [http://129.21.24.150/](http://129.21.24.150/)
and the Taz 4's site is [http://129.21.24.150:8080/](http://129.21.24.150:8080/).
You'll need to login; the username and password are the same for both
printers and are on a label stuck to the Mini's frame.

Once you log in, you can upload your `.gcode` file with the blue
"Upload" button on the bottom left. It will appear in the list of
files above that button; you can then select the tiny button that
looks like a printer (<span class="fa fa-print"></span>) next to the
file, which should load the file and start printing. The "Control" tab
will show the camera view of the printer.

### Photographing

Take and turn in several high-quality photographs (not crooked, in
focus) illustrating how your design is worn.

## Turning in
You'll show your final output object in class on the due date. You
should turn in your photographs and design file via direct message to
me in Slack by 1:59 pm on the due date.

To turn in your design file, you will do two things. You will
add your name to the file, and you will export it.

To add your name to the file, go to the Sketch drop-down menu and
select "Text". Then pick a plane and click it. Type your name. Save
the file.

To export, follow the instructions
[here](https://knowledge.autodesk.com/support/fusion-360/troubleshooting/caas/sfdcarticles/sfdcarticles/How-to-make-a-local-archive-back-up-file-in-Fusion-360.html)
for generating a `.f3d` file. Rename it according to the instructions
below and send it to me in a direct message.

Please name your files `{{page.filename|rmext}}-<yourname>.<ext>`,
replacing `<yourname>` with your name and `<ext>` with your file
extension. For example, `{{page.filename|rmext}}-dan.jpg`. If you have
more than one file of a type, please add a number, as in
`{{page.filename|rmext}}-dan01.jpg`.


## Grading

See the [syllabus](/{{page.roots[0]}}/syllabus.html) for how much this
assignment contributes to your final grade. The grade for this
assignment is determined as follows:

- Printable: printed object looks very close to design (20%)
- 3D: design/object is actually 3D (20%)
- Wearable: object is wearable (20%)
- Creativity: design is interesting/creative (30%)
- Photos: photos are good-quality and show how design is wearable (10%)
