Title: Introduction to Javascript
Template: 720
Extrahead: <script src="/js/paper-full.min.js"></script>

[TOC]

##Basics
Let's start with our browser debugger. If you're using Firefox, look
in Tools <i class="fa fa-long-arrow-right"></i> Web Developer <i class="fa
fa-long-arrow-right"></i> Web Console; if you're on Chrome, look under the
"<span class="fa fa-bars"></span>" menu <i class="fa
fa-long-arrow-right"></i> More tools <i class="fa
fa-long-arrow-right"></i> JavaScript Console.

Javascript has a C-like syntax, which is also similar to Java. Try
these things:

```.javascript
3
"hello"
var x = 5
console.log("hello")
console.log(x)
x + 7
```

###Hello World
Let's do the classic "write a function to print 'hello world'"
exercise!

```.javascript
var hello = function()
{
  console.log("hello world!");
}
```

##Variables
We should always declare variables with `var`. If we do it without,
we end up with a global variable, which can be a problem! Unlike other
languages, even inside a function if you don't use `var` your variable
becomes global! This is bad (see my page on [Javascript
pitfalls](javascript_pitfalls.html) for more).

##Objects
Almost everything in JS is an object. The only exceptions are:
numbers, strings, `true`/`false`, `null`, and `undefined`. Objects are
a containers with properties, which have names and values. 

There are no classes in Javascript. There's a way to do inheritance, though,
which can be pretty confusing, so we won't talk about it now.

Objects look like Python dicts (sort of) or Java HashMaps. Let's make
an object:

```.javascript
var hello = {}
hello.car = 'honda'
hello.year = 1957
hello
```

Objects can have their properties accessed by a dot or with brackets:

```.javascript
hello.year
hello['year']
```

If we try to access nonexistent properties we get `undefined`:

```.javascript
hello['color']
```

Arrays are objects, too:

```.javascript
rit = ['Rochester', 'Institute', 'of', 'Technology']
```

They use numbers for accessors:

```.javascript
rit[0]
```

They can have any object inside:

```.javascript
hci = ['Human', 42, rit, hello]
```

Let's make a more complicated object:

```.javascript
var flight = {
  airline: "Oceanic",
  number: 815,
  departure: {
    IATA: "SYD",
    time: "2004-09-22 14:55",
    city: "Sydney"
  },
  arrival: {
    IATA: "LAX",
    time: "2004-09-23 10:42",
    city: "Los Angeles"
  }
};
```

This is interesting because it's also something that's used for
data compatibility!

**Switch to JSON slides**

##Functions
Functions are objects too! They're "first class", meaning they
are just values that can be passed around. For example:

```.javascript
var hello = function() { console.log("hello world") }
hello()
hello2 = hello
hello2()
```

##Callbacks
Putting a function into a variable allows us to do "callbacks". Here's
a simple example:

```.javascript
var done = function(what)
{
  console.log("The function " + what + " is done!");
}
var doSomething = function(callback)
{
  var now = new Date().getTime();  //What time is it now?
  while(new Date() < now + 1000) {}; //Delay 1 second; don't do this in real code!
  if(callback)  //Will be undefined if nothing was passed
    callback("doSomething");
}

doSomething(done);
```

We can also drop our `done` function in as an anonymous function.
Instead of assigning the function to a variable, we just put it in as
the argument for the callback:

```.javascript
doSomething(
  function(what)
  {
    console.log("The function " + what + " is done!");
  }
);
```

Callbacks are used a lot in Javascript, for example with timers.

##Timers
The correct way to set a delay is using the `setTimeout()` function (I
used the `while()` loop above for simplicity):

```.javascript
var timeoutCallback = function()
{
  console.log("Timeout over");
};

window.setTimeout(timeoutCallback, 1000);
```

This calls the `timeoutCallback` function after 1000 milliseconds, or
1 second.

We can call a function repeatedly as well:

```.javascript
var intervalCallback = function()
{
  console.log("Beep!");
};

var intervalID = window.setInterval(intervalCallback, 1000);
```

This calls the `intervalCallback` **every** 1000 milliseconds, until
we cancel it with

```.javascript
window.clearInterval(intervalID)
```

Callbacks are also used quite often in libraries, such as...

##jQuery

It's a handy library that does a lot of good stuff for us. It also
helps to illustrate why functions-as-objects is super handy!

###$ ?
For ease of typing, jQuery represents itself as `$`. Let's try it:
make a new HTML file called `jquery_test.html` that looks like this:

```.html
<html>
  <head>
    <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
  </head>
  <body>
    <div id="hello">
      Hello
    </div>
  </body>
</html>
```

Load that up in your browser and open the Javascript console. Now type
`$` and hit enter. Depending on your browser, you'll see any of:

- `function m()` (Firefox)
- `function m(a, b)` (Chrome)
- `function m(a, b) {return new m.fn.init(a,b);}` (Safari)

The point being that `$` actually refers to something real!

###Changing the page
jQuery makes it easy to change the page. Try these things in the
Javascript console:

```.javascript
$('#hello')
$('#hello').text()
$('#hello').text("Goodbye")
$('#hello').append(" cruel world")
$('#hello').after('<h1>Hello!</h1>')
```

The `#` symbol is a CSS selector that refers to the `id` parameter in
the HTML. If we had instead done `<div class="good">` we could use a
period `.` to refer to everything with class `good`: `$('.good')`.

###jQuery and Ajax
Ajax is a way of grabbing data from somewhere else. Let's go back to
our `jquery_test.html` file and add some scripting. Change your file
to look like this:

```.html
<html>
  <head>
    <script src="http://code.jquery.com/jquery-1.11.3.min.js"></script>
    <script>
      $.ajax({
          url: "https://data.sparkfun.com/output/YGV3jNvQMjh2G4oOLwdx.json",
          dataType: "jsonp",
          data: {page: 1},
          success: function( response ) {
              $('#results').text(JSON.stringify(response[0])); // server response
          }
      });
    </script>
  </head>
  <body>
    <pre id="results">
    </pre>
  </body>
</html>
```

##Paper.js
Paper.js is a fun library to do graphical stuff! It has a "language"
all of its own called "Paperscript" which is actually Javascript with
a bit of extra stuff on top to simplify things. The
[tutorials](http://paperjs.org/tutorials/) are really handy.
