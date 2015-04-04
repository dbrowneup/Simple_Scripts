#! /usr/bin/env python

from __future__ import print_function
from pyfaidx import Fasta
import sys, getopt

def usage():
	print("usage: python extract_unigene_isoforms.py -q <gene_list.txt> -f <Trinity_assembly.fa> -o <output_file.fa>")

#Parse list of gene IDs and extract isoforms from assembly
def extract_sequences(targs, db, out):
	target_file = open(targs, "r").read().split('\n')
	if target_file[len(target_file)-1] == '':
		del target_file[len(target_file)-1]
	output_file = open(out, "w")
	database_file = Fasta(db)
	for i in database_file:
		for x in target_file:
			if x in i.name:
				print(">"+i.name, file=output_file)
				for line in i:
					print(line, file=output_file)
	output_file.close()

#Load list of target sequences and define database and output files
#Then call function to execute sequence extraction
def main(argv):
	target_file = ''
	database_file = ''
	output_file = ''
	try:
		opts, args = getopt.getopt(argv, "hq:f:o:")
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	for opt, arg in opts:
		if opt == "-h":
			usage()
			sys.exit()
		elif opt == "-q":
			target_file = arg
		elif opt == "-f":
			database_file = arg
		elif opt == "-o":
			output_file = arg
	extract_sequences(target_file, database_file, output_file)

if __name__ == "__main__":
	main(sys.argv[1:])