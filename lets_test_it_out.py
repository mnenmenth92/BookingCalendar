
from datetime import datetime, timedelta
from config import time_format

#
# now = datetime.now()
# string_date = now.strftime("%Y%m%d_%H%M%S")
# print(len(string_date))
# print(string_date)
#






class time_slot():
    def __init__(self, start, duration):
        self.time_started = start
        self.duration = duration


    def conflict(self, start, duration):
        time_started = self.string_to_time(start)
        time_ended = time_started + timedelta(minutes=duration)
        return self.check_if_time_between(time_started) or self.check_if_time_between(time_ended)


    def string_to_time(self, string_time):
        return datetime.strptime(string_time, time_format)

    def get_start_time(self):
        return self.string_to_time(self.time_started)

    def get_end_time(self):
        time = self.string_to_time(self.time_started) + timedelta(minutes=self.duration)
        return time

    def check_if_time_between(self, _time):
        return _time > self.get_start_time() and _time < self.get_end_time()



time1_str = "20200501_123030"
compared_string = "20200501_122031"
compared_time = datetime.strptime(compared_string, time_format)

time1 = time_slot(time1_str, 60)

print(time1.conflict(compared_string,20))


