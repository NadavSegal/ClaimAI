import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import config_local
import logging

_logger = logging.getLogger(__name__)


class PrepareData:

    def __init__(self):
        path_str = './data/' + config_local.data_clean['data_file_name'] + '.csv'
        self.ds = pd.read_csv(path_str)

    def clean(self):
        # self.ds = self.ds.dropna(how='all')

        self.add()

    def add(self):
        self.ds['incident_month'] = pd.to_datetime(self.ds['incident_date']).dt.month
        self.ds['incident_day'] = pd.to_datetime(self.ds['incident_date']).dt.day
        self.ds['claim_outcome'] = ((np.random.rand() - 0.5) * 0.15 + 1) * self.ds[
            'total_claim_amount'] + np.random.rand()


class Descriptive:

    def __init__(self, data):
        self.ds = data.ds
        self.fields = config_local.data_clean['top_chart_fields']
        self.fig_n = 1

    def top_chart(self):
        for field in self.fields:
            chart_sum = self.ds.groupby([field]).sum()['claim_outcome'] / 1000000
            chart_mean = self.ds.groupby([field]).mean()['claim_outcome'] / 1000
            # keys = [incident_month for incident_month, df in self.ds.groupby([field])]
            self.fig_chart(chart_sum, str(field) + ' - total', 'Total - claim outcome[M$]')
            self.fig_chart(chart_mean, str(field) + ' - mean', 'Mean - claim outcome[K$]')

    def fig_chart(self, y, title, y_lab):
        plt.figure(self.fig_n)
        plt.xlabel('Criteria')
        plt.ylabel(y_lab)
        plt.title(title)
        plt.grid()
        plt.xticks(rotation=45, size=8)
        plt.bar(y.keys(), y)
        plt.show(block=False)
        plt.savefig('./output/' + title + '.png')
        self.fig_n += 1


class Figures:

    def __init__(self, fig_n, title, ylab):
        self.fig = plt
        self.fig_n = fig_n
        self.fig.figure(fig_n)
        self.fig.xlabel('Criteria')
        self.fig.ylabel(ylab)
        self.fig.title(title)
        self.fig.show(block=False)
        self.fig.grid()

    def plot_bar(self, chart_sum, keys):
        self.fig.figure(self.fig_n)
        self.fig.xticks = keys
        self.fig.bar(keys, chart_sum)
        self.fig.draw()

