cat pipe | ./fancy_cache | nc -l 1337 > pipe  &
python client.py 
