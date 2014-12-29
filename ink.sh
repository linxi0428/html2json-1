#!/bin/bash
#
# script runner
# 
# nabster, December 2014


printf "\n\n\n\n\n\n"
echo "	                      XXXXXXXXXXXXXXXXX"
echo "	                  XXXXX             XXXXXXXX"
echo "	               XXXX                       XXXX"
echo "	              XXX                           XXX"
echo "	             XX                               XX"
echo "	            XX                                 XX"
echo "	           XX                                   XX"
echo "	           XX XXX                            XX XX"
echo "	           XX XX                             XX  X"
echo "	           XX XX                             XX  X"
echo "	           XX  XX                            XX  X"
echo "	           XX  XX                           XX  XX"
echo "	            XX XX   XXXXXXXX      XXXXXXX   XX XX"
echo "	             XXXX XXXXXXXXXX     XXXXXXXXXX XXXXX"
echo "	              XXX XXXXXXXXXX     XXXXXXXXXX XXX"
echo "	     XXX       XX  XXXXXXXX       XXXXXXXXX  XX      XXXX"
echo "	    XXXXX     XX   XXXXXXX   X X   XXXXXXX   XX     XXXXXX"
echo "	   XX   XX    XX     XXX    XXXXX    XXX     XX    XX   XX"
echo "	  XXX    XXXX  XX          XXX XXX          XX  XXXX    XXX"
echo "	 XXX         XXXXXXX       XXX XXX       XXXXXXXXX        XX"
echo "	 XXXXXXXXX     XXXXXXXX    XXX XXX    XXXXXXXX      XXXXXXXX"
echo "	   XXXX XXXXX      XXXXX              XXX XX     XXXXXX XXX"
echo "	           XXXXXX  XXX XX           XX XXX  XXXXXX"
echo "	               XXXXXX X  XXXXXXXXXXX XX XXXXXX"
echo "	                   XX X XX XX X XXXXXXX XX"
echo "	                 XXXX XX X XX X XX X XX XXXXX"
echo "	             XXXXX XX   XXXXXXXXXXXXX   XX XXXXX"
echo "	     XXXXXXXXXX     XX                 XX       XXXXXXX"
echo "	   XXXXXX        XXXXXXX            XXXX          XXXXXXX"
echo "	    XXXXX       XXXXXX                XXX       XXXXXXX"
echo "	        XXXX  XXXXX                     XXX    XXX"
printf "\n\n\n\n\n\n"

# READ DIRECTORY

python ink.py alaska
python ink.py alger
python ink.py bigtirana
python ink.py blondel
python ink.py calmica
python ink.py cambridge
python ink.py cecisuisse
python ink.py cologne
python ink.py copen
python ink.py halide
python ink.py haram
python ink.py kremlin
python ink.py marseille
python ink.py mashkur
python ink.py mosqueville
python ink.py pristina301
python ink.py pristinaaptum
python ink.py pristinadarvuga
python ink.py pristinadurigag
python ink.py pristinamayesh
python ink.py pristinavictoloq
python ink.py rayoflight
python ink.py rijeka
python ink.py slovenia
python ink.py sphere
python ink.py strasbourg

cd ..

cat *.jsont >> data.json
rm *.jsont

