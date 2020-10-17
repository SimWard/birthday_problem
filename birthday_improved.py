import numpy as np
import matplotlib.pyplot as plt
import bisect

MAX_BIRTHDAY_TESTS = 40


def test_birthday_percentage(number, samples=10000):
    counter = 0
    for i in range(samples):
        bdays = np.random.randint(1, 365, number)
        if len(np.unique(bdays)) != len(bdays):
            counter += 1
    return counter / samples


def create_success_dict(tests, samples=10000):
    success_dict = {}
    for i in range(tests):
        pc = test_birthday_percentage(i, samples)
        success_dict[i] = pc
    return success_dict


def show_probability_chart(success_dict):
    half_pos = bisect.bisect_right(list(s.values()), 0.5)
    barlist = plt.bar(list(s.keys()), list(s.values()))
    barlist[half_pos - 1].set_color('r')
    plt.text(half_pos - 1, s[half_pos], s[half_pos], ha="right")
    plt.title("Birthday problem - Pr(shared birthdays) by number of people")
    plt.xlabel("Number of people together")
    plt.ylabel("Probability of birthday matching")
    plt.show()


s = create_success_dict(MAX_BIRTHDAY_TESTS)
show_probability_chart(s)
