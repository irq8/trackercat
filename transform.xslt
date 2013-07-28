<?xml version="1.0" encoding="utf-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform" version="1.0"
	xmlns:g="http://www.topografix.com/GPX/1/1"
	xmlns="http://earth.google.com/kml/2.0">
	<xsl:output method="xml" version="1.0" encoding="UTF-8" indent="yes"/>
	<xsl:template match="/g:gpx">
		<kml>
			<Document>
				<name>Imported from GPX</name>
				<visibility>1</visibility>
				<Style id="waypoint">
					<Icon>
						<href>http://maps.google.com/mapfiles/kml/pushpin/ylw-pushpin.png</href>
					</Icon>
				</Style>
				<Style id="route">
					<Icon>
						<href>root://icons/bitmap-4.png?x=160&amp;y=0&amp;w=32&amp;h=32</href>
					</Icon>
				</Style>
				<Folder>
					<name>Tracklogs</name>
					<visibility>1</visibility>
					<xsl:apply-templates select="g:trk" />
				</Folder>
			</Document>
		</kml>
					
	</xsl:template>
	
	<xsl:template match="g:trk">
		<Placemark>
			<name><xsl:value-of select="g:name" /></name>
			<Style>
				<LineStyle>
					<color>FFFF0000</color>
					<width>1</width>
				</LineStyle>
			</Style>
			<LineString>
				<coordinates>
					<xsl:apply-templates select="g:trkseg/g:trkpt" />
				</coordinates>
			</LineString>
		</Placemark>
	</xsl:template>
	
	<xsl:template match="g:trkseg/g:trkpt">
		<xsl:value-of select="@lon" />,<xsl:value-of select="@lat" />,<xsl:value-of select="g:ele" />
		<xsl:text disable-output-escaping="yes"><![CDATA[ ]]></xsl:text>
	</xsl:template>
</xsl:stylesheet>