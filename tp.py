import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import time
import threading
from scipy.ndimage import gaussian_filter1d

# In[2]:


eeg_recording = pd.read_csv('../Sleep Data/raw_data_1/101/PSG_raw/C3.txt', sep=' ', skiprows=7, header=None)
eeg_recording.columns = ['data']


# In[3]:


eeg_numpy = np.array(eeg_recording['data'])


# In[4]:


eeg_numpy = eeg_numpy[:-128]


# In[5]:


allData = np.array(np.split(eeg_numpy, len(eeg_numpy)/(128*30)))

from concurrent.futures import ThreadPoolExecutor

encoded_items = []

def task(threadData):
    num_filters = 100
    l = threading.Lock()
    for data in threadData:
        item = []        
        for i in range(num_filters):
            y = gaussian_filter1d(data, i + 1)
            item.append(y)
        with l:    
            encoded_items.append(item)
    print("Processing {}".format(threading.current_thread()))

def main():
 print("Starting ThreadPoolExecutor")
 with ThreadPoolExecutor(max_workers=3) as executor:
   future = executor.submit(task, (allData[:300]))
   future = executor.submit(task, (allData[300:400]))
   future = executor.submit(task, (allData[400:]))
 print("All tasks complete")

if __name__ == '__main__':
    start_time = time.time()
    main()
    parallel_time = time.time() - start_time
    print('Parallel Time: ', parallel_time)
    print('Speedup: ', 97.36/parallel_time)
    print('P', sum(np.array(encoded_items)))