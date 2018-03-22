# -*- coding: utf-8 -*-
"""
Created on Thu Mar 22 10:29:50 2018

@author: LAC40641
"""
# ---------- > WORKINGDIRECTORY
import os
working_directory = 'C:\\Users\\LAC40641\\Desktop\\clasespy'
os.chdir(working_directory)
# < ---------- WORKINGDIRECTORY

import auto as a
import camion as c
import pandas as pd
import libreria as lib

fordka = a.Auto('Ford', 'ka')
merc01 = c.Camion('Mercedez', '01')

fordka.wheels
merc01.wheels


fordka.vehicle_type()
merc01.vehicle_type()

fordka.numsum(40)
merc01.numsum(40)

lib.printpantalla()

