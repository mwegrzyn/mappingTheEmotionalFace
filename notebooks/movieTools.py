from matplotlib import animation
from moviepy.editor import VideoFileClip

from PIL import Image

import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('dark')
# modified from:
"""
Matplotlib Animation Example

author: Jake Vanderplas
email: vanderplas@astro.washington.edu
website: http://jakevdp.github.com
license: BSD
Please feel free to use and modify this, but keep the above information. Thanks!
"""

def saveVideo(pics,outName,myFps=1):
    # First set up the figure, the axis, and the plot element we want to animate
    fig = plt.figure();
    plt.xticks([]);plt.yticks([])
    myAnim = plt.imshow(Image.open(pics[0],'r')); # dummy

    # initialization function: plot the background of each frame
    def init():
        return myAnim,

    # animation function.  This is called sequentially
    def animate(i):
        #line.set_data(x, y)
        if i > 0:
            myAnim = plt.imshow(Image.open(pics[i-1],'r'));
        else:
            myAnim = plt.imshow(Image.open(pics[i],'r'));
        return myAnim,

    # call the animator.  blit=True means only re-draw the parts that have changed.
    anim = animation.FuncAnimation(fig, animate, init_func=init,
                                   frames=len(pics)+1);

    # save the animation as an mp4.  This requires ffmpeg or mencoder to be
    # installed.  The extra_args ensure that the x264 codec is used, so that
    # the video can be embedded in html5.  You may need to adjust this for
    # your system: for more information, see
    # http://matplotlib.sourceforge.net/api/animation_api.html
    anim.save(outName, fps=myFps, extra_args=['-vcodec', 'libx264'],dpi=300);