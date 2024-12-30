def solution(diffs, times, limit):
    max_level = max(diffs)
    min_level = min(diffs)
    core_level = (max_level+min_level)//2
    while True: 
        prev_level = core_level
        total_time = 0
        prev_times = times[0]
        for diff,time in zip(diffs,times):
            if diff <= core_level:
                total_time += time
            elif diff > core_level:
                total_time += (prev_times+time) * (diff-core_level) + time
            prev_times = time
        if total_time > limit:
            min_level = core_level
        elif total_time == limit:
            answer = core_level
            break
        elif total_time < limit:
            max_level = core_level

        core_level = (max_level+min_level)//2

        if (prev_level == core_level) and prev_level == 1:
          answer = 1
          break
        elif (prev_level == core_level):
          
          answer = core_level +1
          break


    return answer
