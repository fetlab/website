Title: Project Guidelines&mdash;Individual Effort
Template: 722

This page describes the requirements for the **individual effort**
portion of the [group project](project_guidelines.html).

[TOC]

##Part 1: Initial paper exploration
Each student will individually look through (at least) the last three
years of each of the International Sympoisum on Wearable Computers
(ISWC), the International Joint Conference on Pervasive and Ubiquitous
Computing (UbiComp), and the International Conference on
Human-Computer Interaction with Mobile Devices and Services
(MobileHCI). These proceedings can be found in the ACM Digital
Library; ISWC and UbiComp are listed under the Publication tab
[here](http://dl.acm.org/event.cfm?id=RE336) and MobileHCI is under
the Publication tab [here](http://dl.acm.org/event.cfm?id=RE395). If
you have a favorite conference you'd like to add to this list, you
may, but the papers you choose must match the theme of the class and
no more than three may come from conferences other than those listed
here.

When looking through these conferences, don't read the papers (yet).
Look instead for things that catch your eye; in particular, you can
look at:

- the session title (e.g., _Wrist and hand interaction I_);
- the paper title (e.g., _Nail+: sensing fingernail deformation to
	detect finger force touch interactions on rigid surfaces_);
- the abstract for papers; and/or
- the video for papers (if there is a video, it can be found on an
	individual paper's page).

From these three years of three conferences, you will choose **nine**
papers (you can do one per conference/year, but don't have to) that
look, at first glance, interesting to possibly replicate or extend.

You will send me these nine papers via Slack, in a Post. Your post
must clearly number the papers 1--9, and consist of:

- the paper title;
- the paper authors;
- the conference the paper came from;
- a link to the paper's page on the ACM Digital Library;
- 1--2 sentences about what you find interesting about the paper.

Note that there are different kinds of papers; in particular, you may
notice "study" papers and "implementation" papers. To draw from my own
publications, _[Quickdraw](http://dl.acm.org/citation.cfm?id=1357092)_
is a study paper, looking at how quickly people can access their
mobile devices; _[Nenya](http://dl.acm.org/citation.cfm?id=1979238)_,
on the other hand, is primarily an implementation paper (with a study
component), discussing how I created a ring to control mobile devices.

##Part 2: Paper choice and summarization
Next you will download the PDFs for each your nine papers and skim the
paper. You can [read this brochure about efficiently reading
papers](http://www.cs.columbia.edu/~hgs/netbib/efficientReading.pdf),
but the relevant points for skimming, pulled from that link and
modified slightly, are:

- Read the introduction. Pay attention to the contributions the
	authors are trying to make. Sometimes they explicitly state this.
- Read the section headings.
- Look at the images and any tables or graphs and read the captions.
- Read the conclusions.

From these nine papers, you will:

- pick **three** that you find the most interesting, compelling, or
	otherwise desirable;
- read them _in their entirety_ (see [How to Read an Engineering
	Research Paper](https://cseweb.ucsd.edu/~wgg/CSE210/howtoread.html)
	and [How to read a research
	paper](http://www.eecs.harvard.edu/~michaelm/postscripts/ReadPaper.pdf));
- and write a summary of the paper and a brief sketch of how you might
	replicate or extend the paper, which you will submit to me via a
	Slack Post.

The summary should be several paragraphs long, and contain the
following parts:

- the title, authors, conference, and link to the paper (the same
	format as in your nine paper list);
- a clear explanation of what the goal of the authors was, including
	the contributions they were trying to make;
- an explanation of what method(s) they used to make their
	contributions, including what (if any) implementation was involved;
- what limitations, problems, or other issues there are with the
	research;
- and how you might replicate or extend their work during the course
	of the semester in order to either address the limitations or to
	confirm the correctness of their research.

###Example
Here's an example of what such a summary might look like:

<blockquote markdown="1">
Quickdraw: the impact of mobility and on-body placement on device access time.<br>
Daniel Ashbrook, James R Clawson, Kent Lyons, Thad E Starner, and Nirmal Patel.
CHI '08: Proceedings of the SIGCHI Conference on Human Factors in Computing Systems, New York, New York, USA 2008 pp. 219-222.<br>
http://portal.acm.org/citation.cfm?doid=1357054.1357092<br>
<br>
The goal of the authors was to empirically determine how long it would
take people to access devices that were placed at different points on
the body. In particular, they investigated a device in the pocket, in
a hip holster, and on the wrist.

The authors performed a study where they had people either stand still
or walk around, and timed how long it would take participants to
respond to an alarm on the device. They implemented software on a
phone to run the study, including presenting an alarm sound, measuring
response times, and detecting when the phone was removed from the
pocket by using the device's camera.

The research is at this point quite a few years old. Mobile phones
have gotten much less bulky, screens have become capacitive rather than
resistive, and we now have smartwatches. Hip holsters for mobile
phones are less common than they were in 2007 when this study was run.
All of these factors mean that the findings in this study may no
longer reflect the access times for real devices today.

I propose to replicate this study in order to determine whether the
measurements from this paper still apply today. Doing so will involve
implementing similar software to that used in this paper, and
designing and running a similar study. I propose to use a modern
Android-based mobile phone and an Android Wear-based smartwatch to
write the study software. Because hip holsters are less common, I
propose to skip that part of the study.
</blockquote>

##Grading
The individual effort portion of your grade is worth **12%**.

[Part 1](#part-1-initial-paper-exploration) is worth 5% of
your final grade; the criteria for this part are:

- You send me the correct number of papers from the correct
	conferences, as described above (1%).
- You adhere to the format and provide all of the information
	requested for each of the papers (3%).
- Your writing is clear and comprehensible without significant
	spelling or grammar errors (1%).

[Part 2](#part-2-paper-choice-and-summarization) is worth 7% of your
final grade; the criteria for this part are:

- You send me the correct number of papers from the correct
	conferences, as described above (1%).
- You adhere to the format and provide all of the information
	requested for each of the papers (5%).
- Your writing is clear and comprehensible without significant
	spelling or grammar errors (1%).

