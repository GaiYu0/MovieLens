import sys
import numpy as np
from pyspark.sql.session import SparkSession
import utils

csv = sys.argv[1]

ss = SparkSession.builder.getOrCreate()
df = ss.read.csv(csv, 'uid INT, iid INT, r FLOAT, t INT')

data_frame_to_array = lambda df: np.array(df.rdd.flatMap(lambda x: x).collect())

####################################################################################################

n_partitions = int(sys.argv[2])

sorted_df = df.sort('uid')
uid = data_frame_to_array(sorted_df.select('uid'))
iid = data_frame_to_array(sorted_df.select('iid'))
r = data_frame_to_array(sorted_df.select('r'))

c = data_frame_to_array(df.groupBy('uid').count().sort('uid').select('count'))
segment = np.cumsum(c) - c
quotient, reminder = np.divmod(c, n_partitions)
offsets = [np.zeros_like(c)]
for i in range(n_partitions):
    offsets.append(offsets[-1] + quotient + (i < reminder))
indices = [utils.arange(segment + p, segment + q) for p, q in zip(offsets[:-1], offsets[1:])]

uids = list(map(uid.__getitem__, indices))
iids = list(map(iid.__getitem__, indices))
rs = list(map(r.__getitem__, indices))

####################################################################################################

np.save('uids', uids)
np.save('iids', iids)
np.save('rs', rs)
