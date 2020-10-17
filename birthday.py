import pandas as pd
import matplotlib.pyplot as plt
import datetime.datetime as dt

start = dt.now()

df = pd.DataFrame(pd.date_range('2020-01-01', periods=366, freq='1D'))

amplifier = 1000

df = pd.concat([df] * amplifier)
df = df.reset_index(drop=True)
df = df.rename(columns={df.columns[0]: "birthdays"})


def test_birthday_percentage(number, samples=1000):
    counter = 0
    for i in range(samples):
        temp = df.sample(number)
        if not temp['birthdays'].is_unique:
            counter += 1
    return counter / samples


def create_success_table(tests, samples=1000):
    success_dict = {}
    for i in range(tests):
        pc = test_birthday_percentage(i, samples)
        success_dict[i + 1] = pc
    return success_dict


s = create_success_table(5)
plt.bar(list(s.keys()), list(s.values()))
plt.show()
