#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pandas as pd
from plot.bars import HotUsers

hot_users_path = "data/hot_users.csv"

hot_users = pd.read_csv(hot_users_path).sort_values(["hotness"], ascending=False)


HotUsers().bar(hot_users, plot=False)


print(hot_users.reset_index().to_json(orient='records'))