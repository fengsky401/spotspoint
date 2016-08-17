import pprint
import cv2
import numpy as np
from PIL import Image,ImageDraw
from pylab import *
import os
from readimage import *
from usrdefine import *

#filename='image_0000.png'
#label=[160 120 160 92 188.5 76.9]
def spotpoint(srcdir,tardir,filename,label,rradius,fillcolor,outlinecolor):
   completesrcname=os.path.join(srcdir,filename)
   completetarname=os.path.join(tardir,filename)
   print(completesrcname);
   print(completetarname)
   img=cv2.imread(completesrcname);
   cv2.imwrite(completetarname,img);
   img2=Image.open(completetarname);
   draw=ImageDraw.Draw(img2);
   print len(label);
   for i in range(0,len(label)/2):
       draw.ellipse(((label[2*i]-rradius,label[2*i+1]-rradius),(label[2*i]+rradius,label[2*i+1]+rradius)),fill=fillcolor,outline=outlinecolor);
       print '%d %d\n' %(label[2*i],label[2*i+1]);
   img2.save(completetarname);
  

############################DEFINED PATH###############################################
srcimgdir='/home/nero/project/ImageFlow-master/TF-framework/Data/Depth'
tarimgdir='./target'
TargetLabel_path='/home/nero/project/ImageFlow-master/TF-framework/targetlabel'
PredictLabel_path='/home/nero/project/ImageFlow-master/TF-framework/sourcelabel';
TarLable_File_Name=['have2001.csv']
PreLable_File_Name=['have2001.csv']
#################SIGN TARGET POINT##################################
for j in range(0,len(TarLable_File_Name)):

  labels, filenames = read_labels_with_string(TargetLabel_path, TarLable_File_Name[j])
  for i in range(0,len(filenames)):
     spotpoint(srcimgdir,tarimgdir,filenames[i],labels[i],4,'blue','red')
'''print (len(labels))
#print (filenames)
for i in range(0,len(filenames)):
   print '%d  ' %(i);
   print(labels[i]);
   print '\n';
 '''  
##################SIGN PREDICT POINT###################################################
for j in range(0,len(PreLable_File_Name)):

  labels, filenames = read_labels_with_string(TargetLabel_path, PreLable_File_Name[j])
  for i in range(0,len(filenames)):
     spotpoint(tarimgdir,tarimgdir,filenames[i],labels[i],3,'red','yellow')
