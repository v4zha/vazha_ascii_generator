import math
import random

#TOT_CHAR_SET={'-','|','\\','/','=',"^"}
X_MAX=200
Y_MAX=30

def get_x(x_list,y_coord):
	x_index=[]
	for i in range(X_MAX):
		if x_list[y_coord][i]=="-":
			x_index.append(i)
			
	return x_index

def leaf_clean(x_coord,x2,y_coord,screen):
		for x in range(x_coord,x2+1):
			if x !=x_coord and screen[y_coord][x]=="-":
				screen[y_coord][x]=" "

def del_rem(y_coord,screen):
	for x in range(X_MAX):
		for y in range(y_coord,Y_MAX):
			screen[y][x]=""


def draw_ascii_line(y1,y2,screen):
	x2=get_x(screen,y2)[-1]
	x1=get_x(screen,y1)[0]
	r_list=[]
	for i in range(6):
	 	r_list.append(random.randint(x1,x2+1))
	#slope
	m=(y2-y1)/(x2-x1)		
	for x in range(x1,x2+1):
		y=(x-x1)*m + y1	
		y_coord=int(y)
		if x in r_list:
			screen[y_coord][x]="^"
			#screen[y_coord][x+1]="\\"
			#x=x+1
				
		else:
			screen[y_coord][x]="-"
		leaf_clean(x,x2+1,y_coord,screen)
	
	del_rem(y1,screen)
	
def draw_ascii_ellipse(a,b,org_x,org_y,screen):
	x=[]
	y=[]		
	for theta in range(0,360):
		cos_t=math.cos(math.radians(theta))
		sin_t=math.sin(math.radians(theta))
		denom=math.sqrt((b*cos_t)*(b*cos_t) + (a*sin_t)*(a*sin_t))
		r=(a*b)/denom		    
		x.append(r*cos_t+org_x)
		y.append(r*sin_t+org_y)
	x_co=[]
	y_co=[]
	for x_coord in x:
		x_co.append(math.floor(x_coord))
	for y_coord in y:
	    y_co.append(math.floor(y_coord))
	
	for i in range(360):
		screen[y_co[i]][x_co[i]]="-"


def draw_leaf(a=26,b=5,foc_x=26,foc_y=6,y1=7,y2=5):
	screen=[[" " for x in range(X_MAX)] for y in range(Y_MAX)] 
	#a=26
	#b=5
	#focus shift
	#foc_x=26
	#foc_y=6    
	#y2=5
	#y1=7
	
	draw_ascii_ellipse(a,b,foc_x,foc_y,screen)
	draw_ascii_line(y1,y2,screen)	

#	for y in range(Y_MAX):
	#		print(screen[y][x],end="")
	#	print("")
	
	return screen


def get_max(screen):
	max_x=0
	max_y=0
	for y in range(Y_MAX):
		for x in range(X_MAX):
			if screen[y][x]=="-" or screen[y][x]=="^":
				if x>max_x:
					max_x=x
				if y>max_y:
					max_y=y	
	return max_x,max_y+2

def get_min(screen):
	min_x=0
	min_y=0
	for y in range(Y_MAX):
		for x in range(X_MAX):
			if screen[y][x]=="-" or screen[y][x]=="^":
				if x<min_x:
					min_x=x
				if y<min_y:
					min_y=y	
	return min_x,min_y

def get_banana():
	banana=[["" for x in range(10)]for y in range(10)]
	canvas=[[" " for x in range(10)]for y in range(10)]
	banana[0]=list(" |\\")
	banana[1]=list("  \\\\")
	banana[2]=list("  | |")
	banana[3]=list("-=====-")
	banana[4]=list("| | | |")
	banana[5]=list(" | | |")
	banana[6]=list("  | |")
	banana[7]=list("   |")
		 
	for y in range(10):
		for index,ele in enumerate(banana[y]):
			canvas[y][index]=ele
    
	return canvas
	