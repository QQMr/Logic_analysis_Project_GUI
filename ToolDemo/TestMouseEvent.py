import matplotlib.pyplot as plt
import numpy as np

figmain, axmain = plt.subplots()
figzoom, axzoom = plt.subplots()

axmain.set(xlim=(-5, 5), ylim=(-75, 175), autoscale_on=False,
          title='Click to zoom')
axzoom.set(xlim=(-2, 2), ylim=(-75, 175), autoscale_on=False,
           title='Zoom window')

x = np.arange(-5, 5, 0.1)
y = x ** 3

axmain.plot(x, y, 'g-d')
axzoom.plot(x, y, 'b-.o')


def onbuttonpress(event):
    print(str(event.button))
    if event.button == 1:        # left = 1, scroll=2, right=3
        xUp, xdown = axzoom.get_xlim()
        x, y = event.xdata, event.ydata

        if (x-xUp) > (xdown -x):
            xUp = x - (xdown -x)
        else:
            xdown = x + (x - xUp)

        axzoom.set_xlim(xUp, xdown)
        #axzoom.set_ylim(y - 10, y + 10)
        figzoom.canvas.draw()
    if (event.button == 'up' or event.button == 'down'):
        xUp = 0;
        xdown = 0;
        x_scalar = 0
        x, y = event.xdata, event.ydata
        x_scalar = x_scalar + int(event.step)/10
        #x_scalar = x_scalar if(x_scalar > 0) else 0
        print( "Step"+ str(event.step) )
        xUp, xdown  = axzoom.get_xlim();
        axzoom.set_xlim(xUp - x_scalar, xdown + x_scalar)
        #axzoom.set_ylim(y - 10, y + 10)
        figzoom.canvas.draw()


figmain.canvas.mpl_connect('button_press_event', onbuttonpress)
figmain.canvas.mpl_connect('scroll_event', onbuttonpress)

plt.show();