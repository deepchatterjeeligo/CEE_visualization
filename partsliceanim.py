from __main__ import *

import yt
import matplotlib.pyplot as pl
import matplotlib.animation as animation

if partslice_fixlimits:
	sizingappend = ''
else:
	sizingappend = '_sizing'

# create figure
ts = yt.load( readpath + 'star.out.00000' + str(startingset) )
plot = yt.SlicePlot(ts, partslice_direction, ('gas', partslice_parttype + '_nuclei_density'), width = partslice_plotwidth )
plot.annotate_timestamp(time_unit = 'hr')
# plot.set_buff_size([2000,2000])

if partslice_fixlimits:
	plot.set_zlim('all',partslice_lowlim,partslice_highlim)
	
# plot.set_axes_unit('unitary')
fig = plot.plots[partslice_parttype + '_nuclei_density'].figure

# create frames
def animate(i):
	num = i*frameskip + 1000000 + startingset
	numstr = str(num)
	cut = numstr[1:7]
	print 'partslice: ' + simname + ' Frame ' + str(i) + ' Data Set ' + cut
	
	ds = yt.load(readpath + 'star.out.' + cut)
	
	plot._switch_ds(ds)
	
# create animation object
anim = animation.FuncAnimation(fig, animate, frames = nframes, interval = period, repeat = False)
partslice_saveas = writepath + partslice_direction + '_' + partslice_parttype + '_slice_' + simname + sizingappend + '.mp4'
anim.save(partslice_saveas)
print 'partslice: Saved animation ' + partslice_saveas