import sys
class helper:
    def __init__(self):
        pass
    @staticmethod
    def init(args, vertex, cap, flow, level, path, numnodes):
        sources = []
        sinks = []
        #read in graph
        if(args.infile != None):
            for line in args.infile:
                record = line.strip().split(" ")
                if line[0] =='p':
                    numnodes = int(record[2]) + 2 #make space for super node and sink
                    for i in range(numnodes):
                        vertex.append([])
                        cap.append({})
                        flow.append({})
                        level.append(0)
                        path.append(None)
                elif line[0] == "n":
                    if record[2] =="s":
                        sources.append(int(record[1]))
                    else:
                        sinks.append(int(record[1]))
                elif line[0]=="a":
                    head = int(record[1])
                    tail = int(record[2])
                    vertex[head].append(tail)
                    cap[head][tail] = int(record[3])
                    flow[head][tail] = 0
        else:
            print "First enter p record e.g p max 10 15 \n then enter edge line by line in the format a head tail cap \n next enter the n records e.g n 1 s\n Press enter each time. \nPress enter twice when done."
            line = raw_input("==> ")
            while line !="":
                record = line.strip().split(" ")
                if line[0] =='p':
                    numnodes = int(record[2]) + 2 #make space for super node and sink
                    for i in range(numnodes):
                        vertex.append([])
                        cap.append({})
                        flow.append({})
                        level.append(0)
                        path.append(None)
                elif line[0] == "n":
                    if record[2] =="s":
                        sources.append(int(record[1]))
                    else:
                        sinks.append(int(record[1]))
                elif line[0]=="a":
                    head = int(record[1])
                    tail = int(record[2])
                    vertex[head].append(tail)
                    cap[head][tail] = int(record[3])
                    flow[head][tail] = 0
                line = raw_input("==> ")
        #support multiple sources and sinks
        #create super node if multiple sink and source
        for i in sources:
            vertex[0].append(i)
            flow[0][i] = 0
            cap[0][i] = sys.maxint
        for i in sinks:
            vertex[i].append(len(vertex) -1)
            flow[i][len(vertex) -1] = 0
            cap[i][len(vertex) -1] = sys.maxint
        return vertex, cap, flow, level, path, numnodes

    #write output to file
    @staticmethod
    def writeGraph(args, vertex, flows, max_flow):
        if(args.output != None):
            with open(args.output,"w") as f:
                for i in range(1, len(vertex) -1):
                    for j in vertex[i]:
                        if j != len(vertex) -1:
                            f.write("f "+ str(i)+" "+ str(j) +" "+ str(flows[i][j]))
                f.write("s "+str(max_flow))                
                f.flush()
        else: #no output file. Write to stdout
            for i in range(1, len(vertex) -1):
                for j in vertex[i]:
                    if j != len(vertex) -1:
                        print "f", str(i), str(j), str(flows[i][j])
            print "s",str(max_flow)
