import sys
import numpy as np

prefix = sys[1]

uids = np.load('uids.npy')
iids = np.load('iids.npy')
rs = np.load('rs.npy')

for i in range(1, len(rs) + 1):
    np.save('%s%d/uid' % (prefix, i), uid)
    np.save('%s%d/iid' % (prefix, i), iid)
    np.save('%s%d/r' % (prefix, i), r)
