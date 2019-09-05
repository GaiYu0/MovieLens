wget http://files.grouplens.org/datasets/movielens/ml-100k.zip &
wget http://files.grouplens.org/datasets/movielens/ml-1m.zip &
wget http://files.grouplens.org/datasets/movielens/ml-10m.zip &
wait

for f in *.zip; do
    unzip $f &
done
wait
