#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
import os.path
from Bio import SeqIO
from gzip import GzipFile

def open_fasta_with_biopython(filename):
	return [rec for rec in SeqIO.parse(filename, "fasta")]

def open_compressed_fasta_with_biopython(filename):
	with GzipFile(filename) as f:
		return [rec for rec in SeqIO.parse(f, "fasta")]

def open_compressed_fasta_with_biopython_and_generator(filename):
	with GzipFile(filename, mode='r') as f:
		for line in f:
			if chr(line[0]) == '>':
				yield line.decode('utf-8').strip()

if __name__ == "__main__":
	ressource_folder = os.path.join(os.path.abspath('..'), 'ressources')
	# file
	# filename = 'Homo_sapiens.GRCh38.dna.chromosome.1.fa.gz'
	filename = 'Homo_sapiens.GRCh38.dna.toplevel.fa.gz'

	ressource_file = os.path.join(ressource_folder, filename)
	# fasta_ressource = open_fasta_with_biopython(ressource_file)
	# for f in fasta_ressource:
	# 	print(f.id)

	fasta_ressource = open_compressed_fasta_with_biopython_and_generator(ressource_file)
	# for f in fasta_ressource:
	# 	print(f)

	# lambda
	extract_id = lambda x: x.split(' ')[2]
	for f in fasta_ressource:
		header_id = extract_id(f)
		print(header_id)
