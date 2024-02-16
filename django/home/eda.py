import io
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
from threading import Thread, Lock

class DataAnalysis:
    def __init__(self):
        self.date = '2024-02-01'
        self.title = f'New Housing Properties Listed on iProperty.com.my\n{self.date}'
        self.file_path = os.path.join(STATIC_HOME_ROOT, 'assets', 'data', f'iproperty_new_listed_projects_{self.date}_eda.csv')
        # read data from csv file
        df = pd.read_csv(self.file_path)
        # we only interested in housing price, get house category from the data frame
        self.df_house = df[df.category=='House']
        self.df_project = self.df_house.copy()
        # drop information related to unit type
        self.df_project.drop(['price', 'built_up_size', 'bedroom', 'bathroom', 'car_park'], axis=1, inplace=True)
        # drop duplicated rows
        self.df_project.drop_duplicates(inplace=True)
        self.lock = Lock()
        matplotlib.use('SVG')
    
    def get_title(self):
        return self.title

    def plt_to_svg(self, transparent=False):
        buf = io.BytesIO()
        plt.savefig(buf, format='svg', bbox_inches='tight', transparent=transparent)
        svg = buf.getvalue()
        buf.close()
        plt.cla() # clean up plt so it can be re-used
        return svg

    def plot_pie_chart(self, data, target_column, title):
        self.lock.acquire()
        plt.figure(figsize = (6, 5))
        target = data[target_column].value_counts().reset_index(name='total')
        plt.pie(
            x=target['total'],
            autopct='%1.2f%%',
            colors=sns.color_palette('colorblind'),
            startangle=90,
            wedgeprops={'linewidth': 1.0, 'edgecolor': 'white'}, 
            textprops={'color':"w"}
        )
        plt.legend(target[target_column], loc=2, fontsize='small', fancybox=True)
        plt.title(title, fontdict={'weight': 'bold'}, color='white')
        svg = self.plt_to_svg(True)
        self.lock.release()
        return svg    

    def get_status_pie_chart(self):
        svg = self.plot_pie_chart(self.df_project, 'status', "Status")
        response = HttpResponse(svg, content_type='image/svg+xml')
        return response
    
    def get_status_pie_chart_description(self):
        return 'Nearly 80% of the housing properties are new launch and open for sale property with 56.07% of new launch property and 23.36% of open for sale property.'

    def get_tenure_pie_chart(self):
        svg = self.plot_pie_chart(self.df_project, 'tenure', "Tenure")
        response = HttpResponse(svg, content_type='image/svg+xml')
        return response

    def get_tenure_pie_chart_description(self):
        return 'More than 90% of the housing properties are freehold and leasehold property with 66.36% of freehold property and 32.71% of leasehold property.'

    def get_land_title_pie_chart(self):
        svg = self.plot_pie_chart(self.df_project, 'land_title', "Land Title")
        response = HttpResponse(svg, content_type='image/svg+xml')
        return response
    
    def get_land_title_pie_chart_description(self):
        return 'Close to two thirds of the housing properties are residential land title.'
    
    def plot_bar_chart(self, data, target_column, title, xlabel, ylabel):
        self.lock.acquire()
        target = data[target_column].value_counts(sort=True).reset_index(name='total')
        fig, ax = plt.subplots(figsize=(8, 5))
        figplot = sns.barplot(
            data=target,
            y='total',
            x=target_column, 
            hue=target_column,
            palette='colorblind',
            estimator=lambda x: sum(x)*100.00/target['total'].sum(),
            ax=ax)
        #plt.tight_layout()
        plt.xlabel(xlabel, color='black')
        plt.ylabel(ylabel, color='black')
        plt.title(title, fontdict={'weight': 'bold'}, color='black')
        plt.xticks(rotation="vertical", color='black')
        plt.yticks(color='black')
        plt.tick_params(axis='both', which='major', labelsize=9)
        # show percentage on bar for first 3 bars
        for index, row in target.iterrows():
            y = row.total*100.00/target['total'].sum()
            figplot.text(row.name, y + 0.15, f'{y:.2f}%', fontsize=9, color='black')
            if index == 2:
                break        
        svg = self.plt_to_svg()
        self.lock.release()
        return svg
    
    def get_property_type_bar_chart(self):
        svg = self.plot_bar_chart(self.df_project, 'type', "Property Type", 'Property Type', 'Precentage')
        response = HttpResponse(svg, content_type='image/svg+xml')
        return response
    
    def get_property_type_bar_chart_description(self):
        return "Top 3 housing property types are 2-sty terrace/link house 28.04%, service residence 27.10% and condominium 13.08%."

    def get_state_bar_chart(self):
        svg = self.plot_bar_chart(self.df_project, 'state', "State", 'State', 'Precentage')
        response = HttpResponse(svg, content_type='image/svg+xml')
        return response
    def get_state_bar_chart_description(self):
        return "Top 3 states are Selangor 57.01%, Johor 15.89% and Kuala Lumpur 14.02%. More than half of the housing properties listed on iProperty.com.my are in Selangor state. Terengganu, Sabah, Pahang, and Kedah only have one property projet listed on iProperty.com.my."

    def get_city_bar_chart(self):
        svg = self.plot_bar_chart(self.df_project, 'city', "City", 'City', 'Precentage')
        response = HttpResponse(svg, content_type='image/svg+xml')
        return response
    
    def get_city_bar_chart_description(self):
        return "Top 3 cities are Shah Alam 9.35%, Johor Bahru 6.54% and Semenyih 5.61%. Top 10 cities are in Selangor and Johor."

    def plot_price_box_plot(self, data):
        self.lock.acquire()
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.boxplot(ax=ax, data=data, x='price')
        upper_quartile = data.price.quantile(0.75)
        lower_quartile = data.price.quantile(0.25)
        iqr = upper_quartile - lower_quartile
        upper_whisker_end = upper_quartile + 1.5 * iqr
        plt.annotate(f'RM{upper_whisker_end:,.2f}', 
                            xy=(upper_whisker_end, 0.025), 
                            xytext=(upper_whisker_end + 2 * 250_000, 0.2), 
                            fontsize=10, 
                            color='blue', 
                            arrowprops=dict(arrowstyle= '->', color='blue', lw=1.0, ls='--'))
        price_median = self.df_house.price.median()
        plt.annotate(f'RM{price_median:,.2f}', 
                     xy=(price_median, 0.025), 
                     xytext=(price_median + 2 * 250_000, 0.35), 
                     fontsize=10, 
                     color='blue', 
                     arrowprops=dict(arrowstyle= '->', color='blue', lw=1.0, ls='--'))
        plt.title("Housing Price", fontdict={'weight': 'bold'}, color='black')
        plt.xlabel("Price (RM)", color='black')
        svg = self.plt_to_svg()
        self.lock.release()
        return svg

    def get_price_box_plot(self):
        svg = self.plot_price_box_plot(self.df_house)
        response = HttpResponse(svg, content_type='image/svg+xml')
        return response

    def get_price_box_plot_description(self):
        return "Housing price distribution is skewed to the right with median value of RM805,888.00 and mean value of RM1,002,233.58. Outliers are observerd beyond RM2,264,374.00."

    def plot_price_hist(self, data, y_mean_annotate, y_median_annotate, title):
        self.lock.acquire()
        fig, ax = plt.subplots()
        fig.set_size_inches(9, 4)
        fig.tight_layout()
        tick_spacing=250_000 # set spacing for each tick
        ax.xaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))
        sns.histplot(ax=ax, data=data.price, kde=True, bins=100)
        plt.title(title, fontdict={'weight': 'bold'}, color='black')
        plt.xlabel("Price (RM)", color='black')
        plt.ylabel("Number of Properties", color='black')
        plt.axvline(data.price.median(), c='darkorange')
        plt.annotate(f'Median (RM{data.price.median():,.2f})', 
                        xy=(data.price.median(), y_median_annotate), 
                        xytext=(data.price.median() + 2 * tick_spacing, y_median_annotate - 0.5), 
                        fontsize=10, 
                        color='blue', 
                        arrowprops=dict(arrowstyle= '->', color='blue', lw=1.0, ls='--'))
        plt.axvline(data.price.mean(), c='darkorange')
        plt.annotate(f'Mean (RM{data.price.mean():,.2f})', 
                        xy=(data.price.mean(), y_mean_annotate), 
                        xytext=(data.price.mean() + 2 * tick_spacing, y_mean_annotate - 0.5), 
                        fontsize=10,
                        color='blue', 
                        arrowprops=dict(arrowstyle= '->', color='blue', lw=1.0, ls='--'))
        svg = self.plt_to_svg()
        self.lock.release()
        return svg

    def get_price_hist_plot(self):
        upper_quartile = self.df_house.price.quantile(0.75)
        lower_quartile = self.df_house.price.quantile(0.25)
        iqr = upper_quartile - lower_quartile
        upper_whisker_end = upper_quartile + 1.5 * iqr
        df_house_price_remove_outliers = self.df_house[self.df_house.price < upper_whisker_end]
        svg = self.plot_price_hist(df_house_price_remove_outliers, 7, 6, "Distribution of Housing Price")
        response = HttpResponse(svg, content_type='image/svg+xml')
        return response
    
    def get_price_hist_plot_description(self):
        return "With the removal of the properties with price > RM2,264,374.00, mean value is closer to median value. Most of the price for housing properties listed on iProperty.com.my in RM250,000 to RM1,250,000 range."

    def plot_price_category_box(self, data, y, ylabel, title, ylabel_rotation):
        self.lock.acquire()
        fig, ax = plt.subplots(figsize=(6, 4))
        figplot = sns.boxplot(ax=ax, data=data, x='price', y=y, hue=y, palette="husl")
        plt.title(title, fontdict={'weight': 'bold'}, color='white')
        plt.xlabel("Price (RM)", color='white')
        plt.ylabel(ylabel, color='white')
        plt.xticks(color='white')
        plt.yticks(rotation=ylabel_rotation, color='white')
        # iterate over boxes
        for i,box in enumerate(figplot.patches):
            box.set_edgecolor('white')
            #box.set_facecolor('white')
            # iterate over whiskers and median lines
            for j in range(6*i,6*(i+1)):
                figplot.lines[j].set_color('white')
        svg = self.plt_to_svg(True)
        self.lock.release()
        return svg
    
    def get_price_state_box_plot(self):
        svg = self.plot_price_category_box(self.df_house, 'state', 'State', "State vs Housing Price", 0)
        response = HttpResponse(svg, content_type='image/svg+xml')
        return response
    
    def get_price_state_box_plot_description(self):
        return "Terengganu, Sabah, Pahang, and Kedah only have one property projet listed on iProperty.com.my, hence distribution of box plot for these states do not provide much information. Kuala Lumpur has the highest median price value, RM922,5000. As Kuala Lumpur is the most developed state in Malaysia, and thus has the highest housing demand. Housing price for Kuala Lumpur is also more dispersed compared to other states. Selangor has the second highest median price value, RM851,000 as it is next to Kuala Lumpur and also one of the developed state in Malaysia. Johor has the third highest median price vlaue, RM790,500 due to it strategic location that near to Singapore and being one of the top choice of location for Malaysia My Second Home (MM2H). It is worth to note also the 25th percentile for all the states are above RM500,000."

    def get_price_land_title_box_plot(self):
        svg = self.plot_price_category_box(self.df_house, 'land_title', 'Land Title', "Land Title vs Housing Price", 0) 
        response = HttpResponse(svg, content_type='image/svg+xml')
        return response
    
    def get_price_land_title_box_plot_description(self):
        return "Overall housing price for residential land title is higher than commercial land title, suggesting that there might be an association between land title and housing price. Median price value for residential land title is higher than 75th percentile price value of commercial land title. Price value for property with residential land title is more dispersed than property with commercial land title."

    def get_price_tenure_box_plot(self):
        svg = self.plot_price_category_box(self.df_house, 'tenure', 'Tenure', "Tenure vs Housing Price", 0)
        response = HttpResponse(svg, content_type='image/svg+xml')
        return response
    
    def get_price_tenure_box_plot_description(self):
        return "There is only property project with Malay reserved land tenure and hence its distribution does not provide much information. Overall the housing for price for freehold properties is higher and dispersed than leasehold properties, suggesting that there might be an association between tenure type and housing price. Freehold properties are usually more expensive than leasehold properties, partly because of the higher demand on the market and risks attached to leasing for leasehold properties."

    def plot_price_built_up_size_scatter_plot(self, data, hue, legend_title, title):
        self.lock.acquire()
        fig, ax = plt.subplots(figsize=(6, 4))
        sns.scatterplot(ax=ax, data=data, x='price', y='built_up_size', hue=hue)
        plt.xlabel('Built Up Size (sqft)')
        plt.ylabel('Price (RM)')
        plt.title(title, fontdict={'weight': 'bold'})
        plt.legend(title=legend_title,loc=4, fontsize='small', fancybox=True)
        svg = self.plt_to_svg()
        self.lock.release()
        return svg
    
    def get_price_state_scatter_plot(self):
        svg = self.plot_price_built_up_size_scatter_plot(self.df_house, 'state', 'State', "Housing Price vs Built Up Size (State)") 
        response = HttpResponse(svg, content_type='image/svg+xml')
        return response
    
    def get_price_state_scatter_plot_description(self):
        return "Housing price is positive correlated with build up size is observed for different states."

    def get_price_land_title_scatter_plot(self):
        svg = self.plot_price_built_up_size_scatter_plot(self.df_house, 'land_title', 'Land Title', "Housing Price vs Built Up Size (Land Title)") 
        response = HttpResponse(svg, content_type='image/svg+xml')
        return response

    def get_price_land_title_scatter_plot_description(self):
        return "Housing price is positive correlated with build up size is observed for different land titles."

    def get_price_tenure_scatter_plot(self):
        svg = self.plot_price_built_up_size_scatter_plot(self.df_house, 'tenure', 'Tenure', "Housing Price vs Built Up Size (Tenure)") 
        response = HttpResponse(svg, content_type='image/svg+xml')
        return response
    
    def get_price_tenure_scatter_plot_description(self):
        return "Housing price is positive correlated with build up size is observed for different tenure types."
    