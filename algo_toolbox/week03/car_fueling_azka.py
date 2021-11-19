# Problem Description
# Input Format. The first line contains an integer 𝑑. The second line contains an integer 𝑚. The third line
# specifies an integer 𝑛. Finally, the last line contains integers stop1, stop2, . . . , stop𝑛.
# Input Format. Assuming that the distance between the cities is 𝑑 miles, a car can travel at most 𝑚 miles
# on a full tank, and there are gas stations at distances stop1, stop2, . . . , stop𝑛 along the way, output the
# minimum number of refills needed. Assume that the car starts with a full tank. If it is not possible to
# reach the destination, output −1.
# Constraints. 1 ≤ 𝑑 ≤ 10^5. 1 ≤ 𝑚 ≤ 400. 1 ≤ 𝑛 ≤ 300. 0 < stop1 < stop2 < · · · < stop𝑛 < 𝑚.

text = '''950
400
4
200 375 550 750'''
# text = '''10
# 3
# 4
# 1 2 5 9'''
# text = '''200
# 250
# 2
# 100 150'''

(d,m,n) = (int(i) for i in text.strip().split('\n')[:-1])

stations = [int(i) for i in text.strip().split('\n')[-1].split()]

station_count = 0
last_station = 0

if d < m:
    station_count = 0
else:
    for i,station in enumerate(stations):
        if station-last_station > d:
            station_count = -1
            break
        elif i<len(stations)-1:
            if stations[i+1] < last_station + m:
                continue
            else:
                station_count += 1
                d -= station
                last_station = station
        else:
            station_count += 1
            d -= station
            last_station = station

print(station_count)