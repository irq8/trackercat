### About TrackerCat

TrackerCat is an open source GPS forensics utility that parses GPX files on devices that use them for recording trip activity. The tool is designed for forensic analysts, private sector investigators, law enforcement, or military personnel. TC should be used in *conjunction* with an investigator's current forensics tools. It is not designed to replace other GPS forensics tools. It can't compete with commercial products either. But it can extract large amounts of critical GPS data from supported devices.

The tool is 100% open source and freely available. It can also be incorporated into your own open or closed source project. 

Below is a exhaustive README which describes the tool, its use, GPX-file forensics, troubleshooting tips, set up the depedencies on Windows and Linux, KML use in Google Maps, and some other things.

~

***tc.py*** -- the Python 2.7 tool hosted here can parse GPX files (XML files found on many GPS devices). The tool does *not* support historic data stored in binary files and can only be used on devices that utilize the GPX 1.1 format. That said, tc.py can dump critical timestamp and trip coordinates to CSV format. The data can also be imported into major mapping tools that support KML (Keyhole Markup Language). 

***Supported Devices*** -- TC should be able to parse the content of any GPS devices that record trip data in GPX files. This includes many older GPS devices. A few Garmin devices were tested during the creation of the tool.

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

Using this function, you can manually narrow down your timeframe using some excel-fu. Unlike using regular expressions (which may prove troublesome against massive XML files), TrackerCat can handle this with ease.

When run with -csv - after extracting trackpoint times - it'll also ask whether or not you want the parent Active Log info printed to their own CSV. This is completely optional and may not be necessary in all cases.

<center><img src="http://forensicsblog.org/wp-content/uploads/2013/08/trackercat.jpg" alt="Active Logs & Trackpoint CSVs" width="%40"><i>- Active Logs and Trackpoint CSVs</i></center>

**Data File Extraction**
The -e argument allows the analyst to recursively export all GPX files from a mounted device or local path. This includes all archived GPXs.

**Help & Feature Check**
> python tc.py -h 

### XSLT GPX-to-KML Conversion 

TC has a Python XSLT conversion function that takes a GPS eXchange Format file and converts it to a Keyhole Markup Language file by using an XSL stylesheet.  Using this tool, forensic analysts can quickly create mappable KML files that can be used to view trip data in programs like Google Earth. It does this by parsing the GPX's Active Log trip data. This includes the extraction of the log's main timestamp as well as trackpoint coordinates associated with that log. Additional trackpoint data can be extracted with the -csv argument.

While Google Earth automatically converts GPX files to KML, TC is designed for ease of use and automates this process. Information gathering and conducting investigations is key, not playing with mapping tools. Files are immediately saved to 100% XML-valid KML files (not compressed KMZs). They can be used by mapping tools immediately. Unlike tools such as GPS TrackMaker, TC immediately provides quick results without opening and re-saving as a different file type. 

Plug a file in, convert it, then view tracks in your favorite mapping tool.
 
### Trackpoint Times to CSV

The timestamp-to-CSV function allows you to extract trackpoint timestamps and coordinates, writing them both to a single CSV. It also allows for the optional creation of an Active Log CSV file. Both can be used for timeline correlation. Since Active Log data is easily exported to KML by TC, trackpoint data to CSV is more useful. 

Since these timestamps are *within* the file's XML, there's no worry about modifying the data. Since this is a forensics tool and not a trip manager (like other GPX managers), it will never alter data on the device.


**Device Equivalent to a Last Write Time**

On the Garmins I've tested, GPX Metadata Time tag are of significant importance.

If a GPX Metadata Time is read from Current.gpx in DEVICE\GPX\Current.gpx, this time will act as a "last write time" on many devices. To be more percise, if the input file is Current.gpx, this will represent the time the device was last powered on. Instead of making that assumption for you, TC will simply provide this timestamp to you while processing.

The GPX Metadata Time is not written CSV since archived GPX metadata times are much less significant than Current.gpx's time. You could always > redirect output to a file and record the tool's visual output if neccessary.


### Other GPS Utilities

Many hardware and software solutions exist for extracting trip data from GPS devices. Unlike many of these products, this tool is open source and free of charge. While XSL transformations from XML-to-KML are nothing new, an automated XML converter with GPX-to-KML is unique. While GPX parsers are not new either, this is the first open source GPS tool with GPX forensics in mind.   

### GPX Data Structures

A working knowledge of GPX data structures and their timestamps is critical to your success with this tool. Not all GPS devices are the same. A proper analysis should never end by executing a few lines of code and showing your boss a cool fly-over of GPS data in Google Earth. ***You may need to modify this code to get it to work with your target device!!!***

For some supplementary research on GPS device forensics with GPX files, feel free to read my research notes: [http://forensicsblog.org/research-gps-device-analysis](http://forensicsblog.org/research-gps-device-analysis)

### Aiding Analysts by Narrowing the Scope

Mapping aside, TrackerCat can help you determine which GPX files contain Active Logs that fall into case's timeline. Instead of scrolling through thousands of lines of XML with syntax highlighting enabled, this approach allows you to convert a GPS data file into a mappable file. Unlike other tools that do the same, TC also has advanced options which allow you to *dump individual trackpoint timestamps* to CSV. 


If the hierarchy or search patterns used by the tool doesn't fit your device's data structure, modify it!

TC can be useful during active investigations to help an analyst determine whether or not a seized GPS device holds the critical information. It can also be used to corroborate known facts of a case through timeline analysis.

### Expanding TrackerCat's Features

Feel free to use this GitHub to contribute to TrackerCat and expand its functionality. This includes creating other standalone tools that can be used to analyze other forms of GPS data. I’m not a professional programmer. The goal of the project is to work with fellow analysts and programmers to implement better open source GPS tools.
 
_TrackerCat is primarily designed for Windows using Python 2.7._ The tools found within the repository will likely run on any operating system with some tweaking. 

This project is in no way affiliated with Google, libxml2, libxslt, the Python Software Foundation, the Apache Software Foundation, the GNOME Project or any other group, organization or company that isn't specifically mentioned in this document.

If you’d like to show your support for the project, let me know and I’ll add your name to a Contributors section. 

### Python Libraries

The two third party libraries required for the Python XSL transformation function in tc.py was originally written in C by Daniel Veillard for the GNOME Project. Both Python libraries are imported in full in the tc.py program. 
 
For more information on libxml2 and libxslt, please see: [http://xmlsoft.org/](http://xmlsoft.org/) 

I've redistributed the library's source in this repository with full attribution paid to the developers. A copy of the MIT License can be seen here: [http://opensource.org/licenses/MIT](http://opensource.org/licenses/MIT)

### System Requirements

**Windows** _(Python 2.7+)_:
* The best way to install libxml2/libxslt Windows is by using the libxml and libxslt bindings (exe) from Stéphane Bidoul's site: http://users.skynet.be/sbi/libxml-python/  (an executable should be found within this repository)
* Have these documents in the same place: tc.py, transform.xslt as well as complete GPX (example, Current.gpx or a device’s archived GPX files).
* A sufficient amount of memory necessary to run the trackpoint-to-CSV feature (this should not pose a significant problem, even if processing large amount of data).

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

* Please ensure that you're running Python 2.7; this tool is not compatible with Python 3.0.
* Python must be in your system path: C:\Python27; Refer to Python documentation for help.
* Feel free to tweak the self-executing line at the top of the Python script (tc.py) to fit your environment.

### Modifications

The TrackerCat Project as a whole can include _attempts to modify or add features to the official TrackerCat tool itself_. As a secondary goal, _you can use the repository to aid in developing other tools for GPS device analysis_. These can be features you’d like to see added to tc.py or just supplementary tools.

Obviously _any attempt to integrate a feature into tc.py must be written in Python_. I prefer all future modifications to tc.py stay Python 2.7-compliant. While 3.0 offers a number of interesting improvements, programs coded in 2.7 are more widely adopted and thus used for TrackerCat.
 
This GitHub was created to facilitate the growth of tc.py, aid in the analysis of GPS artifacts, and help develop GPS device forensics as a whole.  

### Limitations of TrackerCat

**FILE SLACK and Memory Concerns** -- Trackpoint data found in fileslack should not be passed through the Python script as something will break. This data is fragmented at best. If the data is valuable to you, feel free to manually add these coordinates to your finished XML file by using the proper KML elements. Usually this data is useless because - while it may contain coordinates the present GPX file does not - it usually isn't complete and fails to provide the scope necessary to make sense of the data for investigative purposes. 

It probably goes without saying but physical hardware analysis, flash memory concerns, data fragmentation, and other issues are beyond TC. 

More information on manually parsing and understanding GPX files can be read on my blog, on [my GPS research page](http://forensicsblog.org/research-gps-device-analysis/). While far from authoritative, it'll also give some more information on what can be found in slack space.

**Remaining Folders After Export** -- TC doesn't always cleanup after itself and delete empty directories remaining after a successful extraction. 

To manually examine GPX files, I suggest using a tool like AccessData's FTK Imager or XML Spy. 

### Understanding GPX Files & Analyzing Devices

For more information on how to accomplish a manual analysis of a GPS device, please see my research notes in which I conducted an in-depth analysis of an older (popular) commercial GPS device.

[http://forensicsblog.org/research-gps-device-analysis/](http://forensicsblog.org/research-gps-device-analysis/)

The forensic analysts and technologists that work in the field have produced a number of amazing resources. I’ve added many of them as references on the bottom of my notes page.  

### Ideas for Future Consideration

The goal of tc.py is to provide mappable output from GPS data files. That said, the following ideas are worth considering:

* **Timestamps to Body File**. Another interesting possibility is dumping timestamps to a body file for direct input into super timelines. There would need to be more than a few commandline ways of pruning data, the output of a sizeable workload would be massive.
* **Archive Grouping**  Taking multiple files (like GPX Archives) and converting them into a chained conversion, outputting to 1 master KML. This KML will have multiple historic Active Logs. It can use wildcards or some form of globbing.
_Example of this type of feature:_ an investigator notes multiple Active Logs of interest within a GPS device's GPX\Archives folder. This feature would be used to create a KML with many interesting Active Logs from past trips that have been phased out of the device's Current.gpx. Data would be appended to one massive KML for mapping.
* **Direct Image Mounting** I've been considering the use of [guestfs](http://libguestfs.org/guestfs-python.3.html) but this isn't that important.

### Google Earth Tips

Part of the appeal when it comes to GPS forensics is navigating across maps and viewing GPS history in real time. So, commence the fun…

Feel free to hit the "Play Tour" button at the bottom the Places panel (looks like a triangle). This is a minute long time waster that makes for nice eye candy during presentations.

Additionally, you can right click on the Tracklog Active Log entries and select "Show Elevation Profile" to see the elevation distribution for that entry. The purpose of that is to help you understand the terrain. You may right click and select sections on the elevation panel to highlight that portion of the trip in the viewer. I have preserved elevation data in the KML transformation. Terrain data is also stored on the keyhole server which Google Earth connects to when you first open the program (the default keyhole server is kh.google.com).

### Thanks for reading

Special thanks to the entire staff and user-base of [Stack Overflow](http://www.stackoverflow.com) and [Dream in Code](http://www.dreamincode.net/) for your support. Also a big thanks to ethompso for aiding me in fixing the tool's GPX extraction capabilities.
