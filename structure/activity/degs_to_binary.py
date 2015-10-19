# This file is part of MAMMULT: Metrics And Models for Multilayer Networks
# 
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or (at
# your option) any later version.
# 
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
####
##
## Take a file which contains, on the n-th line, the degrees at each
## layer of the n-th node, and print on output the corresponding node
## participation bit-strings, i.e. the string which contains "1" if on
## that layer the node is connected, and zero otherwise
## 
## on the stderr, we also dump the distribution of each bit-string
##


import sys

def to_binary(l):
    s = 0
    e = 0
    for v in l:
        s += v * pow(2,e)
        e +=1
    return s

if len(sys.argv) < 2:
    print "Usage: %s <filein>" % sys.argv[0]
    sys.exit(1)

distr = {}

with open(sys.argv[1]) as f:
    for l in f:
        elems = [int(x) for x in l.strip(" \n").split(" ")]
        new_list = [1 if x>0 else 0 for x in elems]
        val = to_binary(new_list)
        if val in distr:
            distr[val] += 1
        else:
            distr[val] = 1
        for i in new_list:
            print i,
        print

for k in distr:
    bin_list = bin(k)
    bin_num = sum([int(x) if x=='1' else 0 for x in bin_list[2:]])
    sys.stderr.write("%d %028s %d \n" % (bin_num, bin_list[2:], distr[k]))
    
