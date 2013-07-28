### About TrackerCat

This is a Python XSLT conversion utility that takes a GPS eXchange Format file and converts it to a Keyhole Markup Language file by using an XSL stylesheet.  Using this tool, forensic analysts can quickly create mappable KML files that can be used to view trip data in programs like Google Earth. It does this by parsing the GPX's Active Log trip data. This includes the extraction of the log's main timestamp as well as trackpoint coordinates associated with that log.
 
**Other GPS Utilities**

Many hardware and software solutions exist for extracting trip data from GPS devices. Unlike many of these products, this tool is open source and free of charge. While XSL transformations from XML-to-KML are nothing new, an automated XML converter with GPX-to-KML in mind is new. 

Instead of having to manually examine each GPX, enter it into a specialized GPS program and re-save it as KML, this tool automates the conversion process. This tool was designed specifically for investigators to use in conjunction with pre-existing mapping software.  

**GPX Data Structures**

A working knowledge of GPX data structures and their timestamps is critical to your success with this tool. Not all GPS devices are the same. A proper analysis should never begin and end with executing a few lines of code and showing your boss a cool fly-over of GPS data in Google Earth. 

For some supplementary research on GPS device forensics with GPX files, feel free to read my research notes: [https://forksec.wordpress.com/research-gps-device-analysis](https://forksec.wordpress.com/research-gps-device-analysis)

**Aiding Analysts by Narrowing the Scope**

Mapping aside, TrackerCat can help you determine which GPX files contain Active Logs that fall into case's timeline. Instead of scrolling through thousands of lines of XML with syntax highlighting enabled, this approach allows you to convert a GPS data file into a mappable file. That will let you spend more time analyzing the data that matters!

**What it Does**

Presently the tool extracts Active Log timestamps as well as trackpoint coordinates from a specified GPX file.

![KML in Google Earth](http://forksec.files.wordpress.com/2013/07/activelogs-kml.jpg?w=900)

In the future it may allow for more advanced features such as extracting trackpoint timestamps for use in super timelines. Do you find designing open source tools for GPS analysis interesting? If yes, TrackerCat is for you.

**TrackerCat Project & Repository**

Feel free to use this GitHub to contribute to TrackerCat and expand its functionality. This includes creating other standalone tools that can be used to analyze other forms of GPS data. I’m not a professional programmer. The goal of the project is to work with fellow analysts and programmers to implement better open source GPS tools.
 
_TrackerCat is primarily designed for Windows using Python 2.7._ The tools found within the repository will likely run on any operating system with some tweaking. 

Please note that this project is in no way affiliated with Google, libxml2, libxslt, the Python Software Foundation, the Apache Software Foundation, the GNOME Project or any other group, organization or company that isn't specifically mentioned as a contributor in the Wiki.

If you’d like to show your support for the project, let me know and I’ll add your name to the Contributors section.

### Python Libraries

The two libraries required for Python XSL transformations using tc.py were originally written in C by Daniel Veillard for the GNOME Project. Both Python libraries are imported in full in the tc.py program.
 
For more information on libxml2 and libxslt, please see: [http://xmlsoft.org/](http://xmlsoft.org/) 

I've redistributed the library's source in this repository with full attribution paid to the developers. A copy of the MIT License can be seen here: [http://opensource.org/licenses/MIT](http://opensource.org/licenses/MIT)


### System Requirements

**Windows** _(Python 2.7+)_:
* The best way to install on Windows is by using the libxml and libxslt bindings (exe) from Stéphane Bidoul's site: http://users.skynet.be/sbi/libxml-python/  (an executable should be found within this repository)
* Have these documents in the same place: tc.py, transform.xslt as well as complete GPX (example, Current.gpx or a device’s archived GPX files).

**Linux** _(Python 2.6-dev)_:
* Download the appropriate libraries for your distro, here: ftp://xmlsoft.org/libxslt/ (they should be in the repo) 
* Keep in mind that the installation of the modules on linux is very distribution specific. 
* Documentation: http://www.xmlsoft.org/python.html
* Do not use apt-get autoremove on libxml2 (this is fairly destructive, removing everything GNOME related)

If you are having issues with compiling from source, you can try:

> sudo apt-get install python-dev && sudo apt-get install libxml2-dev && sudo apt-get install libxslt1-dev

Each distro is a little different with downloading and installing the modules. Generally, you should run "python setup.py build install" from within the module's folder and keep your fingers crossed. 
Providing technical support for the installation of those third party modules are beyond the scope of this document. If in doubt, please see: http://www.xmlsoft.org/FAQ.html or contact the developers.


### Java Transforms (Multi Platform Support)

My friend anonymously donated a quick java alternative to TC's Python conversion. This works on virtually any platform. 

Installing the OpenJDK 7: 
> sudo apt-get update & sudo apt-get install openjdk-7-jdk

Compile the Java Code:
> javac GpxToKml.java

Execute the Converter:
Ensure you have an input.gpx and the transform.xslt in the same location and go for it:
> java GpxToKml


### Troubleshooting in Windows

To troubleshoot Windows issues:

* Please ensure that you're running Python 2.7; this tool is not compatible with Python 3.0. There are no plans to adopt 3.0 in the near future.
* Python must be in your system path: C:\Python27; Refer to Python documentation for help.
* Feel free to tweak the self-executing line at the top of the Python script (tc.py) to fit your environment.
* Ensure that you have successfully built and installed libxml2 and libxslt OR that you have downloaded and installed the appropriate Windows bindings (I’ve provided an executable as well as its creator’s information in the repository).

### Using tc.py (Syntax)

To run tc.py, use the following directions:

* Export GPX files from device image to folder with the program's files. Critical timestamps will be maintained within the GPX files. Exporting does not change these timestamps for reasons discussed [in my research](http://forksec.wordpress.com/research-gps-device-analysis/).
* Run the python script with:

> python tc.py -i [gpx file] -o [output file]

* Assuming a successful transformation (a clean stdout is a good indication of success), launch Google Earth.
* Go to "File" and then "Open." Select the keyhole file you wish to examine (.KML).
* Under "Places," expand "Temporary Place," "Imported from GPX," and then "Tracklogs." 
* Note that, by default, ALL ACTIVE LOGS are selected. These contain trackpoint data. No waypoint data is extracted (while they are rich with actual addresses, they lack timestamps and are of no use to us). 

To see an updated list of accepted arguments by running tc.py with the –h flag.


### TrackerCat and Project

Some confusion is natural. I’ve referred to the “tool” (or tc.py) as well as “the project” throughout the wiki. 

The TrackerCat Project as a whole can include _attempts to modify or add features to the official TrackerCat tool itself_. As a secondary goal, _you can use the repository to aid in developing other tools for GPS device analysis_. These can be features you’d like to see added to tc.py or just supplementary tools.

Obviously_ any attempt to integrate a feature into tc.py must be written in Python_. I prefer all future modifications to tc.py stay Python 2.7-compliant. While 3.0 offers a number of interesting improvements, programs coded in 2.7 are more widely adopted and thus used for TrackerCat.

Supplementary tools – that aren’t designed to be integrated into tc.py - can be in _any _language. My particular involvement is not necessary: I trust the GH community. I know that Perl is huge in the DFIR community and is welcome here as well! Any contributions should be as cross-platform capable as possible.
 
This GitHub was created to facilitate the growth of tc.py, aid in the analysis of GPS artifacts, and help develop GPS device forensics as a whole.  


### Limitations of TrackerCat

**FILE SLACK**: Trackpoint data found in fileslack should not be passed through the Python script as something will break. This data is fragmented at best. If the data is valuable to you, feel free to manually add these coordinates to your finished XML file by using the proper KML elements. Usually this data is useless because - while it may contain coordinates the present GPX file does not - it usually isn't complete and fails to provide the scope necessary to understand the data.

More information on manually parsing and understanding GPX files can be read on my blog, on [my GPS research page](https://forksec.wordpress.com/research-gps-device-analysis/). While far from authoritative, it'll also give some more information on what can be found in slack space.

**TRACKPOINT TIMESTAMPS**: Individual trackpoints in GPX format have timestamps but KMLs do not. Active Logs still maintain temporal data (this is critical). There are two very different schools of thought at play: GPX files record movement in the highest level of detail possible whereas KMLs are geared toward mapping. Active Log times are critical and are the focus of TrackerCat. While it would have been nice to retain trackpoint times, this information is not as critical. 

The major limitation is that Active Logs do not contain as much temporal data as trackpoint times: Active Logs usually do not contain seconds. Usually, I like my timelines to chronicle every second of a given time span. Unfortunately that’s not possible here. Manually examining the GPX may be required unless a timestamp-to-csv is adopted.

To manually examine GPX files, I suggest using a tool like AccessData's FTK Imager or XML Spy.  Trackmaker is also a great tool worth mentioning (I used this tool extensively in my research in order to manually convert GPX files to KML files, it was also one of the inspirations behind TC).

Please see the section entitled _"Future Considerations"_ for another possible uses for trackpoint timestamps.


### Understanding GPX Files & Analyzing Devices

For more information on how to accomplish a manual analysis of a GPS device, please see my research notes in which I conducted an in-depth analysis of a popular GPS device.

[https://forksec.wordpress.com/research-gps-device-analysis/](https://forksec.wordpress.com/research-gps-device-analysis/)

The forensic analysts and technologists that work in the field have produced a number of amazing resources. I’ve added many of them as references on the bottom of my notes page.  


### Future Considerations

The goal of tc.py is to provide mappable output from GPS data files. That said, the following ideas are worth considering for improvements or modifications to the code or project as a whole:

* **GPX Input Validation**. This is really a matter of a simple bit of code but I'm not entirely convinced it's required. libxml2 -- which is being used in TC -- supports this functionality. 

* **GPX Active Log and Trackpoint Timestamps to CSV**. This possible enhancement allows for the extraction of both ActiveLog and Trackpoint timestamps found within a GPX and dumping them to a CSV. It calls upon the csv Python module. 
Since there are commercial tools that handle parsing GPS data extremely well, this may not be needed (knowing each trackpoint time is extremely anal and displays a propensity towards Obsessive Compulsive Disorder). Still, I can understand the need to see this feature included and gladly accept modifications that address this. 

* **Timestamps to Body File**. Another interesting possibility is dumping timestamps to a body file for direct input into super timelines. This, like timestamps-to-CSV, is not a priority but it should be considered.

* **Archive Grouping**.  This future consideration is one where you can take multiple files (say, GPX Archives) and convert them in a chained conversion, outputting to 1 master KML. This KML will have multiple historic Active Logs. It can use wildcards or some form of globbing.
_Example of this type of feature:_ an investigator notes multiple Active Logs of interest within a GPS device's GPX\Archives folder. This feature would be used to create a KML with many interesting Active Logs from past trips that have been phased out of the device's Current.gpx.
 
* **A GUI**. Worth considering but, since the tool is rather simple in its current incarnation, this isn't a big deal if we don’t have one for a while. Things like a CSV dump could easily be plugins that are selectable from a GUI menu.

The ideas expressed above are my own, I'll gladly adopt any working attempts to make the tc.py tool more "full featured." _**The best way to get a function or feature included in the official project is to write one yourself.**_


### Google Earth Tips


Something inside told me not to write this section. But then I figured, why not? Part of the appeal when it comes to GPS forensics is navigating across maps and viewing GPS history in real time. So, commence the fun…

Feel free to hit the "Play Tour" button at the bottom the Places panel (looks like a triangle). This is a minute long time waster that makes for nice eye candy during presentations!  

Additionally, you can right click on the Tracklog Active Log entries and select "Show Elevation Profile" to see the elevation distribution for that entry. The purpose of that is to help you understand the terrain. You may right click and select sections on the elevation panel to highlight that portion of the trip in the viewer. Elevation is stored in an XML element known as ele (in GPX-speak). I have preserved this data in the KML transformation. Terrain data is also stored on the keyhole server which Google Earth connects to when you first open the program (the default keyhole server is kh.google.com).

There’s so much more you can do with GPS device forensics but that would really go beyond TrackerCat. Suffice it to say that – in conjunction with your current forensic tools – TrackerCat can aid you in giving you one less thing to worry about. Hopefully you’ll also dig our mapping data.


### Choice of Project License


Let’s clear the air: I believe in free software. I want those with the skills to improve the tool or the overall project to be able to. That’s the reason I’ve selected a permissive Open Source license.

Adopting a copyleft license would restrict project developers in defining that all derivative works carry the same license. Instead, I’d like to ensure that future modifications are unhindered by legal regulations. 

And for the end user? Use the software where you see fit as long as attribution is maintained. If you'd like to see this tool prosper into a full-fledged open source project, consider donating some code! 

_Closed source modifications and enterprise/government use of any kind is also permitted._

Research or documentation found outside this project's repository is not licensed under the project's primary license. 


### Contact Project Lead

If you'd like to contact me for issues any issues that aren't covered in the Wiki, please use the [contact form on my blog](http://forksec.wordpress.com/contact/). 

_All animals appearing in this work are entirely fictitious. Any resemblance to real cats, living or dead is purely coincidental. All Rights Reserved. Some restrictions apply._
