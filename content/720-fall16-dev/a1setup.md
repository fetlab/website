Title: Assignment 1 Setup
Template: 720

##Goals
The goal for this task is to be ready to do the hands-on work in
class, and to be set up to do. You'll be doing the following:

- **Github:** getting set up with a Github account and software
- **Node:** installing and setting up node.js and associated
	Javascript development tools
- **Paper:** installing Paper.js, a Javascript graphics library
- **jQuery:** installing jQuery, a Javascript utility library

If you have problems with any of these steps, Google first, then ask
on [Slack](using_slack.html).

###Grading
You'll get credit for following these instructions and being prepared
in class. You'll lose credit for not being ready to be hands-on in
class.

##Github
Set up a [Github](http://github.com) account. You'll be turning in all
of your code for this class by posting it to Github. If you haven't
used Git before, you'll want to learn about it by reading [Git
Basics](http://git-scm.com/book/en/v2/Getting-Started-Git-Basics).
Github has available [Windows](https://windows.github.com) and
[Mac](https://mac.github.com/) GUIs that you can use rather than the
command line. (Note: if you already have a Github account but don't
want to use it, feel free to make a new one for the purposes of this
class.)

Once you have a Github account, set up a new repository for this
assignment. You'll turn it in by giving me the link to this
repository. I'd suggest starting to use this repository right away
while you work on this assignment.

**Note:** Because everything on Github is by default
publically-visible, you must be extra-careful about giving attribution
to code you didn't write yourself. If in doubt, double-check the
[syllabus](files/720/syllabus.pdf) for the attribution and plagiarism
policies.

##Node and Browserify
Install [Node](https://nodejs.org/download/), a tool for running
Javascript on your local machine (outside of the browser). Node is
very popular and quite powerful, and lets you do many things including
running a web server or controlling a robot.

Node comes with a package manager, npm; once you've got Node
installed, you can use npm to install different modules. For modules
you might use often you can use the `-g` option (for "global") to
install them once on your system; otherwise, the modules will be
installed in your current project directory. You use the modules with
the `require` statement (similar to `import` in Python):

~~~~.javascript
var awesomeModule = require("awesomeModule");
~~~~

Now all of the functionality of awesomeModule is available as the
variable `awesomeModule`.

Because Node is often used standalone (without a browser), there is an
extra step to be able to use Node modules with a web page. We need a
program called _Browserify_ which bundles up your code and all of the
necessary Node modules into a single file you can include in your web
page. You can install Browserify with `npm install -g browserify`.
While you're at it, install Watchify the same way: `npm install -g
watchify`. Watchify automatically runs Browserify anytime your file
changes, so you don't have to remember to.

To use these programs, you'll write all of your code in a single
Javascript file, using `require` as necessary to load different
modules. In a Terminal window, change directories to your project,
then run `watchify -d -v -o bundle.js yourfile.js` (where
`yourfile.js` is the name of your Javascript project file). Now, in
your main HTML file, include the generated file with `<script
src="bundle.js"></script>`.

##Paper
I recommend using [Paper.js](http://paperjs.org) for visualization.
It's a well-thought-out Javascript graphics library that has a lot of
good documentation and examples. It has a special Javascript extension
language called Paperscript which makes using it easier. In order to
take advantage of it, you'll want to _not_ use npm to install Paper,
but download it and install it from the site above, and include it in
your HTML file directly via `<script
src="paperjs-v0.9.23/dist/paper-full.js"></script>`. Read and work
through the Paper tutorials so you understand how to use it.

###Tips
* If you find that your graphics aren't showing up right away, try
	calling `view.draw()` to force an update.
* Chrome often has better performance. However, to use Paperscript,
	Paper has to load the Javascript file and process it. This means
	it's using Javascript to open local files, which Chrome prohibits.
	To get around this problem, start Chrome using the
	`--allow-file-access-from-files` argument. If you're on a Mac, open
	a Terminal and run `/Applications/Google\
	Chrome.app/Contents/MacOS/Google\ Chrome
	--allow-file-access-from-files &`; then you can close the Terminal
	window.

##JQuery
JQuery is a handy Javascript library that does lots of useful stuff.
Use npm to install it and include it with `var $ =
require('jquery');`. To use JQuery in Paperscript files, you'll need
to add JQuery as a script line in your HTML file (`<script
src="node_modules/jquery/dist/jquery.min.js"></script>`) and then
reference its global variable in your Paperscript file: `var $ =
window.$;`.


##Other libraries
Feel free to use other libraries. If you have a favorite other than
Paper, you're welcome to use it as long as you can complete the
assignment as requested.
