import requests
import pandas as pd
import numpy as np
import random
import time

url = 'https://www.reddit.com/r/Android/'
columns = input("Please specified which columns to pull [hot,new,top,rising] : ")
url = url +columns+'.json'
posts = []
after = None

for a in range(40):
    if after == None:
        current_url = url
    else:
        current_url = url + '?after=' + after
    print(current_url)
    res = requests.get(current_url, headers={'User-agent': 'Pony Inc 1.0'})

    if res.status_code != 200:
        print('Status error', res.status_code)
        break

    current_dict = res.json()
    current_posts = [p['data'] for p in current_dict['data']['children']]
    posts.extend(current_posts)
    after = current_dict['data']['after']

    # COMPLETE THE CODE!
    if a > 0:
        prev_posts = pd.read_csv(f'../datasets/Android_{columns}.csv')
        current_df = pd.DataFrame(current_posts)
        pd.concat([prev_posts,current_df],axis=0).to_csv(f'../datasets/Android_{columns}.csv',index=False)
        print(f'{prev_posts.shape[0]+current_df.shape[0]} posts has been downloaded!')
    else:
        pd.DataFrame(posts).to_csv(f'../datasets/Android_{columns}.csv', index = False)

    # generate a random sleep duration to look more 'natural'
    sleep_duration = random.randint(2,6)
    print(f'Waiting for {sleep_duration} seconds')
    time.sleep(sleep_duration)

print(f'Successfully load Android_{columns} data!')
