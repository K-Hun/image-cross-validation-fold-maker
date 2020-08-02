import subprocess as sbp
import os
import os, shutil
from pathlib import Path
from random import shuffle
import time


def create_classes_empty_dir(labels, path):
	for label in labels:
		Path(os.path.join(path, label)).mkdir(parents=True, exist_ok=True)
	delete_files(path)

def delete_files(folder_path):
	folder = folder_path
	for filename in os.listdir(folder):
		file_path = os.path.join(folder, filename)
		try:
			if os.path.isfile(file_path) or os.path.islink(file_path):
				os.unlink(file_path)
			elif os.path.isdir(file_path):
				delete_files(file_path)
		except Exception as e:
			print('Failed to delete %s. Reason: %s' % (file_path, e))	


def merg_two_dirs(folder1_path, folder2_path):
	path = folder1_path
	fol = os.listdir(path)
	p2 = folder2_path

	for i in fol:
		p1 = os.path.join(path,i)
		p3 = 'cp -r ' + p1 +' ' + p2+'/.'
		print(p3)
		proc=sbp.Popen(p3,shell=True)
		proc.wait()

def merge_folds(folds_path, output_path, total_folds, excepted_fold = 0):
	for i in range(1,total_folds+1):
		if i == excepted_fold:
			continue
		merg_two_dirs(os.path.join(folds_path, "fold"+str(i)), output_path)
#exit()
def make_folds(dataset_path, output_path, labels, folds_count):
	for i in range(1, folds_count + 1):
		create_classes_empty_dir(labels, os.path.join(output_path, 'folds/fold'+str(i)))
	for label in labels:
		listOfFiles = os.listdir(os.path.join(dataset_path, label))
		fold_size = int(len(listOfFiles)/folds_count)
		shuffle(listOfFiles)
		for j in range(folds_count):
			first = j * fold_size
			if first > len(listOfFiles) - 1:
				break
			last = (j + 1) * fold_size
			
			if last > len(listOfFiles) - 1:
				last = len(listOfFiles) - 1
			print('fold#'+str(j+1),label,'[', first, last + 1,']')
			for k in range(first, last):
				shutil.copy(os.path.join(dataset_path, label + '/' + listOfFiles[k]),
					os.path.join(output_path, 'folds/fold'+str(j+1)+'/'+label))



# TODO
def check_feasibility(labels, dataset_path, folds_count):
	isFeasible = True
	for label in labels:
		print(label, len(os.listdir(os.path.join(dataset_path, label))))
