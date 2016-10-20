Title: Assignment 3
Template: 720

##Introduction
In [Assignment 1](assignment1.html), you learned about online data and
visualizations. In [Assignment 2](assignment2.html), you took your
skills further and incorporated some hardware for some basic
interaction. Now in this assignment, you'll take the final step in
your basic learning and look at how to create an appealing enclosure
for your work.

##Goals
The main goal for this assignment is to become comfortable with
designing for 3D printing and laser cutting and to learn how to use
the equipment. The learning goals for this assignment are as follows:

- Learn how to use [TinkerCAD](https://tinkercad.com) for 3D modeling
- Learn how to evaluate the printability of 3D models
- Learn how to use a 3D printer
- Learn how to use [Inkscape](http://inkscape.org) or Adobe Illustrator
	for 2D design for laser cutting
- Learn how to use the laser cutter
- Learn how to measure existing objects and incorporate those
	measurements into models


##What to do

###C-level work
Design and fabricate a case for your electronics for IA 2. Do this via
either 3D printing or laser cutting. It should enclose the components
and expose the interaction elements (and you may want to include a way
to easily get to the buttons).

###B-level work
Do the C-level work; then do it again for the other fabrication
method. That is, if you made a case with the laser cutter, make
another one on the 3D printer; if you made one on the 3D printer, make
another with the laser cutter. Alternately, make a single case that
combines in some interesting way elements from both the laser cutter
and the 3D printer.

Make _one_ of your cases work with an
existing physical object in the environment. For example, you might
add a part to your model to allow your Photon to attach to a light
switch cover.

###A-level work
Do the B-level work. On _one_ of the cases, incorporate into your case
an extra input or output element **not previously existing** in your IA 2
project. For example, add a servo for motion or an LED for output.
Some part of the case must be involved in the I/O mechanism:
a servo might move some piece, an LED could 
[side light](https://www.google.com/search?q=laser+etch+side+light&tbm=isch)
something.

##Deliverables
You'll turn in your model files via your Github repository. Along with your
files, upload a Readme.md file, which Github will then display with
your repository. Include a description of your case, the techniques
you used, and any special features (in the case of A-level). Also
include a photo or a short video.

You will also show your work in class.


##Setup and learning
###Laser cutting
Install [Inkscape](http://inkscape.org) or use a lab machine with Adobe
Illustrator on it. If you have another 2D design program you really
like, you are welcome to use it instead.

####Inkscape
1. Create a new document
2. Go to File -> Document Properties
3. Under the Page tab, change Default units to "in"
4. Under "Custom Size" on the Page tab, change Units to "in", Width to
   32 and height to 18
5. Close the Document Properties window
6. In the toolbar, find the set of icons that look like
	 <img src="/files/720/inkscape-scale1.png" width="100px">.
	 Click the leftmost icon to turn it off, so it looks like
	 <img src="/files/720/inkscape-scale1.png" width="100px">.
	 This operation disables the defaul behavior of scaling the width of
	 an object's line when you change the size of the object.

####Illustrator
1. Go to File -> New
2. In the New Document window, change the Units to "Inches", Width to
	 32 in and Height to 18 in
3. Open the Advanced area
4. Change Color Mode to RGB

####Selecting cut vs raster
The laser cutter works via a print driver. This is good, because it
means that you don't have to use a particular program. This is bad,
because you have to set strange settings in your programs.

The laser cutter's default behavior is to raster, or engrave. Even
vectorized lines will be in raster mode by default. For every line in
your design that you want to cut rather than raster, you must do two
things.

1. First, you must set the line color to 100% red. It must be
	 exactly RGB (255, 0, 0). This is why in Illustrator you must set the
	 color mode to RGB instead of CMYK.
2. Second, you must set the line to be equal to or less than 1,000th
	 of an inch thick, or <= .001 inches. 

When the laser cutter gets a line that looks like this, then it will
cut it with the power level you instruct in the print control panel.

###3D printing
Visit [TinkerCAD](https://tinkercad.com) and create an account (or
login with your existing Autodesk account). If you have another 3D
modeling program you like that can export STL files, you are welcome
to use it.

##Resources
Here are some useful links:

- A [good guide](http://www.saic.edu/media/saic/pdfs/campusresources/instructionalshops/aoc_laserguide.pdf)
	for using a laser cutter very similar to ours.
- [The manual for the laser cutter in the FETLab](https://trello-attachments.s3.amazonaws.com/558cae29a54e147c3dd34942/55a9499af759d51516da6cbb/f3577a243608f44135922920b535b445/VLS_Platform_User_Guide.pdf).
- My [Tips Trello board](https://trello.com/b/JuxwmQhn/tips) with more
	useful links for laser cutting and 3D printing.

There are many, many, many other sources of information for laser cutting
and 3D printing. Here are a few:

- [Laser Cutting Tutorials Tips](http://support.ponoko.com/forums/345641-Laser-Cutting-Tutorials-Tips)
- [So you've opened Inkscape for the first time ever](http://support.ponoko.com/entries/20235788-So-you-ve-opened-Inkscape-for-the-first-time-ever)
