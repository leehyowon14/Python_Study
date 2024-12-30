class time_:
    def __init__(self, time_):
        self.minute = int(time_.split(":")[0])
        self.second = int(time_.split(":")[1])
    def add(self,adding_time):
        self.second += adding_time
        if self.second >=60:
            self.minute += 1
            self.second -= 60
    def minus(self, minus_time):
        self.second -= minus_time
        if self.minute <=0:
          if self.second <0:
            self.minute =0
            self.second =0
        if self.second < 0:
            self.minute -= 1
            self.second += 60

    
def solution(video_len, pos, op_start, op_end, commands):
    video_time = time_(video_len)
    pos_time = time_(pos)
    op_start_time = time_(op_start)
    op_end_time = time_(op_end)
    for command in commands:
        if (pos_time.minute*100+pos_time.second) >= (op_start_time.minute*100+op_start_time.second) and (pos_time.minute*100+pos_time.second)<=(op_end_time.minute*100+op_end_time.second):
            pos_time.minute = op_end_time.minute
            pos_time.second = op_end_time.second
            
        if command == "prev":
            pos_time.minus(10)
        elif command == "next":
            pos_time.add(10)
            
        if (pos_time.minute*100+pos_time.second) >= (op_start_time.minute*100+op_start_time.second) and (pos_time.minute*100+pos_time.second)<=(op_end_time.minute*100+op_end_time.second):
            pos_time.minute = op_end_time.minute
            pos_time.second = op_end_time.second
        if (pos_time.minute*100+pos_time.second) > (video_time.minute*100 + video_time.second):
            pos_time.minute = video_time.minute
            pos_time.second = video_time.second
    if pos_time.minute <10:
        pos_time.minute = f"0{pos_time.minute}"
    if pos_time.second <10:
        pos_time.second = f"0{pos_time.second}"
    answer = f'{pos_time.minute}:{pos_time.second}'
    return answer