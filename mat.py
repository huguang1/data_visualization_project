import pandas as pd
import matplotlib.pyplot as plt
import math
from scipy.ndimage import gaussian_filter1d
data_frame = pd.read_excel("minard-data.xlsx", engine='openpyxl')
city_lonc = list(data_frame.LONC)
city_latc = list(data_frame.LATC)
city_name = list(data_frame.CITY)
city_lont = list(data_frame.LONT)
city_temp = list(data_frame.TEMP)
city_days = list(data_frame.DAYS)
city_mon = list(data_frame.MON)
city_day = list(data_frame.DAY)
surv_lonp = list(data_frame.LONP)
surv_latp = list(data_frame.LATP)
surv_surv = list(data_frame.SURV)
surv_dir = list(data_frame.DIR)
surv_div = list(data_frame.DIV)

plt.scatter(city_lonc, city_latc, c='green', marker='+', label='+1 points')
for i in range(len(city_lonc)):
    plt.text(city_lonc[i], city_latc[i], city_name[i])

for i, value in enumerate(surv_div):
    if i == len(surv_div) - 1:
        continue
    if surv_dir[i] == 'A':
        color = 'r'
    else:
        color = 'g'
    width = math.pow(surv_surv[i] / 5000, 3/4) * 2
    # width = surv_surv[i] / 10000
    if value == 1:
        plt.plot([surv_lonp[i], surv_lonp[i + 1]], [surv_latp[i], surv_latp[i + 1]], linewidth=width, color=color)
    if value == 2:
        plt.plot([surv_lonp[i], surv_lonp[i + 1]], [surv_latp[i], surv_latp[i + 1]], linewidth=width, color=color)
    if value == 3:
        plt.plot([surv_lonp[i], surv_lonp[i + 1]], [surv_latp[i], surv_latp[i + 1]], linewidth=width, color=color)


plt.title("ASSIONMENT LOGISTIC REGRESSION")  # title
plt.xlabel("first_feature")  # x-axis
plt.ylabel("second_feature")  # y-axis
plt.legend(loc=0, bbox_to_anchor=(1, 1))
plt.show()




