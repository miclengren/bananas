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
# Open and show image in a new Figure window
backdrop_img = PIL.Image.open(backdrop)
fig, axes = plt.subplots(1, 2)
axes[0].imshow(backdrop_img, interpolation='none')

# Display in second axes and set window 
axes[1].imshow(backdrop_img, interpolation='none')
axes[1].set_xticks(range(1150, 500, 10))
axes[1].set_xlim(1150, 500) #coordinates measured in plt, and tried in iPython
axes[1].set_ylim(1150,500)
fig.show()

# Open, resize, and display
family_member = os.path.join(directory, 'chyna.png')
family_member_img = PIL.Image.open(family_member)
fig2, axes2 = plt.subplots(1, 2)
axes2[0].imshow(family_member_img)

fig2.show()

# Paste into and display
# Uses alpha from mask
backdrop_img.paste(family_member_img, (1150, 500), mask=family_member_img)
# Display
fig3, axes3 = plt.subplots(1, 2)
axes3[0].imshow(backdrop_img, interpolation='none')
axes3[1].imshow(backdrop_img, interpolation='none')
axes3[1].set_xlim(1150, 500)
axes3[1].set_ylim(1150, 500)
fig3.show()