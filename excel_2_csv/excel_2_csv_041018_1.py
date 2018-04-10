# -*- coding: utf-8 -*-

#! python3

# USAGE
# python3 excel_2_csv_041018_1.py "FOLDERWITHEXCEL"

import os,sys,csv,openpyxl

import logging
logging.basicConfig(level=logging.DEBUG, format=" %(asctime)s - %(levelname)s - %(message)s")
# logging.disable(logging.CRITICAL)

#####################################
# COMMAND LINE PARSING
#####################################

input_folder = sys.argv[1] # should be "FOLDERWITHEXCEL", which should be a path
logging.debug('The input folder targeted is:  %s' % (input_folder))

#####################################
# END COMMAND LINE PARSING
#####################################

#####################################
# ANALYZE FILES
#####################################

for file in os.listdir(input_folder):
	# check that file is an Excel file
	if endswith('xlsx'):
		pass

#####################################
# END ANALYZE FILES
#####################################

