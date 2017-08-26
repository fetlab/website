Title: Assignment 1 Setup
Template: 720

##Goals
The goal for this task is to be ready to do the hands-on work in
class, and to be set up to do. You'll be doing the following:

- **Github:** getting set up with a Github account and software
- **Paper:** installing Paper.js, a Javascript graphics library
- **jQuery:** installing jQuery, a Javascript utility library

If you have problems with any of these steps, Google first, then ask
on [Slack](using_slack.html) (also see [How to ask
questions](http://www.catb.org/esr/faqs/smart-questions.html#intro)).

###Grading
You'll get credit for following these instructions and being prepared
in class. You'll lose credit for not being ready to be hands-on in
class.

##Github
Set up a new repository for this assignment. You'll turn it in by
giving me the link to this repository. I'd suggest starting to use
this repository right away while you work on this assignment.

**Note:** Because everything on Github is by default
publically-visible, you must be extra-careful about giving attribution
to code you didn't write yourself. If in doubt, double-check the
[syllabus](files/720/syllabus.pdf) for the attribution and plagiarism
policies.

##Paper
I recommend using [Paper.js](http://paperjs.org) for visualization.
It's a well-thought-out Javascript graphics library that has a lot of
good documentation and examples. It has a special Javascript extension
language called Paperscript which makes using it easier. In order to
take advantage of it, download it and install it from the site above,
and include it in your HTML file directly via (e.g.) `<script
src="paperjs-v0.9.23/dist/paper-full.js"></script>`. Read and work
through the [Paper.js tutorials](http://paperjs.org/tutorials/) so you
understand how to use it (note you can use the Paper.js
[sketch](http://sketch.paperjs.org) tool to easily experiment in your
browser). It is a good idea to start playing with it right away.

###Tips
* If you find that your graphics aren't showing up right away, try
	calling `view.draw()` to force an update.
* Chrome often has better performance. However, to use Paperscript in
	an external file, Paper has to load the Paperscript file and process
	it. This means it's using Javascript to open local files, which
	Chrome prohibits.  To get around this problem, start Chrome using
	the `--allow-file-access-from-files` argument. If you're on a Mac,
	open a Terminal and run `/Applications/Google\
	Chrome.app/Contents/MacOS/Google\ Chrome
	--allow-file-access-from-files &`; then you can close the Terminal
	window.

##jQuery
jQuery is a handy Javascript library that does lots of useful stuff.
Download a copy from [the jQuery website](http://jquery.com/download/)
(get the "compressed, production jQuery")
and include it in your HTML file with something like `<script
src="jquery-3.1.0.min.js"></script>`. You can then use the global
jQuery variable `$`.

##Other libraries
Feel free to use other libraries. If you have a favorite other than
Paper, you're welcome to use it as long as you can complete the
assignment as requested.

##Javascript
If you're unfamiliar with it, you might want to start with my
[Introduction to Javascript](intro_to_js.html) page, and continue with
some of the resources listed on [the front page](index.html).
