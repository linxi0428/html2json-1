#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python HTML >> JSON
# 
# nabster, December 2014
#
#	                      XXXXXXXXXXXXXXXXX
#	                  XXXXX             XXXXXXXX
#	               XXXX                       XXXX
#	              XXX                           XXX
#	             XX                               XX
#	            XX                                 XX
#	           XX                                   XX
#	           XX XXX                            XX XX
#	           XX XX                             XX  X
#	           XX XX                             XX  X
#	           XX  XX                            XX  X
#	           XX  XX                           XX  XX
#	            XX XX   XXXXXXXX      XXXXXXX   XX XX
#	             XXXX XXXXXXXXXX     XXXXXXXXXX XXXXX
#	              XXX XXXXXXXXXX     XXXXXXXXXX XXX
#	     XXX       XX  XXXXXXXX       XXXXXXXXX  XX      XXXX
#	    XXXXX     XX   XXXXXXX   X X   XXXXXXX   XX     XXXXXX
#	   XX   XX    XX     XXX    XXXXX    XXX     XX    XX   XX
#	  XXX    XXXX  XX          XXX XXX          XX  XXXX    XXX
#	 XXX         XXXXXXX       XXX XXX       XXXXXXXXX        XX
#	 XXXXXXXXX     XXXXXXXX    XXX XXX    XXXXXXXX      XXXXXXXX
#	   XXXX XXXXX      XXXXX              XXX XX     XXXXXX XXX
#	           XXXXXX  XXX XX           XX XXX  XXXXXX
#	               XXXXXX X  XXXXXXXXXXX XX XXXXXX
#	                   XX X XX XX X XXXXXXX XX
#	                 XXXX XX X XX X XX X XX XXXXX
#	             XXXXX XX   XXXXXXXXXXXXX   XX XXXXX
#	     XXXXXXXXXX     XX                 XX       XXXXXXX
#	   XXXXXX        XXXXXXX            XXXX          XXXXXXX
#	    XXXXX       XXXXXX                XXX       XXXXXXX
#	        XXXX  XXXXX                     XXX    XXX


#=========================================#
# IMPORTS                                 #
#=========================================#

from bs4 import BeautifulSoup
from ink_map import *
import re
import json
import sys

# cordoue
# damas
# kairouan

#=========================================#
# FUNCTIONS                               #
#=========================================#

def clear_spaces(_input):
    """
    Clears spaces and lines
    """
    _input = re.sub(r"^[\n\s\r]*", "", _input, re.MULTILINE)
    _input = re.sub(r"[\n\s\r]*$", "", _input, re.MULTILINE)

    return _input

#=========================================#
# PROCESS                                 #
#=========================================#

if (not sys.argv):
	print "Please enter file name"
	exit()

# GET HTML FILE
html = BeautifulSoup(open("../" + sys.argv[1] + "/fiche.html"))

# NAME
name = clear_spaces(html.big.string)

# SUBTITLE
title = clear_spaces(html.findAll("font", { "size" : "4pt" })[0].string)

# SOURCES
sources = clear_spaces(html.a['href'])

# DESCRIPTION
descs = html.findAll("p", { "align" : "justify" })
description = list();
for desc in descs:
    description.append(clear_spaces(desc.string))

# MEDIAS
meds = html.findAll("a", { "rel" : "shadowbox[test2]" })
medias = list();
for med in meds:
	img = re.search('^images/(.*)\..*$', med.get('href'), re.IGNORECASE)
	if img:
	    med = img.group(1)
	medias.append(med)

# OUTPUT TO JSON
with open('../' + sys.argv[1] + '.jsont', 'w') as output:
	json.dump(
		{
			"name":name,
			"title":title,
			"subtitle":title,
			"sources":sources,
			"folder":sys.argv[1],
			"description":description,
			"latLng":map[sys.argv[1]],
			"medias":medias
		},
		output
	)