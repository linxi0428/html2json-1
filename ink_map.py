#!/usr/bin/env python
# -*- coding: utf-8 -*-
# python HTML >> JSON
# 
# nabster, December 2014

#=========================================#
# PRE-PROCESS REGEX                       #
#=========================================#

## ALL DATES
# ^.*\[(.*)\].*\n.*DE(\d*)A(\d*)/(.*)/.*$
# map["_\2_\3"]["\4"] = [\1]

## LOCAL DATES
# ^.*\[(.*)\].*\n.*DE(\d*)A(\d*)/(.*)/.*$\s*
# map["\4"] = [\1]\n

#=========================================#
# MAP                                     #
#=========================================#

map = {}

# 600-700
map["kairouan"] = [35.674963,10.094005]
map["aqsa"] = [32.0779374,35.2353378]
map["rocher"] = [31.7779374,35.2353378]
# 700-800
map["kairouan"] = [35.674963,10.094005]
map["damas"] = [33.511637, 36.306584]
# 800-900
map["djenne"] = [13.9052, -4.5553]
# 900-1000
map["djenne"] = [13.9052, -4.5553]
# 1000-1100
map["djenne"] = [13.9052, -4.5553]
# 1100-1200
map["djenne"] = [13.9052, -4.5553]
# 1200-1300
map["djenne"] = [13.9052, -4.5553]
# 1300-1400
map["1314 - Ozbek Han Mosque"] = [45.029167, 35.088611]
# 1400-1500
map["1421-1451, Mosquee Dzhumaya, Plovdiv"] = [42.135404,24.74566]
# 1500-1600
map["nusrat"] = [55.676139,12.568594]
# 1600-1700
map["nusrat"] = [55.676139,12.568594]
# 1700-1800
map["nusrat"] = [55.676139,12.568594]
# 1800-1900
map["nusrat"] = [55.676139,12.568594]
# 1900-2000
map["nusrat"] = [55.676139,12.568594]
# 2000-2100
map["alaska"] = [61.14,-149.86]
map["bigtirana"] = [41.33,19.83]
map["cecisuisse"] = [47.37,8.51]
map["cologne"] = [50.94,6.95]
map["pristinamayesh"] = [43,20.96]
map["pristina301"] = [42.77,20.86]
map["pristinadurigag"] = [42.87,21.46]
map["pristinadarvuga"] = [42.65,21.70]
map["pristinaaptum"] = [42.67,21.16]
map["pristinavictoloq"] = [42.47,20.96]
map["cambridge"] = [52.206927,0.122181]
map["strasbourg"] = [48.587963,7.7425]
map["halide"] = [41.005316,28.976966]
map["calmica"] = [41.2,28.8]
map["rayoflight"] = [25.271911,55.307922]
map["mosqueville"] = [25.5,55.3]
map["blondel"] = [50.635025,5.581049]
map["sphere"] = [38.731088,35.479095]
map["kremlin"] = [55.798469, 49.104811]
map["rijeka"] = [45.328979,14.439754]
map["slovenia"] = [46.051791,14.511452]
map["copen"] = [55.676139,12.568594]
map["marseille"] = [43.296466,5.369771]
map["alger"] = [36.75343,3.04239]
map["mashkur"] = [52.286504,76.962168]
map["haram"] = [21.422876,39.825735]