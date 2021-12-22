def calc_latency_from_log(log_file):
    log = open("./logs/latency.log").readlines()
    consumed_time = []
    for line in log:
        try:
            consumed_time.append(float(line.split()[-2]))
        except:
            pass
    return sum(consumed_time)/len(consumed_time)