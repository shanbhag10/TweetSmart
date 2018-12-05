#!/bin/sh
for i in {1..13}
do
  echo $i
  python3 twitter_likes.py $i
  sleep 900
done
