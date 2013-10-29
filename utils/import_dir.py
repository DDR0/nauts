#Python 2.
#Usage: Run in a directory full of images to generate a directory full of .cfg files.
import os
from PIL import Image

files = os.listdir(".")

pathFragment = os.getcwd()[os.getcwd().find('images/')+len('images/'):]
print(pathFragment)

#Create a _new_ folder for our output, to avoid creaming something.
outpath_base = "output"
outpath_counter = 1
outpath = outpath_base
while os.path.exists(outpath):
	outpath_counter += 1
	outpath = outpath_base + str(outpath_counter)
os.makedirs(outpath)

#Unfortunantly, format relies on the {} characters. Which are part of json. So, to escape them, we double them in the template.
template = """{{
id: "{0}",
next_animation: "'normal'",
always_active: false,

//zorder: "@include data/zorder.cfg:",

editor_info: {{
	category: "unprocessed ???",
	help: "Generated with import_dir.py.",
}},

on_end_anim: "animation('normal')",
animation: {{
	id: "normal",
	image: "{3}/{0}.png",
	scale: 1,
	x: 0,
	y: 0,
	w: {1},
	h: {2},
	//collide: [0,0,{1},{2}],
	frames: 1,
	duration: 100000000,
}},
}}"""

for file in files:
	if file[-4:] == ".png":
		filesize = Image.open(file).size
		
		newObject = template.format(file[:-4], filesize[0], filesize[1], pathFragment)
		newFilePath = outpath+'/'+file[:-4]+'.cfg'
		
		print('writing '+outpath+'/'+file[:-4]+'.cfg')
		with open(outpath+'/'+file[:-4]+'.cfg', mode='wt') as output:
			output.write(newObject)