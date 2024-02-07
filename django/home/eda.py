import os
import pandas as pd
import matplotlib
import matplotlib.ticker as ticker
import numpy as np
import seaborn as sns
from matplotlib import pyplot as plt
from core.settings import STATIC_HOME_ROOT
from django.templatetags.static import static
from django.http import HttpResponse


class DataAnalysis:
    def __init__(self):
        self.date = '2024-02-01'
        self.file_path = os.path.join(STATIC_HOME_ROOT, 'assets', 'data', f'iproperty_new_listed_projects_{self.date}_eda.csv')
        self.df_house = pd.read_csv(self.file_path)
        self.df_project = self.df_house.copy()
        # drop information related to unit type
        self.df_project.drop(['price', 'built_up_size', 'bedroom', 'bathroom', 'car_park'], axis=1, inplace=True)
        matplotlib.use('SVG')

    def plot_pie_chart(self, data, target_column, agg_count_column, title):
        target = data[target_column].value_counts().reset_index(name='total')
        plt.pie(
            x=target['total'], 
            labels=target[target_column],
            autopct='%1.2f%%',
            colors=sns.color_palette('colorblind'),
            startangle=90,
            wedgeprops={'linewidth': 1.0, 'edgecolor': 'white'},
        )
        plt.tight_layout()
        plt.title(title)
        return plt

    def get_status_pie_chart(self):
        self.plot_pie_chart(self.df_project, 'status', 'title', f"Status for Housing Properties Listed on iProperty.com.my\n{self.date}")
        response = HttpResponse(content_type="image/png")
        plt.savefig(response, format="png", transparent=True)
        return response