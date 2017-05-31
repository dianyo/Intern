import sys
import collections
files = []
for line in sys.stdin:
	if line == "]\n":
		break
	if line == "urls = [\n":
		continue
	start = line.rfind('/') + 1
	end = line.rfind('\"')
	fileName = line[start:end]
	files.append(fileName)

x = collections.Counter(files)
most = x.most_common(3)

for ele,count in most:
	print(str(ele) + " " + str(count))