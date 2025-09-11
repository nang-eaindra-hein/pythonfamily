#laps
fast_min=0.0
fast_sec=0.0
slow_min=0.0
slow_sec=0.0
ave_min=0.0
ave_sec=0.0
total=0.0
fastest=10000.0
slowest=0.0
average_time=0.0

laps=int(input("enter the no. of laps"))
for i in range(laps):
         print("lap",i+1)
         tmin=int(input("enter minutes: "))
         tsec=int(input("enter seconds: "))
         total+=tmin*60+tsec
         t=tmin*60+tsec
if t<fastest:
         fastest=t
         fast_min=tmin
         fast_sec=tsec
if t<slowest:
         slowest=t
         slow_min=tmin
         slow_sec=tsec
average_time=total/laps
ave_min=average_time//60
ave_sec=average_time%60
print("fastest lap:{} min{}sec".format(fast_min,fast_sec))
print("slowest lap:{} min {}sec".format(slow_min,slow_sec))
print("average lap:{}min {}sec".format(ave_min,ave_sec))
