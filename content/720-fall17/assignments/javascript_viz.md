Title: Javascript visualization
Template: 720
Date: 2017-10-05

For this assignment, you'll learn to use a Javscript visualization
library to show data in nice-looking ways.

---

[TOC]

## Learning objectives
We'll eventually be using our Photons to send data to the internet to
use it later, but first we'll be getting data _from_ the internet.
It's convenient to be able to look at that data in a nice way, so our
very first step is to be able to visualize it. In this assignment,
you'll be learning your way around the [Paper.js](http://paperjs.org)
web graphics library.

## Deliverables

## Getting set up
### Learning
Paper.js is a great library, but---like many useful things---it has a
bit of a learning curve. As usual, it's best to go through some
tutorials. First, go through the following tutorials on the [Paper.js
tutorial page](http://paperjs.org/tutorials/):

- Getting Started: Working with Paper.js
- Geometry (all)
- Paths (all)
- Projects & Items: Working with Items

Then take a look at [this
walkthrough](http://andyshora.com/easy-paper-js-tutorial.html) which
shows a number of very simple things you can do.

Finally, have a look at the [Paper.js
examples](http://paperjs.org/examples/), and note that you can view
the source by clicking in the upper-right corner.

### Set up for local development
Your web browser wants to keep you safe. One way it does this is by
preventing random web pages from accessing files on your computer.
This is usually a good thing! But for this assignment, it's a little
annoying because you'll be reloading your test page _a lot_ and
loading Javascript files every time from somewhere else can get
annoying fast.

In order to do this assignment, you'll need to install a local web
server. You already have `npm` installed from the Arduino basics
assignment, so we can use it to install a web server, too. Simply open
up a terminal and type `npm install -g http-server`.

Now, do these things:

1. Pick a folder on your computer where you want to put your project.
1. Save the following files to the folder you chose (right-click,
	 Save):
	- [paper-full.js](https://cdnjs.cloudflare.com/ajax/libs/paper.js/0.11.4/paper-full.js)
	- [perlin.js](https://raw.githubusercontent.com/josephg/noisejs/master/perlin.js)
	- [paper_example.html](/720/files/paper_example.html)
	- [paper_example.js](/720/files/paper_example.js)
1. Open the terminal and change into that directory.
1. Type `http-server` and hit return. You'll see something like this:

        Starting up http-server, serving ./
        Available on:
        	http://127.0.0.1:8080
        	http://192.168.0.6:8080
        Hit CTRL-C to stop the server	

1. Copy one of those links and paste it into your web server, and add
	 `/paper_example.html` to the end, so you might have
	 `http://127.0.0.1:8080/paper_example.html`.
1. When you hit enter, you should see the example paper visualization
	 I made. It's ugly! If it doesn't load, ask for help.

### Understand the example
Click [this link](/720/files/paper_example.html) to see the example
running.

Now have a look at the `paper_example.html` and `paper_example.js`
files and understand what's going on in them. The basic idea is that
every 10 milliseconds or so, the `myDraw()` function is called with a
semi-random value (generated via a [Perlin
noise](https://en.wikipedia.org/wiki/Perlin_noise)-like function).
Later, we'll use real data instead of noise.

## What to do
Your goal is simple: modify the code in the example files to make your
own visualization. Pretending that the code is receiving "real" data, 
you should use Paper.js to visualize this data in an interesting,
attractive, creative, and/or fun way.

The requirements are:

- Visualize the semi-random data using Paper.js. This can be via a
	graph or something more abstract.
- Your visualization should be **significantly different** from my
	example. My example is provided _only as an example_ that I wrote in
	15 minutes and yours should be significantly nicer and more
	interesting.
- Update the visualization in realtime as new data is provided.

Feel free to calculate properties such as the rate of change,
positive/negative-ness, or so on, and visualize those instead or in
addition to the raw data.

You can use extra files, extra libraries, rename functions, and so
forth.

As usual, be _very clear_ about attribution, including the resources
you used for learning.

## Turning in
Please zip up your files, including `paper-full.js` and name the zip
file according to the usual convention:
`{{page.filename|rmext}}-<yourname>.zip`. I should be able to unzip
this file, run a local webserver, and open your `.html` file and see
your visualization. You might want to test this out in a different
directory to ensure it works.

## Grading

See the [syllabus](/{{page.roots[0]}}/syllabus.html) for how much this
assignment contributes to your final grade. The grade for this
assignment is determined as follows:

- Working visualization (60%)
- Updates in realtime (10%)
- Works when I unzip your file (5%)
- Significantly different visualization from example (15%)
- Attractive/creative (10%)
