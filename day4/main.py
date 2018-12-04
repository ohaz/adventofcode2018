from datetime import datetime


def guards(times):
    d = {}
    current_gid = 0
    for current_time in times:
        if current_time[1] is not None:
            current_gid = current_time[1]
        if current_gid not in d.keys():
            d[current_gid] = []

        if 'falls asleep' in current_time[2]:
            d[current_gid].append({'start': current_time[0], 'end': None, 'duration': 0})
        elif 'wakes up' in current_time[2]:
            d[current_gid][-1]['end'] = current_time[0]
            d[current_gid][-1]['duration'] = (current_time[0] - d[current_gid][-1]['start']).total_seconds()

    second_d = []
    for key in d.keys():
        second_d.append((key, sum([x['duration'] for x in d[key]])))
    second_d.sort(key=lambda x: x[1], reverse=True)

    return d, second_d


def part2(d, second_d):
    guards = []
    for guard in d.keys():
        minutes = {}
        for entry in d[guard]:
            for minute in range(entry['start'].minute, entry['end'].minute):
                if minute in minutes.keys():
                    minutes[minute] += 1
                else:
                    minutes[minute] = 1
        highest_minute = [-1, -1]
        for minute in minutes.keys():
            if minutes[minute] > highest_minute[1]:
                highest_minute[0] = minute
                highest_minute[1] = minutes[minute]
        guards.append((guard, highest_minute[0]))
    guards.sort(key=lambda x: x[1], reverse=True)
    return guards[0]


def part1(d, second_d):
    longest_guard = d[second_d[0][0]]


    minutes = {}
    for entry in longest_guard:
        for minute in range(entry['start'].minute, entry['end'].minute):
            if minute in minutes.keys():
                minutes[minute] += 1
            else:
                minutes[minute] = 1
    highest_minute = [-1, -1]
    for minute in minutes.keys():
        if minutes[minute] > highest_minute[1]:
            highest_minute[0] = minute
            highest_minute[1] = minutes[minute]
    return second_d[0][0], highest_minute


def sort_times(lines):
    stuff = []
    for line in lines:
        line = line.replace('\n', '')
        time = line[line.find('[')+1:line.find(']')]
        time = datetime.strptime(time, '%Y-%m-%d %H:%M')
        do = line[line.find('] ')+2:]
        gid = None
        if '#' in line:
            gid = line[line.find('#')+1:]
            gid = gid.split(' ')[0]
            gid = int(gid)
        stuff.append((time, gid, do))
    stuff.sort(key=lambda x: x[0])
    return stuff


with open('input.txt', 'r') as input_file:
    input_lines = input_file.readlines()


sorted_times = sort_times(input_lines)
dg, second_dg = guards(sorted_times)
gid, minute = part1(dg, second_dg)
print(gid*minute[0])
gid, minute = part2(dg, second_dg)
print(gid*minute)
