maxproc = 3
# readpath = ''
# writepath = ''
# simname = ''
outprefix = 'star.out.'
nframes = 1
frameskip = 1
startingset = 1
period = 200
do_marks = 0
do_snapshot = 0
dataset = 1
partskip = 1
# ENERCOMP
do_enercomp = 0
bern_low  = 1.0e19
bern_high = 1.0e24
bernlim = 0.5e22
# BERNOULLI
do_bernoulli = 0
bern_fixlimits = 0
# bern_highlim = 1.0e23
# bern_plotwidth = 4.0e13
# ENERGIES
do_energies = 0
# ORBEL
do_orbel = 0
# CORETEMP
do_coretemp = 0
# RADPROF
plot_mesa = 0
# mesadata = 'profile17.data'
corecorrect = 0
do_radprof = 0
radprof_fixaxes = 0
# radprof_axes = [6.0e8, 3.0e11, 3.0e-2, 30.0]
plot_cutoff = 0
# cutoffRho = 0.0009398664788462718
# TEMPPROF
do_tempprof = 0
tempprof_fixaxes = 0
# tempprof_axes = [1.0e9, 1.0e12, 1.0e4, 4.0e7]
# ENTROPY
do_entropy = 0
entprof_fixaxes = 0
# entprof_axes = [1.0e10, 1.0e15, 1.0e-16, 1.0e-9]
# DENSANIM
do_densanim = 0
densanim_direction = 'x'
# densanim_plotwidth = 3.0e11
densanim_fixlimits = 0
# densanim_lowlim = 6.0e10
# densanim_highlim = 6.0e11
# PARTSLICEANIM
do_partslice = 0
partslice_direction = 'x'
partslice_parttype = 'H'
# partslice_plotwidth = 3.0e11
partslice_fixlimits = 0
# partslice_lowlim = 1.0e19
# partslice_highlim = 1.0e24
# VELPART
do_velpart = 0
velpart_fixlimits = 0
# velpart_lowlim = 1.0e9
# velpart_highlim = 1.0e13
# velpart_plotwidth = 4.0e13
# COMPARISON
do_comparison = 0
# comparison_name = ''
nplots = 1
nrows = 1
ncolumns = 1
readpath1 = '/Users/ljprust/data/'
readpath2 = '/Users/ljprust/data/'
readpath3 = '/Users/ljprust/data/'
readpath4 = '/Users/ljprust/data/'
readpath5 = '/Users/ljprust/data/'
readpath6 = '/Users/ljprust/data/'
readpath7 = '/Users/ljprust/data/'
readpath8 = '/Users/ljprust/data/'
title1 = ''
title2 = ''
title3 = ''
title4 = ''
title5 = ''
title6 = ''
title7 = ''
title8 = ''

import math

gamma = 5.0/3.0
G = 6.674e-8
R = 8.314e7 / G
Rsun = 7.0e10
Msun = 2.0e33
k = 1.381e-16 / G
h = 6.626e-27 / math.sqrt(G)
mpart = 1.6606e-24
