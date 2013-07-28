#!/usr/bin/env python
'''
This is a fast, leightweight XSLT transformation utility that uses libxslt to convert GPX files to KML for GPS analysis.   
Supplemental Research: https://forksec.wordpress.com/research-gps-device-analysis/
'''

import libxslt
import libxml2
import argparse
from sys import exit
from time import gmtime, strftime

parser = argparse.ArgumentParser(description='An XSLT GPX to KML conversion utility for use with GPS mapping software.')
parser.add_argument('-i','--input', help='Input GPX file to transform',required=True)
parser.add_argument('-o','--output', help='Output KML file to write', required=True)

args = parser.parse_args()
inputf = args.input
output = args.output
xslttransform = "transform.xslt"

def begin_conv():
	styledoc = libxml2.parseFile(xslttransform)
	style = libxslt.parseStylesheetDoc(styledoc)
	doc = libxml2.parseFile(inputf)
	result = style.applyStylesheet(doc, None)
	style.saveResultToFilename(output, result, 0)
	style.freeStylesheet()
	doc.freeDoc()
	result.freeDoc()

print ("Input file: %s" % args.input )
print ("Output file: %s" % args.output )

transgo = raw_input('Begin transform? [Y/N] ') 
if transgo == 'y' or transgo == 'Y':
	print '[' + strftime('%Y-%m-%d %H:%M:%S', gmtime()) + ' UTC] Executing transforms...'
	begin_conv()
elif transgo == 'n' or transgo == 'N':
    print '[' + strftime('%Y-%m-%d %H:%M:%S', gmtime()) + ' UTC] Bailing...'
    exit
else:
	print '[' + strftime('%Y-%m-%d %H:%M:%S', gmtime()) + ' UTC] Not an option. Quitting...'
	exit

print '[' + strftime('%Y-%m-%d %H:%M:%S', gmtime()) + ' UTC] Completed.'