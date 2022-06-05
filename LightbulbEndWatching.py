from datetime import datetime
from typing import List, Optional

def sum_light(els: List[datetime], start_watching: Optional[datetime] = None, end_watching: Optional[datetime] = None):
    time = 0
    def returnTime(time):
        return time.day * 24 * 60 * 60 + time.hour * 60 * 60 + time.minute * 60 + time.second
    try: time0 = returnTime(start_watching)
    except: time0 = 0
    try: time3 = returnTime(end_watching)
    except: time3 = pow(2, 50)
    for x in range(0, len(els), 2):
        time1 = returnTime(els[x])
        try: time2 = returnTime(els[x+1])
        except: time2 = time3
        if time0 > time2:
            continue
        elif time3 < time1:
            break
        else:
            end = time1 if time1 > time0 else time0 if time2 > time0 else None
            start = time2 if time2 < time3 else time3 if time1 < time3 else None
            if start == None or end == None:
                continue
            else:
                time += start - end
    return time
