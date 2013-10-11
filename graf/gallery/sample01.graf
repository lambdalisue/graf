#!/usr/bin/env graf
# vim: set fileencoding=utf-8 :
#
# Author:   Alisue (lambdalisue@hashnote.net)
# URL:      http://hashnote.net/
# Date:     2013-10-04
#
# (C) 2013 hashnote.net, Alisue
#
import os
import numpy as np
root = os.path.dirname(__file__)

# set default parser class
set_default_parser(parsers.JASCOParser)

# load dataset
dataset = []
nameset = []
for i in xrange(0, 60, 10):
    dataset += load(os.path.join(root, 'raw/%d.*.txt' % i),
            using=(0, 1), unite=True, basecolumn=0)
    nameset += [str(i)]

# relative
filters.relative(dataset, ori=0, column=1)

# plot
subplot(211)
for n, (x, y) in zip(nameset, dataset):
    # calculate average
    ax = filters.statistics.avg(x)
    ay = filters.statistics.avg(y)
    # calculate confidential interval
    e = filters.statistics.interval(y)
    # plot
    color = styles.color_cycle.next()
    #errorbar(ax, ay, yerr=e, color=color, alpha=0.6)
    plot(ax, ay, label=n, color=color)
legend()
grid()

subplot(212)
# find peaks
px = []
py = []
for (x, y) in dataset:
    # calculate average
    ax = filters.statistics.avg(x)
    ay = filters.statistics.avg(y)
    # find peak
    index = np.where(ay==np.max(ay))
    px.append(ax[index])
    py.append(ay[index])
plot(nameset, py)
twinx()
plot(nameset, px)

show()
