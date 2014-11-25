import numpy as np
import os
import re
import sys

filelist = []
filelink = {}
linkcount = {}
pagerank = {}
target = {}
totrank = []

def scan_txt(dir, query):	
	global filelist
	global filelink
	global linkcount
	global target
	
	pattern = re.compile("[a-zA-Z0-9]+\\.txt")
	query = re.compile(query)
	filelist = os.listdir(dir)
	for file in filelist:
		linkcount[file] = 0
		content = open(dir+'/'+file, 'r').read()
		
		#mat = pattern.search(content)		
		#if mat:
			#print file + " YOOOOOOOOOO"
			#print mat.group(1)
			
		#print file + ":::"
		#print re.findall("[a-zA-Z0-9]+\\.txt", content)
		for link in re.findall("[a-zA-Z0-9]+\\.txt", content):
			if not link in filelink:
				filelink[link] = {}
			if not file in filelink[link]:
				filelink[link][file] = True
				linkcount[file] += 1
		if query.search(content):
			target[file] = True
	#print linkcount
	
def drop_dead_end(droped, linkcnt):
	global filelist
	global linkcount
	global filelink
	global pagerank
	global totrank
	global target
	
	dead_end = False 
	for file in filelist:
		if file in droped:
			continue
		if linkcount[file] == 0: 
			droped[file] = True
			for link in filelink[file].keys():
				linkcnt[link] -= 1
			drop_dead_end(droped, linkcount)
			linkcnt[link] += 1
			pagerank[file] = 0
			#print file+":"
			
			for link in filelink[file].keys():
				#print link + " : " + str(linkcount[link])
				pagerank[file] += pagerank[link]/linkcount[link]
			
			#print pagerank[file]
			if file in target:
				totrank.append((file, pagerank[file]))
			dead_end = True
			break
	
	if not dead_end:
		idx = {}
		ridx = []
		cnt = 0
		cons = []
		coe = []
		subco = []
		#print linkcount
		for file in filelist:
			if file in droped:
				continue
			idx[file] = cnt
			ridx.append(file)
			coe.append([])
			cnt += 1
			cons.append(0)
		
		for file in filelist:
			if file in droped:
				continue
			subco = cons[:]
			for link in filelink[file].keys():
				if file in droped:
					continue
				elif idx[link]==0:
					cons[idx[file]] = -1.0/linkcnt[link]
				else:
					subco[idx[link]] = 1.0/linkcnt[link]
			if idx[file]==0:
				cons[idx[file]] = 1
			else:
				subco[idx[file]] = -1
			#print file + ":"
			#print filelink[file].keys()
			#print subco
			coe[idx[file]] = subco[:]
			
		result = np.linalg.solve(np.array(coe), np.array(cons))
		result[0] = 1
		i = 0
		for rank in result:
			pagerank[ridx[i]] = rank
			#print ridx[i]+":"
			#print pagerank[ridx[i]]
			if ridx[i] in target:
				totrank.append((ridx[i], rank))
			i += 1

scan_txt(sys.argv[1], sys.argv[2])
#print filelink
drop_dead_end({}, linkcount)
i = 1
print "rank\tfilename"
for filerank in sorted(totrank, reverse=True, key = lambda x : x[1]):
	print str(i) + "\t" + filerank[0]
	i += 1
