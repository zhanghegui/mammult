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
## Take as input the layers of a multiplex, and provide as output a
## file where the n-th line contains the activity of the n-th node. We
## assume that nodes are numbered sequentially, starting from 0, with
## no gaps (i.e., missing nodes are treated as isolated nodes)
##
##
##


import sys

if len(sys.argv) < 2:
    print "Usage: %s <layer1> [<layer2>...]" % sys.argv[0]
    sys.exit(1)

node_activity = {}

max_N = -1

for layer in sys.argv[1:]:
    active = []
    with open(layer, "r") as lines:
        for l in lines:
            if l[0] == "#":
                continue
            
            s, d = [int(x) for x in l.strip(" \n").split(" ")[:2]]
            active.extend([s,d])
            if s > max_N:
                max_N = s
            if d > max_N:
                max_N = d
        active = set(active)
        for n in active:
            if n in node_activity:
                node_activity[n] += 1
            else:
                node_activity[n] = 1
    

for n in range(max_N+1):
    if n in node_activity:
        print node_activity[n]
    else:
        print 0




