#! /usr/bin/python3
import math
from leaf import draw_leaf,get_max,get_min,get_banana

#max canvas size
X_MAX=200
Y_MAX=30
#set origin (100,50)
OX=100
OY=15
#leaf_attach_coordinate (100,40)
ACX=99
ACY=15
#tot_char set
TOT_CHAR_SET={'-','|','\\','/','=',"^"}
#colors :)
END='\033[0m'
GREEN='\033[92m'
YELLOW='\033[93m'
RED='\033[91m'
CYAN='\033[96m'

def mirror_leaf(leaf):
	org_x=0
	org_y=2
	LX_MAX,LY_MAX=get_max(leaf)
	leaf_mir=[[" " for x in range(X_MAX)] for y in range(Y_MAX)]	
	for y in range(LY_MAX):
		for x in range(LX_MAX):
			leaf_mir[y+org_y][((int((OX*3)/2))-x-1)+org_x]=leaf[y][x]
	"""
	for y in range(LY_MAX):
		for x in range(x_MAX):
			print(leaf_mir[y][x],end="")
		print("")	
	"""
	return leaf_mir
	
def rotate_leaf(leaf,rot_fac):
	THETA=rot_fac
	LX_MAX,LY_MAX=get_max(leaf)
	rot_x=X_MAX
	rot_y=Y_MAX
	org_x=48
	org_y=12
	leaf_rot=[[" " for x in range(rot_x)] for y in range(rot_y)]	
	cos_t=math.cos(math.radians(THETA))	
	sin_t=math.sin(math.radians(THETA))
	for y in range(LY_MAX):
		for x in range(LX_MAX):
			#     [ [cos_t,sin_t],[-sin_t,cos_t] ] * [ x , y ]                           
			#lenear transformation go brrr :)
			x_coord=org_x+x*cos_t+y*sin_t
			y_coord=org_y+x*sin_t*(-1) +y*cos_t
			x_co=int(x_coord)
			y_co=int(y_coord)
			leaf_rot[y_co][x_co]=leaf[y][x]	  
	"""
	for y in range(rot_y):
		for x in range(rot_x):
			print(leaf_rot[y][x],end="")
		print("")		  
	"""
	return leaf_rot

def vazha_color(ascii_char):	
	if ascii_char=="^" or ascii_char=="-":
		return GREEN+ascii_char+END
	elif ascii_char in ['|','\\','=']:
		return YELLOW+ascii_char+END
	if ascii_char=="||":
		return RED+ascii_char+END
	else:
		return ascii_char	

def attach_leaf(leaf,rot_fac,mirror=False):
	leaf_shift=[[" " for x in range(X_MAX)] for y in range(Y_MAX)]	
	LX_MAX,LY_MAX=get_max(leaf)
	#print("max >> : ",LX_MAX,LY_MAX)
	#find y_coord of x_max :)
	y_coord=0
	for y in range(Y_MAX):
		if leaf[y][LX_MAX]=="-" or leaf[y][LX_MAX]=="^":
			if y>y_coord:
				y_coord=y

	#print("attach_point >> : ",LX_MAX,y_coord)
	beautify=0
	if rot_fac > 4 :
		beautify=2
	if not mirror:
		#ORIGIN ==> (100,15)
		org_y=OY+y_coord+beautify
		#+beautify just to beautify :)
		org_x=OX+LX_MAX+beautify
		for y in range(Y_MAX):
			for x in range(X_MAX):
				leaf_shift[y-org_y][x-org_x]=leaf[y][x]
	else:
		#ORIGIN ==> (100,15)
		#org_y=OY+y_coord
		#+beautify just to beautify :)
		#org_x=OX+LX_MAX+beautify
		org_x=int((3*OX)/2)+4
		org_y=1

		for y in range(Y_MAX):
			for x in range(X_MAX):
				leaf_shift[y-org_y][x-org_x]=leaf[y][x]

	return leaf_shift

def attach_stem(canvas):
	width=1
	#max width => 3
	for y in range(OY,Y_MAX):
		if y>=Y_MAX-(Y_MAX/3):
				width=1
		if  y>= Y_MAX-(Y_MAX/10):
				width=2
		for i in range(width):
				canvas[y][OX-width]="||"
				canvas[y][OX+width]="||"

def append_tree(tree,canvas):
	for y in range(Y_MAX):
		for x in range(X_MAX):
			if not (tree[y][x] in TOT_CHAR_SET):
				tree[y][x]=canvas[y][x]

def attach_banana(banana):
	banana_shift=[[" " for x in range(X_MAX)] for y in range(Y_MAX)]
	for y in range(10):
		for x in range(10):
			banana_shift[OY+y+1][OX+x+4]=banana[y][x]
	"""
	for y in range(Y_MAX):
		for x in range(X_MAX):
			print(banana_shift[y][x],end="")
		print("")				
	"""
	return banana_shift

def draw_tree():
	tree=[[" " for x in range(X_MAX)] for y in range(Y_MAX)]
	canvas=[[" " for x in range(X_MAX)] for y in range(Y_MAX)]
	#leaf set_1
	leaf=attach_leaf(rotate_leaf(draw_leaf(a=15),rot_fac=6),rot_fac=6)
	append_tree(tree,leaf)
	leaf=attach_leaf(mirror_leaf(rotate_leaf(draw_leaf(a=20,b=5),rot_fac=5)),rot_fac=4,mirror=True)
	append_tree(tree,leaf)
	#leaf_set 2
	leaf=attach_leaf(rotate_leaf(draw_leaf(a=5,b=20),rot_fac=8),rot_fac=2)
	append_tree(tree,leaf)
	leaf=attach_leaf(mirror_leaf(rotate_leaf(draw_leaf(a=20,b=5),rot_fac=5)),rot_fac=4,mirror=True)
	append_tree(tree,leaf)
	#leaf_set 3
	leaf=attach_leaf(rotate_leaf(draw_leaf(a=12,b=9),rot_fac=3),rot_fac=3)
	append_tree(tree,leaf)

	leaf=attach_leaf(mirror_leaf(rotate_leaf(draw_leaf(a=5,b=20,foc_x=30,foc_y=5),rot_fac=2)),rot_fac=0,mirror=True)
	append_tree(tree,leaf)
	
	#leaf_set 4
	leaf=attach_leaf(rotate_leaf(draw_leaf(a=2,b=22),rot_fac=20),rot_fac=3)
	append_tree(tree,leaf)

	leaf=attach_leaf(mirror_leaf(rotate_leaf(draw_leaf(a=5,b=18),rot_fac=2)),rot_fac=0,mirror=True)
	append_tree(tree,leaf)

	leaf=attach_leaf(mirror_leaf(rotate_leaf(draw_leaf(a=7,b=20),rot_fac=6)),rot_fac=0,mirror=True)
	append_tree(tree,leaf)

	#attach banana
	banana=attach_banana(get_banana())
	append_tree(tree,banana)

	#attach stem
	attach_stem(canvas)
	append_tree(tree,canvas)
	for y in range(6,Y_MAX):	
		for x in range(50,X_MAX):		
			print(vazha_color(tree[y][x]),end="")
		print("")
	

	print(" "*30,end="")
	print(CYAN+"="*40+END)
	print(" "*46,end="")
	print("AL_VAZHA")
	print(" "*30,end="")
	print(CYAN+"="*40+END)

draw_tree()	
