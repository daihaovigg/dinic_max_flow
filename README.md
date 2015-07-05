# Dinic's Maximum network flow algorithm
Dinic’s algorithm is a polynomial algorithm for computing the maximum network flow in a
network. It is similar to Edmond-Karp’s algorithm which run in O(nm<sup>2</sub>) time and runs in
O(n<sup>2</sub>m).


Input graph has to be in DIMACS graph format

Example input can be found in sample_input.txt


example run:

./maxflowsolve.py -i input_graph.txt -o output_file

where
 i = input file
 o = output file

To read from stdin and to write to stdout, dont specify the -i or -o options