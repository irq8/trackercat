### About TrackerCat

TrackerCat is an open source GPS utility that excels in working with GPX files. It's geared for forensic analysts, private sector investigators, law enforcement or military personnel to assist in conducting GPS device analysis. TC should be used in conjunction with an investigator's current forensics tools. It can also be incorporated into your own open source or closed source project.  

The project's tools are 100% open source and freely available.

### Use

**Recursive Extraction**

> python tc.py -e [Mounted Image or Local Path]

A folder named 'Exports' will contain all GPXs in the specified path as well as sub-directories. This includes any Archive folders containing historic trip data.

**XSLT GPX-to-KML Conversion**
> python tc.py -i [gpx file] -o [output file]

You can find the Active Logs by selecting "Places," "Temporary Places," "Imported from GPX," and then opening "Tracklogs."
 
By default ALL ACTIVE LOGS are selected. These contain trackpoint data. No waypoint data is extracted (while they are rich with actual addresses, they lack timestamps and are of no use to us). You will also need to have the transform.xslt in the TrackerCat folder.

**Trackpoint Timestamps to CSV**
> python tc.py -csv [gpx file]

This will export trackpoint times and coordinates from a GPX file. This can be quite cumbersome and, usually, contains well over 9,000 timestamps (depending on the GPX file and GPS device). Among many other things, trackpoint times can give you a deeper understanding as to the timeframe of data stored on the GPS device. 

When run with -csv - after extracting trackpoint times - it'll also ask whether or not you want the parent Active Log info printed to their own CSV.


**Help & Feature Check**
> python tc.py -h 

### XSLT GPX-to-KML Conversion 

TC has a Python XSLT conversion function that takes a GPS eXchange Format file and converts it to a Keyhole Markup Language file by using an XSL stylesheet.  Using this tool, forensic analysts can quickly create mappable KML files that can be used to view trip data in programs like Google Earth. It does this by parsing the GPX's Active Log trip data. This includes the extraction of the log's main timestamp as well as trackpoint coordinates associated with that log. Additional trackpoint data can be extracted with the -csv argument.

While Google Earth automatically converts GPX files to KML, TC is designed for forensics and investigators. Files are immediately saved to 100% XML-valid KML files (not compressed KMZs). Unlike tools such as GPS TrackMaker, TC immediately provides quick results without opening and re-saving as a different file type. 

Plug a file in, convert it, then view tracks in your favorite mapping tool.
 
### Trackpoint Times to CSV

The timestamp-to-CSV function allows you to extract trackpoint timestamps and coordinate data, writing them both to a single CSV. It also allows for the optional creation of an Active Log CSV file. Both can be used for timeline correlation. Since Active Log data is easily exported to KML by TC, trackpoint data to CSV is more useful. 

**Device Equivalent to a Last Write Time**

On the Garmin's I've tested, GPX Metadata Time's are of significant importance.

If a GPX Metadata Time is read from Current.gpx in DEVICE\GPX\Current.gpx, this time will act as a "last write time" on many devices. To be more percise, if the input file is Current.gpx, this will represent the time the device was last powered on. Instead of making that assumption for you, TC will simply provide this time to you via stdout.

The GPX Metadata Time is not written CSV since archived GPX metadata times are much less significant than Current.gpx's time.

### Data File Extraction

The -e argument allows the analyst to recursively export all GPX files from a mounted device or local path. This includes all archived GPXs.

### Other GPS Utilities

Many hardware and software solutions exist for extracting trip data from GPS devices. Unlike many of these products, this tool is open source and free of charge. While XSL transformations from XML-to-KML are nothing new, an automated XML converter with GPX-to-KML in mind is new. While GPX parsers are not new either, this is the first open source GPS tool with GPX forensics in mind.   

### GPX Data Structures

A working knowledge of GPX data structures and their timestamps is critical to your success with this tool. Not all GPS devices are the same. A proper analysis should never end by executing a few lines of code and showing your boss a cool fly-over of GPS data in Google Earth. 

For some supplementary research on GPS device forensics with GPX files, feel free to read my research notes: [https://forksec.wordpress.com/research-gps-device-analysis](https://forksec.wordpress.com/research-gps-device-analysis)

### Aiding Analysts by Narrowing the Scope

Mapping aside, TrackerCat can help you determine which GPX files contain Active Logs that fall into case's timeline. Instead of scrolling through thousands of lines of XML with syntax highlighting enabled, this approach allows you to convert a GPS data file into a mappable file. Unlike other tools that do the same, TC also has advanced options which allow you to dump individual trackpoint timestamps to CSV. 

![KML in Google Earth](http://forksec.files.wordpress.com/2013/07/activelogs-kml.jpg?w=900)

TC can be useful during active investigations to help an analyst determine whether or not a seized GPS device holds the critical information they need. It can also be used to corroborate known facts of a case through timeline analysis. Regardless of how the tool is used, it can provide great insight into a GPS devices that use GPX files.


### Adding Other Features

Check out the <a href="https://github.com/irq8/trackercat/issues/milestones?with_issues=no">Project Milestones</a> to see some goals and desired improvements!

### TrackerCat Project & Repository

Feel free to use this GitHub to contribute to TrackerCat and expand its functionality. This includes creating other standalone tools that can be used to analyze other forms of GPS data. I’m not a professional programmer. The goal of the project is to work with fellow analysts and programmers to implement better open source GPS tools.
 
_TrackerCat is primarily designed for Windows using Python 2.7._ The tools found within the repository will likely run on any operating system with some tweaking. 

Please note that this project is in no way affiliated with Google, libxml2, libxslt, the Python Software Foundation, the Apache Software Foundation, the GNOME Project or any other group, organization or company that isn't specifically mentioned in this document.

If you’d like to show your support for the project, let me know and I’ll add your name to a Contributors section. 

### Python Libraries

The two third party libraries required for the Python XSL transformation function in tc.py was originally written in C by Daniel Veillard for the GNOME Project. Both Python libraries are imported in full in the tc.py program.
 
For more information on libxml2 and libxslt, please see: [http://xmlsoft.org/](http://xmlsoft.org/) 

I've redistributed the library's source in this repository with full attribution paid to the developers. A copy of the MIT License can be seen here: [http://opensource.org/licenses/MIT](http://opensource.org/licenses/MIT)

### System Requirements

**Windows** _(Python 2.7+)_:
* The best way to install libxml2/libxslt Windows is by using the libxml and libxslt bindings (exe) from Stéphane Bidoul's site: http://users.skynet.be/sbi/libxml-python/  (an executable should be found within this repository)
* Have these documents in the same place: tc.py, transform.xslt as well as complete GPX (example, Current.gpx or a device’s archived GPX files).
* A sufficient amount of memory necessary to run the trackpoint-to-CSV feature (this should not pose a significant problem).

**Linux** _(Python 2.6-dev)_:
* Download the appropriate libraries for your distro for XSLT transforms, here: ftp://xmlsoft.org/libxslt/ (they should be in the repo) 
* Keep in mind that the installation of the modules on linux is very distribution specific. 
* XSLT Transformation Documentation: http://www.xmlsoft.org/python.html
* Do not use apt-get autoremove on libxml2 (this is fairly destructive, removing everything GNOME related)

If you are having issues with compiling from source, you can try:

> sudo apt-get install python-dev && sudo apt-get install libxml2-dev && sudo apt-get install libxslt1-dev

Each distro is a little different with downloading and installing the modules. Generally, you should run "python setup.py build install" from within the module's folder and keep your fingers crossed. 
Providing technical support for the installation of those third party modules are beyond the scope of this document. If in doubt, please see: http://www.xmlsoft.org/FAQ.html or contact the developers.

### XSLT Java Transforms (Multi Platform Support)

My friend anonymously donated a quick java alternative to TC's Python conversion function. This works on virtually any platform. You need an input.gpx and the transform.xslt in the same location. 

Installing the OpenJDK 7: 
> sudo apt-get update & sudo apt-get install openjdk-7-jdk

Compile the Java Code:
> javac GpxToKml.java

Executing the Converter:
> java GpxToKml

### Troubleshooting in Windows

To troubleshoot Windows issues:

* Please ensure that you're running Python 2.7; this tool is not compatible with Python 3.0. There are no plans to adopt 3.0 in the near future.
* Python must be in your system path: C:\Python27; Refer to Python documentation for help.
* Feel free to tweak the self-executing line at the top of the Python script (tc.py) to fit your environment.

### TrackerCat and Project

The TrackerCat Project as a whole can include _attempts to modify or add features to the official TrackerCat tool itself_. As a secondary goal, _you can use the repository to aid in developing other tools for GPS device analysis_. These can be features you’d like to see added to tc.py or just supplementary tools.

Obviously _any attempt to integrate a feature into tc.py must be written in Python_. I prefer all future modifications to tc.py stay Python 2.7-compliant. While 3.0 offers a number of interesting improvements, programs coded in 2.7 are more widely adopted and thus used for TrackerCat.

Supplementary tools – that aren’t designed to be integrated into tc.py - can be in _any _language. My particular involvement is not necessary: I trust the GH community. I know that Perl is huge in the DFIR community and is welcome here! Any contributions should be as cross-platform capable as possible.
 
This GitHub was created to facilitate the growth of tc.py, aid in the analysis of GPS artifacts, and help develop GPS device forensics as a whole.  

### Limitations of TrackerCat

**FILE SLACK**: Trackpoint data found in fileslack should not be passed through the Python script as something will break. This data is fragmented at best. If the data is valuable to you, feel free to manually add these coordinates to your finished XML file by using the proper KML elements. Usually this data is useless because - while it may contain coordinates the present GPX file does not - it usually isn't complete and fails to provide the scope necessary to understand the data.

More information on manually parsing and understanding GPX files can be read on my blog, on [my GPS research page](https://forksec.wordpress.com/research-gps-device-analysis/). While far from authoritative, it'll also give some more information on what can be found in slack space.

To manually examine GPX files, I suggest using a tool like AccessData's FTK Imager or XML Spy. 

Please see the section entitled _"Future Considerations"_ for another possible uses for trackpoint timestamps.

### Understanding GPX Files & Analyzing Devices

For more information on how to accomplish a manual analysis of a GPS device, please see my research notes in which I conducted an in-depth analysis of a popular GPS device.

[https://forksec.wordpress.com/research-gps-device-analysis/](https://forksec.wordpress.com/research-gps-device-analysis/)

The forensic analysts and technologists that work in the field have produced a number of amazing resources. I’ve added many of them as references on the bottom of my notes page.  

### Future Considerations

The goal of tc.py is to provide mappable output from GPS data files. That said, the following ideas are worth considering for improvements or modifications to the code or project as a whole:

* **Timestamps to Body File**. Another interesting possibility is dumping timestamps to a body file for direct input into super timelines. 

* **Archive Grouping**.  This future consideration is one where you can take multiple files (say, GPX Archives) and convert them in a chained conversion, outputting to 1 master KML. This KML will have multiple historic Active Logs. It can use wildcards or some form of globbing.
_Example of this type of feature:_ an investigator notes multiple Active Logs of interest within a GPS device's GPX\Archives folder. This feature would be used to create a KML with many interesting Active Logs from past trips that have been phased out of the device's Current.gpx. Data would be appended to one massive KML for mapping.
 
* **A GUI**. Worth considering but, since the tool is rather simple in its current incarnation, this isn't a big deal if we don’t have one for a while. Things like a CSV dump could easily be plugins that are selectable from a GUI menu.

* **Image Mounting**. While exporting from a specific path is possible with the current implementation of TC, there's no form of direct image mounting and unmounting. I've been considering the use of [guestfs](http://libguestfs.org/guestfs-python.3.html) should TC need it in the future. At the moment this isn't a priority.

The ideas expressed above are my own, I'll gladly adopt any working attempts to make the tc.py tool better. _**The best way to get a function or feature included in the official project is to write one yourself.**_

### Google Earth Tips

Part of the appeal when it comes to GPS forensics is navigating across maps and viewing GPS history in real time. So, commence the fun…

Feel free to hit the "Play Tour" button at the bottom the Places panel (looks like a triangle). This is a minute long time waster that makes for nice eye candy during presentations.

Additionally, you can right click on the Tracklog Active Log entries and select "Show Elevation Profile" to see the elevation distribution for that entry. The purpose of that is to help you understand the terrain. You may right click and select sections on the elevation panel to highlight that portion of the trip in the viewer. I have preserved elevation data in the KML transformation. Terrain data is also stored on the keyhole server which Google Earth connects to when you first open the program (the default keyhole server is kh.google.com).


### Choice of Project License

 I believe in free software and would like the chance for skilled programmers to contribute to this project. That’s the reason I’ve selected a permissive Open Source license instead of a copyleft license. Adopting a copyleft license would restrict project developers in defining that all derivative works carry the same license. Instead, I’d like to ensure that future modifications are unhindered by legal regulations. 

And for the end user? Use the software in any way you see fit as long as some attribution is maintained. If you'd like to see this tool prosper into a full-fledged open source project, consider donating some code! 

_Closed source modifications and enterprise/government use of any kind is also permitted._

Research or documentation found outside this project's repository is not licensed under the project's primary license. 


### Contact Project Lead

If you'd like to contact me for issues any issues that aren't covered here, please use the [contact form on my blog](http://forksec.wordpress.com/contact/). 

_All animals appearing in this work are entirely fictitious. Any resemblance to real cats, living or dead is purely coincidental. All Rights Reserved. Some restrictions apply._