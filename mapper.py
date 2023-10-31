# -*- coding: utf-8 -*-
#!/usr/bin/env python 
  
# import sys because we need to read and write data to STDIN and STDOUT 
import sys  
for line in sys.stdin:  
    line = line.strip()  
    words = line.split()  
    for word in words:  
        print ('%s\t%s'%(word,1))
