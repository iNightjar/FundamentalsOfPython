class Time:
    def __init__(self, hour=None, minute=None, second=None) -> None:
        self.hour = hour
        self.minute = minute
        self.second = second

    def __str__(self) -> str:
        return "({:02d}:{:02d}:{:02d})".format(self.hour, self.minute, self.second)

def time_to_int(time):
        minutes = time.hour*60 + time.minute
        seconds = minutes*60+time.second
        return seconds

def int_to_time(seconds):
    time = Time()
    minutes, time.second = divmod(seconds,60)
    time.hour, time.minute = divmod(minutes, 60)
    return time
    
def add_time(t1,t2):
    seconds = time_to_int(t1)+ time_to_int(t2)
    return int_to_time(seconds)

start = Time(9,45,00)
running = Time(1,35,00)
done = add_time(start, running)
print(done)
