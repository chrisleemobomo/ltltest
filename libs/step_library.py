
"""
this script requires json2html 

>>> pip install json2html
"""


import os
import re
import json
from json2html import *

STEP_DIRECTORIES = ["./../libs", "./../proj"]



def get_modules_from_path(testpath):
    """ Retrns a list of all TESTCASE_TEMPLATE_NAME.feature files within the 
            given directory.
            TODO: Ad as well more intermidiate configuration files
    """
    modulepaths = []
    for base_dir, folders, files in os.walk(testpath):
        modulepaths.extend([os.path.join(base_dir, f) for f in files if f.endswith('.py')])
    return modulepaths

modulepaths = []
for d in STEP_DIRECTORIES:
	modulepaths.extend(get_modules_from_path(d))

step_library = {}
for m in modulepaths:
	file = m.split("/")[-1].replace(".py","")
	steps = []
	with open(m, "r") as rh:
		lines = rh.readlines()
	for l in lines:
		if l.lstrip().startswith("@step("):
			step = re.search("\'(.+)\'", l).group(1)
			step = step.replace("\n", "")
			step = step.replace("{}", "(id|n|x|lt|plt|tn|cn|cs)")
			step = step.replace("{0}", "(id|n|x|lt|plt|tn|cn|cs)")
			step = step.replace("([^\"]*)", "value")
			steps.append( step )
	if steps:
		step_library[file] = {}
		step_library[file]["path"] = m.replace("./..", "")
		step_library[file]["steps"] = steps

with open("step_library.json", "w") as wh:
	json.dump(step_library, wh)

html = """
<html>
<head>
<link rel="stylesheet" href="https://maxcdn.bootstrapcdn...">
</head>
<body>
"""

for sm in step_library:
	html += "<h1>{}</h1>".format(sm)
	html += json2html.convert(json=step_library[sm])

html += "</body></html>"

with open("step_library.html", "w") as wh:
	wh.write(html)