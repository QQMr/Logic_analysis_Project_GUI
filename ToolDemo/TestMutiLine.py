from pylab import figure, show, setp
#from matplotlib.numerix import sin, cos, exp, pi, arange
import numpy as np

t = np.arange(0.0, 2.0, 0.01)
s1 = np.sin(2*np.pi*t)
s2 = np.exp(-t)
s3 = np.sin(2*np.pi*t)*np.exp(-t)
s4 = np.sin(2*np.pi*t)*np.cos(4*np.pi*t)

fig = figure()
t = np.arange(0.0, 2.0, 0.01)

yprops = dict(rotation=0,
              horizontalalignment='right',
              verticalalignment='center',
              x=-0.01)

axprops = dict(yticks=[-1, 0, 1])

ax1 =fig.add_axes([0.1, 0.7, 0.8, 0.2], **axprops)
ax1.plot(t, s1)
ax1.set_ylabel('S1', **yprops)

axprops['sharex'] = ax1
axprops['sharey'] = ax1
# force x axes to remain in register, even with toolbar navigation
ax2 = fig.add_axes([0.1, 0.5, 0.8, 0.2], **axprops)

ax2.plot(t, s2)
ax2.set_ylabel('S2', **yprops)

ax3 = fig.add_axes([0.1, 0.3, 0.8, 0.2], **axprops)
ax3.plot(t, s4)
ax3.set_ylabel('S3', **yprops)

ax4 = fig.add_axes([0.1, 0.1, 0.8, 0.2], **axprops)
ax4.plot(t, s4)
ax4.set_ylabel('S4', **yprops)

# turn off x ticklabels for all but the lower axes
for ax in ax1, ax2, ax3:
    setp(ax.get_xticklabels(), visible=False)

show()