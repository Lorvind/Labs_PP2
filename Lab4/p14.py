import datetime
import math

datetime1, time_zone_offset1 = input().split()
datetime2, time_zone_offset2 = input().split()

datetime1 = datetime.datetime.strptime(datetime1, "%Y-%m-%d" )
datetime2 = datetime.datetime.strptime(datetime2, "%Y-%m-%d" )

if time_zone_offset1[3] == '-':
    time_zone_offset1 = datetime.timedelta(hours=int(time_zone_offset1[4:6]), minutes=int(time_zone_offset1[7:9]))
    time_zone_offset1 = -time_zone_offset1
else:
    time_zone_offset1 = datetime.timedelta(hours=int(time_zone_offset1[4:6]), minutes=int(time_zone_offset1[7:9]))

if time_zone_offset2[3] == '-':
    time_zone_offset2 = datetime.timedelta(hours=int(time_zone_offset2[4:6]), minutes=int(time_zone_offset2[7:9]))
    time_zone_offset2 = -time_zone_offset2
else:
    time_zone_offset2 = datetime.timedelta(hours=int(time_zone_offset2[4:6]), minutes=int(time_zone_offset2[7:9]))

datetime1 -= time_zone_offset1
datetime2 -= time_zone_offset2


delta_days = abs(datetime1 - datetime2).days

print(delta_days)