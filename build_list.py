import numpy as np
import itertools 
import os
import argparse
from scipy.misc import comb
from pprint import pprint

# Say a list of the following type has been generated:
# [[site1, [site11, [valid_sites]], [site1, [site2,[valid_sites]]]], [site2,[...]]]
class BuildSet(object):
    def __init__(self, configs=[]):
        self.configs = []
    def dist(a,b):
      dist_param = 1.3
      if(np.sqrt((a-b).dot(a-b)) > dist_param):
      	bool = True
      else:
      	bool = False
      return bool

# Given a lattice a number of items are recursively deposited on the lattice
# with the lattice being truncated at each step according to some condition
# the dist method. This should be generalized so I have a generic function
# for truncating the lattice at each step.
		def recursive_decorate_stack(lattice, depth):
		  n = 0
		  configs = [] 
		  while (n < len(lattice)): 
		        lattice_prune = []
		        config  = lattice[n]
		        if (depth > 1) :
		  	    for site in lattice:
		  	    	if (self.dist(config, site) == False): 
		  	        	pass
		  		else:
		  			lattice_prune.append(site)
		            configs.append([config, recursive_decorate_stack(lattice_prune, depth-1)])
		        elif (depth ==1):
		  	    return lattice
		        n += 1
      return configs

# backtrack_recurse takes a nested list and recursively builds up a flattened
# list from all the combinations. Upon building that list the 
# object has a method to build a set out
# of that list. The sites are np.arrays.
    def backtrack_recurse(self, nested_list, config, depth):
        n = 0
        if depth > 2:
            config = config + [nested_list[0]]
            for site in nested_list[1]:
                if len(site) > 2 :
                    config += [site[0]]
                    self.backtrack_recurse(site[1], config, depth-1)
                    config.pop()
                else :
                    self.backtrack_recurse(site, config, depth-1)
        elif depth == 2:
            n = 0
            config = config + [nested_list[0]]
            for site in nested_list[1]:
                config = config + [site]
                #Sort list here:
                a = sorted(config, key=lambda x : (x[0],x[1]))
                a = (tuple(vec) for vec in a)
                #print 'a', a
                self.configs.append(a)
                config.pop()
        return

    def prune_configs(self):
        self.configs = set(map(tuple, self.configs))
        return
