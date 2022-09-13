# import python libraries

import matplotlib.pyplot as plt
import os
import pandas as pd
import requests
import sys
import xarray as xr

from matplotlib.dates import DateFormatter
from time import sleep

#To find a threshold value throug EPE
import pandas as pd
gauge_name = 'San Saba River near Brady'
lcra_file = pd.read_csv(f'./LCRA_test_github/{gauge_name}.csv')
print(lcra_file)
lcra_file['discharge'] = lcra_file['value']/35.3147
lcra_file = lcra_file.set_index(pd.to_datetime(lcra_file['timestamp']))
max_monthly_discharge = lcra_file['discharge'].resample('M').max()

data = max_monthly_discharge.sort_values(ascending = False)
N = len(data.index)
data = data.to_frame()
data['rank'] =data.rank()     #Rank
data['return_period'] = data['rank']/(N+1)  #unit is per month
data['prob of exceedance'] = 1/(data['return_period'])
data['prob of exceedance'].max()