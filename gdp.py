import random

import pandas as pd
import matplotlib.pyplot as plt
import math
import numpy as np

df = pd.read_csv('gapminder.csv')
country = df.iloc[:, 0]
continent = df.iloc[:, 1]
year = df.iloc[:, 2]
df.iloc[:, 2] = year.apply(lambda x: x + (0.5 - random.random()) * 3.5)
lifeExp = df.iloc[:, 3]
pop = df.iloc[:, 4]
gdpPercap = df.iloc[:, 5]
old_year = year

df.to_csv('newgapminder.csv', index=False, encoding='utf-8')


def year_life_color():
    year = np.array([i + (0.5 - random.random()) * 3.5 for i in old_year])
    Asia = np.array(continent == 'Asia')
    Europe = np.array(continent == 'Europe')
    Africa = np.array(continent == 'Africa')
    Americas = np.array(continent == 'Americas')
    Oceania = np.array(continent == 'Oceania')
    plt.scatter([i for i in year * Asia if i], [i for i in lifeExp * Asia if i], c='red', marker='o', s=15, label='Asia')
    plt.scatter([i for i in year * Europe if i], [i for i in lifeExp * Europe if i], c='black', marker='o', s=15, label='Europe')
    plt.scatter([i for i in year * Africa if i], [i for i in lifeExp * Africa if i], c='green', marker='o', s=15, label='Africa')
    plt.scatter([i for i in year * Americas if i], [i for i in lifeExp * Americas if i], c='blue', marker='o', s=15, label='Americas')
    plt.scatter([i for i in year * Oceania if i], [i for i in lifeExp * Oceania if i], c='magenta', marker='o', s=15, label='Oceania')

    plt.grid(color='b', ls='-.', lw=0.1)
    plt.title("Differentiate continents by color")  # title
    plt.xlabel("year")  # x-axis
    plt.ylabel("life-expectancy")  # y-axis
    plt.legend(loc=2)
    plt.show()


def year_life_shape():
    year = np.array([i + (0.5 - random.random()) * 3.5 for i in old_year])
    Asia = np.array(continent == 'Asia')
    Europe = np.array(continent == 'Europe')
    Africa = np.array(continent == 'Africa')
    Americas = np.array(continent == 'Americas')
    Oceania = np.array(continent == 'Oceania')
    plt.scatter([i for i in year * Asia if i], [i for i in lifeExp * Asia if i], c='red', marker='o', s=30, label='Asia')
    plt.scatter([i for i in year * Europe if i], [i for i in lifeExp * Europe if i], c='black', marker='1', s=30, label='Europe')
    plt.scatter([i for i in year * Africa if i], [i for i in lifeExp * Africa if i], c='green', marker='+', s=30, label='Africa')
    plt.scatter([i for i in year * Americas if i], [i for i in lifeExp * Americas if i], c='blue', marker='d', s=30, label='Americas')
    plt.scatter([i for i in year * Oceania if i], [i for i in lifeExp * Oceania if i], c='magenta', marker='*', s=30, label='Oceania')

    plt.grid(color='b', ls='-.', lw=0.1)
    plt.title("Differentiate continents by shape")  # title
    plt.xlabel("year")  # x-axis
    plt.ylabel("life-expectancy")  # y-axis
    plt.legend(loc=2)
    plt.show()


def year_life_fillstyle():
    year = np.array([i + (0.5 - random.random()) * 3.5 for i in old_year])
    Asia = np.array(continent == 'Asia')
    Europe = np.array(continent == 'Europe')
    Africa = np.array(continent == 'Africa')
    Americas = np.array(continent == 'Americas')
    Oceania = np.array(continent == 'Oceania')
    plt.plot([i for i in year * Asia if i], [i for i in lifeExp * Asia if i], 'o', c='red', markersize=9, label='Asia', fillstyle='top')
    plt.plot([i for i in year * Europe if i], [i for i in lifeExp * Europe if i], 'o',  c='black', markersize=9, fillstyle='bottom', label='Europe')
    plt.plot([i for i in year * Africa if i], [i for i in lifeExp * Africa if i], 'o', c='green', markersize=9, fillstyle='right', label='Africa')
    plt.plot([i for i in year * Americas if i], [i for i in lifeExp * Americas if i], 'o', c='blue', markersize=9, fillstyle='left', label='Americas')
    plt.plot([i for i in year * Oceania if i], [i for i in lifeExp * Oceania if i], 'o', c='magenta', markersize=9, fillstyle='full', label='Oceania')

    plt.grid(color='b', ls='-.', lw=0.1)
    plt.title("Differentiate continents by fillstyle")  # title
    plt.xlabel("year")  # x-axis
    plt.ylabel("life-expectancy")  # y-axis
    plt.legend(loc=2)
    plt.show()


def gdp_life_color():
    m3 = np.array(pop < 3000000)
    m3_m7 = np.array([True if 3000000 <= i < 7000000 else False for i in pop])
    m7_m15 = np.array([True if 7000000 <= i < 15000000 else False for i in pop])
    m15_m30 = np.array([True if 15000000 <= i < 30000000 else False for i in pop])
    m30_m80 = np.array([True if 30000000 <= i < 80000000 else False for i in pop])
    m80 = np.array(80000000 <= pop)
    plt.axes(xscale="log")
    plt.scatter([i for i in gdpPercap * m3 if i], [i for i in lifeExp * m3 if i], c='red', marker='o', label='<3M')
    plt.scatter([i for i in gdpPercap * m3_m7 if i], [i for i in lifeExp * m3_m7 if i], c='black', marker='o', label='3M~7M')
    plt.scatter([i for i in gdpPercap * m7_m15 if i], [i for i in lifeExp * m7_m15 if i], c='green', marker='o', label='7M~15M')
    plt.scatter([i for i in gdpPercap * m15_m30 if i], [i for i in lifeExp * m15_m30 if i], c='blue', marker='o', label='15M~30M')
    plt.scatter([i for i in gdpPercap * m30_m80 if i], [i for i in lifeExp * m30_m80 if i], c='yellow', marker='o', label='30M~80M')
    plt.scatter([i for i in gdpPercap * m80 if i], [i for i in lifeExp * m80 if i], c='magenta', marker='o', label='>80M')
    plt.title("Differentiate population by color")  # title
    plt.xlabel("gdp")  # x-axis
    plt.ylabel("life-expectancy")  # y-axis
    plt.legend(loc=2)
    plt.xlim((0, 140000))
    plt.show()


def gdp_life_size():
    m3 = np.array(pop < 3000000)
    m3_m7 = np.array([True if 3000000 <= i < 7000000 else False for i in pop])
    m7_m15 = np.array([True if 7000000 <= i < 15000000 else False for i in pop])
    m15_m30 = np.array([True if 15000000 <= i < 30000000 else False for i in pop])
    m30_m80 = np.array([True if 30000000 <= i < 80000000 else False for i in pop])
    m80 = np.array(80000000 <= pop)
    s = np.array(pop / 3000000)
    plt.axes(xscale="log")
    plt.scatter([i for i in gdpPercap * m3 if i], [i for i in lifeExp * m3 if i], c='red', marker='o', label='<3M', s=[i for i in s * m3 if i])
    plt.scatter([i for i in gdpPercap * m3_m7 if i], [i for i in lifeExp * m3_m7 if i], c='black', marker='o', label='3M~7M', s=[i for i in s * m3_m7 if i])
    plt.scatter([i for i in gdpPercap * m7_m15 if i], [i for i in lifeExp * m7_m15 if i], c='green', marker='o', label='7M~15M', alpha=0.9, s=[i for i in s * m7_m15 if i])
    plt.scatter([i for i in gdpPercap * m15_m30 if i], [i for i in lifeExp * m15_m30 if i], c='blue', marker='o', label='15M~30M', alpha=0.7, s=[i for i in s * m15_m30 if i])
    plt.scatter([i for i in gdpPercap * m30_m80 if i], [i for i in lifeExp * m30_m80 if i], c='yellow', marker='o', label='30M~80M', alpha=0.6, s=[i for i in s * m30_m80 if i])
    plt.scatter([i for i in gdpPercap * m80 if i], [i for i in lifeExp * m80 if i], c='magenta', marker='o', label='>80M', alpha=0.3, s=[i for i in s * m80 if i])
    plt.title("Differentiate population by size")  # title
    plt.xlabel("gdp")  # x-axis
    plt.ylabel("life-expectancy")  # y-axis
    plt.legend(loc=2)
    plt.xlim((0, 140000))
    plt.show()


def gdp_life_fillstype():
    m3 = np.array(pop < 3000000)
    m3_m7 = np.array([True if 3000000 <= i < 7000000 else False for i in pop])
    m7_m15 = np.array([True if 7000000 <= i < 15000000 else False for i in pop])
    m15_m30 = np.array([True if 15000000 <= i < 30000000 else False for i in pop])
    m30_m80 = np.array([True if 30000000 <= i < 80000000 else False for i in pop])
    m80 = np.array(80000000 <= pop)
    s = np.array(pop / 2000000)
    plt.axes(xscale="log")
    plt.plot([i for i in gdpPercap * m3 if i], [i for i in lifeExp * m3 if i], 'o', c='red', label='<3M', markersize=9, alpha=1, fillstyle='top')
    plt.plot([i for i in gdpPercap * m3_m7 if i], [i for i in lifeExp * m3_m7 if i], 'o', c='black', label='3M~7M', markersize=9, alpha=0.8, fillstyle='bottom')
    plt.plot([i for i in gdpPercap * m7_m15 if i], [i for i in lifeExp * m7_m15 if i], 'o', c='green', label='7M~15M', markersize=9, alpha=0.6, fillstyle='right')
    plt.plot([i for i in gdpPercap * m15_m30 if i], [i for i in lifeExp * m15_m30 if i], 'o', c='blue', label='15M~30M', markersize=9, alpha=0.4, fillstyle='left')
    plt.plot([i for i in gdpPercap * m30_m80 if i], [i for i in lifeExp * m30_m80 if i], 'o', c='cyan', label='30M~80M', markersize=9, alpha=0.3, fillstyle='full')
    plt.plot([i for i in gdpPercap * m80 if i], [i for i in lifeExp * m80 if i], 'o', c='magenta', label='>80M', markersize=9, alpha=0.2, fillstyle='none')
    plt.title("Differentiate population by fillstyle")  # title
    plt.xlabel("gdp")  # x-axis
    plt.ylabel("life-expectancy")  # y-axis
    plt.legend(loc=2)
    plt.xlim((0, 140000))
    plt.show()


def one_chart():
    year = np.array([i+(0.5-random.random())*3 for i in old_year])
    Asia = np.array(continent == 'Asia')
    Europe = np.array(continent == 'Europe')
    Africa = np.array(continent == 'Africa')
    Americas = np.array(continent == 'Americas')
    Oceania = np.array(continent == 'Oceania')

    s = np.array(pop / 2000000)
    plt.scatter([i for i in year * Asia if i], [i for i in lifeExp * Asia if i], c='red', marker='o', s=[i for i in s * Asia if i], label='Asia', alpha=0.5)
    plt.scatter([i for i in year * Europe if i], [i for i in lifeExp * Europe if i], c='black', marker='o', s=[i for i in s * Europe if i], label='Europe', alpha=0.5)
    plt.scatter([i for i in year * Africa if i], [i for i in lifeExp * Africa if i], c='green', marker='o', s=[i for i in s * Africa if i], label='Africa', alpha=0.5)
    plt.scatter([i for i in year * Americas if i], [i for i in lifeExp * Americas if i], c='blue', marker='o', s=[i for i in s * Americas if i], label='Americas', alpha=0.5)
    plt.scatter([i for i in year * Oceania if i], [i for i in lifeExp * Oceania if i], c='magenta', marker='o', s=[i for i in s * Oceania if i], label='Oceania', alpha=0.5)

    s = np.array(gdpPercap / 500)
    plt.scatter([i for i in year * Asia if i], [i for i in lifeExp * Asia if i], c='green', marker='s', s=[i for i in s * Asia if i], label='Asia', alpha=0.5)
    plt.scatter([i for i in year * Europe if i], [i for i in lifeExp * Europe if i], c='blue', marker='s', s=[i for i in s * Europe if i], label='Europe', alpha=0.5)
    plt.scatter([i for i in year * Africa if i], [i for i in lifeExp * Africa if i], c='magenta', marker='s', s=[i for i in s * Africa if i], label='Africa', alpha=0.5)
    plt.scatter([i for i in year * Americas if i], [i for i in lifeExp * Americas if i], c='red', marker='s', s=[i for i in s * Americas if i], label='Americas', alpha=0.5)
    plt.scatter([i for i in year * Oceania if i], [i for i in lifeExp * Oceania if i], c='black', marker='s', s=[i for i in s * Oceania if i], label='Oceania', alpha=0.5)
    plt.grid(color='b', ls='-.', lw=0.25)
    plt.title("Life Expectancy with color")  # title
    plt.xlabel("year")  # x-axis
    plt.ylabel("life-expectancy")  # y-axis
    plt.legend(loc=2)
    plt.show()


def one_chart1():
    Asia = np.array(continent == 'Asia')
    Europe = np.array(continent == 'Europe')
    Africa = np.array(continent == 'Africa')
    Americas = np.array(continent == 'Americas')
    Oceania = np.array(continent == 'Oceania')

    s = np.array(pop / 2000000)
    plt.axes(xscale="log")

    year_list = []
    mark_list = ['o', 'v', '1', 's', 'p', '*', '+', 'x', 'D', '|', '_', '4']
    for index, value in enumerate([1952, 1957, 1962, 1967, 1972, 1977, 1982, 1987, 1992, 1997, 2002, 2007]):
        year_list.append((mark_list[index], np.array(year == value)))
    for value in year_list:
        plt.scatter([i for i in gdpPercap * Asia * value[1] if i], [i for i in lifeExp * Asia * value[1] if i], c='red', marker=value[0],
                    s=[i for i in s * Asia * value[1] if i], alpha=0.5)
        plt.scatter([i for i in gdpPercap * Europe * value[1] if i], [i for i in lifeExp * Europe * value[1] if i], c='black', marker=value[0],
                    s=[i for i in s * Europe * value[1] if i], alpha=0.5)
        plt.scatter([i for i in gdpPercap * Africa * value[1] if i], [i for i in lifeExp * Africa * value[1] if i], c='green', marker=value[0],
                    s=[i for i in s * Africa * value[1] if i], alpha=0.5)
        plt.scatter([i for i in gdpPercap * Americas * value[1] if i], [i for i in lifeExp * Americas * value[1] if i], c='blue',
                    marker=value[0], s=[i for i in s * Americas * value[1] if i], alpha=0.5)
        plt.scatter([i for i in gdpPercap * Oceania * value[1] if i], [i for i in lifeExp * Oceania * value[1] if i], c='magenta',
                    marker=value[0], s=[i for i in s * Oceania * value[1] if i], alpha=0.5)

    plt.title("Life Expectancy with color")  # title
    plt.xlabel("year")  # x-axis
    plt.ylabel("life-expectancy")  # y-axis
    # plt.legend(loc=2)
    plt.show()


if __name__ == '__main__':
    gdp_life_fillstype()










