
## remove puncution from end of string, not in middle

import string 
import re
punctuation_list =  list(string.punctuation)
ws = ["@#haythem..!","is","eating","tac.os.",".haythem","love's","tacos","",":"]
for w in ws: 
    w = re.sub('([^a-zA-Z0-9]+$|^[^a-zA-Z0-9]+)', '', w)
    print(w)
