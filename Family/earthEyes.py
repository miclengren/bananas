'''earthEyes demonstrates PIL.Image.paste()
Unpublished work (c)2013 Project Lead The Way
CSE Activity 1.3.7 PIL API
Version 9/10/2013 '''

import PIL
import matplotlib.pyplot as plt
import os.path              

# Open the files in the same directory as the Python script
directory = os.path.dirname(os.path.abspath(__file__))  
backdrop = os.path.join(directory, 'backdrop.png')
print backdrop
# Open and show the student image in a new Figure window
backdrop_img = PIL.Image.open(backdrop)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(backdrop_img, interpolation='none')

# Display student in second axes and set window to the right eye
axes[1].imshow(backdrop_img, interpolation='none')
axes[1].set_xticks(range(1050, 1410, 100))
axes[1].set_xlim(1000, 1000) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(1000,1000)
fig.show()

# Open, resize, and display earth
family_member = os.path.join(directory, 'chyna.png')
family_member_img = PIL.Image.open(family_member)
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(family_member_img)

fig2.show()

# Paste earth into right eye and display
# Uses alpha from mask
backdrop_img.paste(family_member_img, (1000, 1000), mask=family_member_img) 
# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(backdrop_img, interpolation='none')
axes3[1].imshow(backdrop_img, interpolation='none')
axes3[1].set_xlim(1000, 1000)
axes3[1].set_ylim(1000, 1000)
fig3.show()