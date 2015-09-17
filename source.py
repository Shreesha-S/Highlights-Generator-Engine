"""
Hack developed at Ayana Hackathon 2015, PES University(Formerly PESIT), Bangalore.
"""
import os

with open ("comment1.txt") as f:
    commentary = f.readlines() 

time_list = []

for line in commentary:
    if ("CHANCE!" in line) or ("GOAL!" in line) or ("CHANCES!" in line) or ("CROSSBAR!" in line):
        time = line[0: 3]
        time = time.split()
        time = time[0].strip()
        time_list.append(time)
    else:
        continue

time_list = list(set(time_list))
time_list = map(int, time_list)
time_list.sort()
count = 1

for splice in time_list:
    counter = 0
    if int(splice) + 3 > 45:
        splice = str(int(splice) + 2)
        counter = 1 
    hr = 0
    minute = 0
    if int(splice) + 3 > 59:
        hr += 1
        minute = (int(splice)+3) % 60 
    else:
        hr = 0
        minute = int(splice) + 3
    if (counter == 1):
        os.system("avconv -i football1.mp4 -vcodec copy -acodec copy -ss " + str(hr) +":" + str(minute) + ":40 -t 00:01:00 football-output"+str(count)+".mp4")
    else:
        os.system("avconv -i football1.mp4 -vcodec copy -acodec copy -ss " + str(hr) +":" + str(minute) + ":32 -t 00:01:00 football-output"+str(count)+".mp4")
    count += 1

concat = "mencoder -ovc copy -oac mp3lame "
count = 1
for splice in time_list:
    video = "football-output" + str(count) + ".mp4 "
    concat += video
    count += 1
concat += "-o output.mp4"

os.system(concat)
os.system("vlc output.mp4")
