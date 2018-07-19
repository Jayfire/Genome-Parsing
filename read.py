genome_file = open("new.txt","r")
#output = open("new.txt","w")
contents = ''
count = 0
cutoff = ''
#with open("Pseudomonas","rb") as f:
    #contents = f.read()
for line in genome_file:
    #if isInt(line): continue
    #if not isString: continue
    temp = line[10000000:18000000].replace('\\t','    ').replace('\\n','').replace("'",'')
    tempstr = temp.split('b')

    print(tempstr)
    break
