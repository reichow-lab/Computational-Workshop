from glob	import glob
from sys	import argv
from matplotlib import pyplot as plt 
import re
"""
Up above I am using two libraries that are not automatically built into python. They allow us to use certain functionalities
that we would otherwise have to create ourselves.

Glob is a library that allows us to search through directories via python.

Sys is a library that allows us to communicate with the command line, and argv is a specific method (function) in the sys 
library that lets us put command-line arguments into our program as variables.

Re (regular expression), is a library that allows us to use grep-like functionalities in python.
"""

script, path2star, outname = argv

starlist = glob((path2star + '/*.star'))

starlist.sort()

classd_end	= outname + '_rlnClassDistribution.txt'
accrot_end	= outname + '_rlnAccuracyRotations.txt'
acctra_end	= outname + '_rlnAccuracyTranslations.txt'

classd		= open(classd_end, 'w')
accrot		= open(accrot_end, 'w')
acctra		= open(acctra_end, 'w')

iteration	= 0

for starfile in starlist:

	with open(starfile) as star:

		classd.write(str(iteration) + '\t') 
		accrot.write(str(iteration) + '\t') 
		acctra.write(str(iteration) + '\t') 

		iteration += 1

		for line in star:

			if re.search('Class3D', line):

				val = line.split()

				classd.write(str(val[1]) + '\t')
				accrot.write(str(val[2]) + '\t')
				acctra.write(str(val[3]) + '\t')

		classd.write('\n')
		accrot.write('\n')
		acctra.write('\n')

classd.close()
accrot.close()
acctra.close()
