import sys
from tqdm import tqdm

src = open(sys.argv[1], 'r')
dst = open(sys.argv[2], 'w')
for line in tqdm(src):
    dst.write(line.replace(sys.argv[3], sys.argv[4]))
