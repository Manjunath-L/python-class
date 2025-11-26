import re
text = "Python is supper super super easy"
regex = r"super|"
data1 = re.findall(regex,text,re.IGNORECASE)
print(data1)

#---------str(*) metachar ---------
import re
text ="a python is ython not pppython and pppppython"
regex = r"p*ython"
data1 = re.findall(regex,text,re.IGNORECASE)
print(data1)

#------------ pluse(+) metachar ------------
import re
text ="a python is ython not pppython and pppppython"
regex = r"p+ython"
data1 = re.findall(regex,text,re.IGNORECASE)
print(data1)

# =--------- ? metechar --------------

import re
text ="a python is ython not pppython and pppppython"
regex = r"p?ython"
data1 = re.findall(regex,text,re.IGNORECASE)
print(data1)

# --------------- Hat(^) metechar ------------
import re
text ="a python is ython not pppython and pppppython"
regex = r"^a"
data1 = re.findall(regex,text,re.IGNORECASE)
print(data1)

# ------------------ $ metachar ------------
import re
text ="a python is ython not pppython and pppppython"
regex = r"ppppthon$"
data1 = re.findall(regex,text,re.IGNORECASE)
print(data1)

# ------------------ char([]) metachar ------------
import re
text ="a python is ython not pppython and pppppython"
regex = r"[p]"
data1 = re.findall(regex,text,re.IGNORECASE)
print(data1)

# -------------------- flowerbrase {} metechar
import re
text ="a python is ython not pppython and pppppython"
regex = r"p{,3}ython"
data1 = re.findall(regex,text,re.IGNORECASE)
print(data1)