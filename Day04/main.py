import re

from collections import Counter

with open("input_test.txt") as n:
    test_input = [line.strip() for line in n]

with open("input.txt") as n:
    input = [line.strip() for line in n]


regex = r"\[([0-9]{4})-([0-9]{2})-([0-9]{2}) ([0-9]{2}):([0-9]{2})\] (.*)"
regex_id = r"Guard #([0-9]+) begins shift"


def sort_entries(list):
    return sorted(list)


def sleepy_periods(list):
    sp = []
    guard_id = sleep = wake = None
    sorted_list = sort_entries(list)
    for entry in sorted_list:
        year, month, day, hour, minute, action = re.match(regex, entry).groups()
        guard = re.match(regex_id, action)
        if guard:
            assert sleep is None and wake is None
            guard_id = guard.groups()[0]
        elif "falls asleep" in action:
            assert guard_id is not None and sleep is None and wake is None
            sleep = int(minute)
        elif "wakes up" in action:
            assert guard_id is not None and sleep is not None and wake is None
            wake = int(minute)
            sp.append((guard_id, sleep, wake))
            sleep = wake = None
    return sp


# Solution for first puzzle


def laziest_guard(list):
    sleep_list = sleepy_periods(list)
    sleep_counter = Counter()
    for sleep in sleep_list:
        sleep_counter[sleep[0]] += sleep[2] - sleep[1]
    return sleep_counter.most_common(1)[0][0]


def guard_most_common_time_asleep(list, guard_id: int = 0):
    minute_list = sleepy_periods(list)
    minutes = Counter()
    for minute in minute_list:
        if minute[0] == guard_id:
            for mins in range(minute[1], minute[2]):
                minutes[mins] += 1
    [(minute1, count1), (minute2, count2)] = minutes.most_common(2)
    assert count1 > count2
    return minute1


def get_id_times_common_minute(list):
    grd_id = laziest_guard(list)
    common_min = guard_most_common_time_asleep(list, grd_id)
    return int(grd_id) * int(common_min)


assert get_id_times_common_minute(test_input) == 240

print(f"Strategy 1: {get_id_times_common_minute(input)}")

# Solution for second puzzle


def most_common_minute_asleep_guard(list):
    time_list = sleepy_periods(list)
    counts = Counter()
    for time in time_list:
        for minute in range(time[1], time[2]):
            counts[(time[0], minute)] += 1
    [((gid1, min1), count1), ((gid2, min2), count2)] = counts.most_common(2)
    assert count1 > count2
    return int(gid1) * int(min1)


assert most_common_minute_asleep_guard(test_input) == 4455

print(f"Strategy 2: {most_common_minute_asleep_guard(input)}")
