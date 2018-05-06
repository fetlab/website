//Make a red rectangle to be the background
var background = new Shape.Rectangle(view.bounds);
background.fillColor = "Red";

//Create a new path to use for visualization
var path = new Path();
path.strokeColor = 'green';

//Add segments to the path to make it into a circle. I do this so that
// I can move the points later so the circle will get distorted.
for(var a = 0; a < 360; a += 10)
{
	var v = 50;
	var p = new Point({length: v, angle: a});
	path.add(p)
}

//Add the first point to the path so the circle is closed
path.add(path.segments[0]);

//Smooth the path so it looks a little nicer
path.smooth({ type: 'continuous' });

//Move the path so it's in the center of the screen instead of the
// corner
path.position += view.bounds.center;

//MyDraw() gets called by the code at the bottom of this file to
// simulate data coming from some online data source. Note that the
// timestamp parameter is in milliseconds. I'm not using it but you
// might want to.
var i = 0;
function myDraw(timestamp, val)
{
	//Values from the noise function are small so scale them up
	val *= 10;

	//They are positive or negative so we can just add to the length
	path.segments[i].point.length += val;

	//Be sure we loop around the circle
	if(++i >= path.segments.length)
		i = 0;

	//This part gives the path the hideous radial gradient. Setting it
	// every time ensures that the center of the gradient keeps in the
	// center of the shape.
	path.fillColor = {
			gradient: {
					stops: [['yellow', 0.05], ['red', 0.2], ['black', 1]],
					radial: true
			},
			origin: path.position,
			destination: path.bounds.rightCenter
	};
}

//This is the number of milliseconds between calls to myDraw().
var dataInterval = 10;

/* ---------- Don't change anything below this line! ---------- */

//Get the noise generating function from outside of PaperScript and
// set it up
var noise = window.noise;
noise.seed(Math.random());

//This function will get called about every dataInterval milliseconds,
// but only after the previous call has finished. (This is unlike
// window.setInterval() which would call myDraw() every dataInterval
// milliseconds regardless of whether the previous call to myDraw()
// was still doing stuff.)
var go = function()
{
	myDraw(Date.now(), noise.simplex2(Math.random(), Math.random()));
	window.setTimeout(go, dataInterval);
};
window.setTimeout(go, dataInterval);
