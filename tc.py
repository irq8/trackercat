#!/usr/bin/env python
'''
This is a fast, lightweight GPS utility designed to analyze GPX files. 
Supplemental Research: https://forksec.wordpress.com/research-gps-device-analysis/
'''

import csv
from sys import exit
import libxslt, libxml2
import argparse, shutil, os
from time import gmtime, strftime
from xml.etree import ElementTree
from xml.dom.minidom import parse, parseString

parser = argparse.ArgumentParser(description='A GPS Utility for analyzing GPX files.')
parser.add_argument('-i','--input', help='Input GPX file to transform',required=False) 
parser.add_argument('-o','--output', help='Output KML file to write', required=False)
parser.add_argument('-e','--extractpath', help='Extract from Path', required=False) # Mounted image or local.
parser.add_argument('-csv', help='Input GPX trackpoint timestamps to CSV', required=False)

args = parser.parse_args()
inputf = args.input
output = args.output
extractpath = args.extractpath
xslttransform = 'transform.xslt'
csvinputfile = args.csv

def begin_conv():
	styledoc = libxml2.parseFile(xslttransform)
	style = libxslt.parseStylesheetDoc(styledoc)
	doc = libxml2.parseFile(inputf)
	result = style.applyStylesheet(doc, None)
	style.saveResultToFilename(output, result, 0)
	style.freeStylesheet()
	doc.freeDoc()
	result.freeDoc()

def converter():
	print ("Input file: %s" % args.input )
	print ("Output file: %s" % args.output )
	transgo = raw_input('Begin transform? [Y/N] ') 
	if transgo == 'y' or transgo == 'Y':
		print '[' + strftime('%Y-%m-%d %H:%M:%S', gmtime()) + ' UTC] Executing transforms...'
		begin_conv()
		print '[' + strftime('%Y-%m-%d %H:%M:%S', gmtime()) + ' UTC] Completed.'
	elif transgo == 'n' or transgo == 'N':
		print '[' + strftime('%Y-%m-%d %H:%M:%S', gmtime()) + ' UTC] Bailing...'
		exit
	else:
		print '[' + strftime('%Y-%m-%d %H:%M:%S', gmtime()) + ' UTC] Not an option. Quitting...'
		exit

def gpxlist(ext, dirname, names):
    ext = ext.lower() 
    for name in names:
        if name.lower().endswith('.gpx'):
            print(os.path.join(dirname, name))

def ignore_list(path, files):
    ret = []
    for fname in files:
        fullFileName = os.path.normpath(path) + os.sep + fname
        if not os.path.isdir(fullFileName) \
            and not fname.endswith('gpx'):
            ret.append(fname)
    return ret

def gpxextract(src,dest):
    print '[' + strftime('%Y-%m-%d %H:%M:%S', gmtime()) + ' UTC] Executing Extraction (may take a minute)...'
    shutil.copytree(src,dest,ignore=ignore_list)
    print '[' + strftime('%Y-%m-%d %H:%M:%S', gmtime()) + ' UTC] Successfully Extracted: '
    os.path.walk(path, gpxlist, '.gpx')
    for root, dirs, files in os.walk(dest):
        for dn in dirs:
            pth = os.path.join(root, dn)
            try:
                os.rmdir(pth)
                os.rmdir(root)
            except OSError:
                pass

def gpxtrkparser():
    dom = parse(csvinputfile)
    for metatime in dom.getElementsByTagName('metadata'):
        metatimetag = metatime.getElementsByTagName('time')[0].firstChild.nodeValue
        print '[' + strftime('%Y-%m-%d %H:%M:%S', gmtime()) + ' UTC] GPX Metadata Time:', metatimetag
    namespace = 'http://www.topografix.com/GPX/1/1'
    tree = ElementTree.parse(csvinputfile)
    root = tree.getroot()
    trackSegments = root.getiterator("{%s}trkseg" % namespace)
    for trackSegment in trackSegments:
        for trkpts in trackSegment:
            csvout.writerow([trkpts.find('{%s}time'% namespace).text, trkpts.attrib['lat'], trkpts.attrib['lon'], trkpts.find('{%s}ele'% namespace).text])

def activelogparser():
    with open('activelog.csv', 'wb') as activelogcsvparser:
        csvout2 = csv.writer(activelogcsvparser, delimiter=',',
            quotechar=',', quoting=csv.QUOTE_MINIMAL)
        csvout2.writerow(['ACTIVE LOGS'])
        dom = parse(csvinputfile)
        for activelog in dom.getElementsByTagName('trk'):
            activelog = activelog.getElementsByTagName('name')[0].firstChild.nodeValue
            print activelog
            csvout2.writerow([activelog])
    activelogcsvparser.close()

if args.input and args.output:
	converter()
if args.extractpath:
	path = args.extractpath
	gpxextract(extractpath, 'Exports')

if args.csv:
    print '[' + strftime('%Y-%m-%d %H:%M:%S', gmtime()) + ' UTC] Extracting trackpoint temporal data to CSV...'
    with open('trackpoints.csv', 'wb') as csvfile:
        csvout = csv.writer(csvfile, delimiter=',',
            quotechar=' ', quoting=csv.QUOTE_MINIMAL)
        csvout.writerow(['TRKPT TIMESTAMP', 'LATITUDE', 'LONGITUDE', 'ELEVATION'])
        gpxtrkparser()
        print '[' + strftime('%Y-%m-%d %H:%M:%S', gmtime()) + ' UTC] Timestamps Extracted to trackpoints.csv.'
        csvfile.close()
        activelogcsvb = raw_input("Create a second CSV with Active Logs? [Y/N] ")
        activelogcsv = activelogcsvb.lower()
        if activelogcsv == 'y':
            activelogparser()
            print '[' + strftime('%Y-%m-%d %H:%M:%S', gmtime()) + ' UTC] Active Log Timestamps Extracted to activelogs.csv.'
        if activelogcsv == 'n':
            print '[' + strftime('%Y-%m-%d %H:%M:%S', gmtime()) + ' UTC] Exiting...'
            exit
        else:
            print '[' + strftime('%Y-%m-%d %H:%M:%S', gmtime()) + ' UTC] Exiting...'
            exit