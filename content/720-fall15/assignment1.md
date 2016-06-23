Title: Assignment 1
Template: 720

Check the sidebar to see when this assignment is due.

##Introduction
We'll be talking a lot in this class about connecting resources on the
Internet to resources in the world. We're going to go step-by-step,
and to begin with, we'll look at resources on the Internet. There is a
vast quantity of data available out there, from
[weather data](http://www.ncdc.noaa.gov/cdo-web/webservices/v2) to
[stock data](https://developer.yahoo.com/finance/) to
[wave reports for surfing](http://www.spitcast.com/api/docs/). To
start your explorations, and to get you up to speed, you're going to
look at how to access and visualize this data.

Much of the public data available on the Internet is exposed via [web
APIs](https://en.wikipedia.org/wiki/Representational_state_transfer#Applied_to_web_services).
web stands for "REpresentational State Transfer", and is a way of
exposing information to developers via HTTP calls. To call a web API,
one simply loads a URL; the result of the URL is the result of the API
call.

A simple example of a web API call is the following URL:
[http://jsonplaceholder.typicode.com/posts/1]([http://jsonplaceholder.typicode.com/posts/1]).
When you click on
it, you'll get a result that looks like this:

~~~~.javascript
{
  "userId": 1,
  "id": 1,
  "title": "sunt aut facere repellat provident occaecati excepturi optio reprehenderit",
  "body": "quia et suscipit\nsuscipit recusandae consequuntur expedita et cum\nreprehenderit molestiae ut ut quas totam\nnostrum rerum est autem sunt rem eveniet architecto"
}
~~~~

This is JSON, which is directly usable in Javascript.

##Goals
The main goal for this assignment is to get you comfortable with using
Javascript to visualize data available on the web. To do this, you
will connect to a public API that provides a datastream and visualize
that datastream in realtime.

The learning goals of this assignment are as follows:

* Get an environment set up to experiment with web APIs
* Learn how to use git and Github
* Understand how to call web APIs and work with the data
* Understand how to visualize data with Javascript

We're going to use a lot of modern web development tools and practices
in the class. A good article to read for an overview of these tools is
[The Modern Front-End Workflow - From Start to
Finish](http://blog.chartbeat.com/2014/01/30/modern-front-end-workflow-start-finish/)
(note that we won't necessarily use everything in the article!).

##What to do
Set up the stuff in the [Set up page](a1setup.html).

Your basic goal is to visualize a public datastream. We'll start with
[data.sparkfun.com](http://data.sparkfun.com) because it's easy. Visit
[this page](https://data.sparkfun.com/streams/dZ4EVmE8yGCRGx5XRX1W)
and have a look at the data - this is a weather station on top
of someone's house. You can see that it updates about once per minute.
You can also get this data in JSON format by clicking the JSON button
(or copying the link!); see the
[documentation](http://phant.io/docs/output/http/) for more
information.

###C-level work
Visualize at least two columns from the SparkFun weather station data
stream in a line graph (time on the _x_-axis). Display a scale for
the axes (e.g. ticks for time on the _x_-axis). Update the display
live, so it adds a new point when it gets new weather data.

###B-level work
Do the above task. Create a second, more creative visualization of the
data. This should be abstract and fun---the idea is to push your
skills and understanding.

###A-level work
Do the above two tasks, but rather than using the data source I
suggest, find and use another (potentially more interesting) web API
to use. Visualize this data. Your time-based graph should be really
solid and clear, and your abstract graph should be very interesting
and dynamic. You could use other/additional Javascript libraries (for
example, [three.js](http://threejs.org/) or
[matter.js](http://brm.io/matter-js/) ) if desired.

##Deliverables
You'll turn in your code via your Github repository. Along with your
code, upload a Readme.md file, which Github will then display with
your repository (this is Markdown; you can read [Github's
help](https://help.github.com/articles/markdown-basics/)). Include
information about the data source you chose to visualize, the
libraries you used, and links to your visualization(s). To do this
last one, navigate to your file in Github, select the "Raw" button,
then change
`https://raw.githubusercontent.com` to `http://rawgit.com`.

