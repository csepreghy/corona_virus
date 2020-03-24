import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib import rcParams
import numpy as np

rcParams.update({'font.sans-serif': 'Arial'})

denmark_cases = [1, 2, 3, 4, 4, 10, 15, 20, 23, 29, 37, 92, 264, 516, 676, 804, 836, 875, 932, 1024, 1115, 1223, 1335, 1418, 1512, 1582]
denmark_recovered = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1]
denmark_x = ['27-02-2020', '28-02-2020', '29-02-2020', '01-03-2020', '02-03-2020',
             '03-03-2020', '04-03-2020', '05-03-2020', '06-03-2020', '07-03-2020',
             '08-03-2020', '09-03-2020', '10-03-2020', '11-03-2020', '12-03-2020',
             '13-03-2020', '14-03-2020', '15-03-2020', '16-03-2020', '17-03-2020',
             '18-03-2020', '19-03-2020', '20-03-2020', '21-03-2020', '22-03-2020',
             '23-03-2020']

print(f'len(denmark_cases) = {len(denmark_cases)}')
print(f'len(denmark_cases) = {len(denmark_recovered)}')
print(f'len(denmark_cases) = {len(denmark_x)}')


hungary_cases = [2, 3, 4, 7, 9, 12, 12, 13, 16, 19, 30, 32, 39, 50, 58, 73, 85, 103, 131, 167, 188]
hungary_recovered = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 2, 2, 2, 7, 7, 16, 16, 16]
hungary_x = ['04-03-2020', '05-03-2020', '06-03-2020', '07-03-2020', '08-03-2020',
             '09-03-2020', '10-03-2020', '11-03-2020', '12-03-2020', '13-03-2020',
             '14-03-2020', '15-03-2020', '16-03-2020', '17-03-2020', '18-03-2020',
             '19-03-2020', '20-03-2020', '21-03-2020', '22-03-2020', '23-03-2020',
             '24-03-2020']

print(f'len(hungary_cases) = {len(hungary_cases)}')
print(f'len(hungary_cases) = {len(hungary_recovered)}')
print(f'len(hungary_cases) = {len(hungary_x)}')

background_color = '#1C2024'
grid_color = '#444444'
c_orange = '#F2B134'
c_green = '#62BF04'
c_red = '#ED553B'
c_white = '#FFFFFF'
c_green = '#62BF04'
legend_color = '#282D33'

fig, axs = plt.subplots(nrows=2, figsize=(10, 7))
fig.patch.set_facecolor(background_color)

for ax in axs:
    ax.set_facecolor(background_color)
    ax.tick_params(colors=c_white)
    ax.xaxis.label.set_color(c_white)
    ax.yaxis.label.set_color(c_white)
    ax.grid(True, color=grid_color)


plt.setp(axs[0].xaxis.get_majorticklabels(), rotation=45)
plt.setp(axs[1].xaxis.get_majorticklabels(), rotation=45)

axs[0].plot(denmark_x, denmark_cases, color=c_red, label='Total Cases')
axs[0].plot(denmark_x, denmark_recovered, color=c_green, label='Recovered')
axs[0].set_title('Denmark', color=c_white)
legend_0 = axs[0].legend(facecolor=legend_color)

axs[1].plot(hungary_x, hungary_cases, color=c_white, label='Total Cases')
axs[1].plot(hungary_x, hungary_recovered, color=c_green, label='Recovered')
axs[1].set_title('Hungary', color=c_white)
legend_1 = axs[1].legend(facecolor=legend_color)

for text in legend_0.get_texts():
    text.set_color("white")
for text in legend_1.get_texts():
    text.set_color("white")

fig.suptitle('Coronavirus Cases', color=c_white, size=16)
fig.subplots_adjust(hspace=0.6)
plt.show()