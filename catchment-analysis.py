#!/usr/bin/env python3
"""Software for managing and tracking environmental data from our field project."""

import argparse

from catchment import models, views


def main(args):
    """The MVC Controller of the environmental data system.

    The Controller is responsible for:
    - selecting the necessary models and views for the current task
    - passing data between models and views
    """
    InFiles = args.infiles
    if not isinstance(InFiles, list):
        InFiles = [args.infiles]
    
    for filename in InFiles:
        measurement_data = models.read_variable_from_csv(filename)
        view_data = {'daily sum': models.daily_total(measurement_data),
                     'daily average': models.daily_mean(measurement_data),
                     'daily max': models.daily_max(measurement_data),
                     'daily min': models.daily_min(measurement_data)}
        views.visualize(view_data)


# In the terminal, run python catchment-analysis.py data/rain_data_2015-12.csv
if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description='A basic environmental data management system')

    parser.add_argument(
        'infiles',  # run python catchment-analysis.py -h in the terminal to get help information
        nargs='+',  # the + means: give me at least one argument but could be more
        help='Input CSV(s) containing measurement data')  # Explanation of what's happening (help information)
    # You can specify the below argument when you run the script
    # python catchment-analysis.py -m 'measure' data/rain_data_2015-12.csv
    # The argument is required and it has to be a string; this is not doing anything to the visualisation function
    parser.add_argument('-m', '--measurements',
                        help='Name of measurements data series to load',
                        required=True)
    
    args = parser.parse_args()

    main(args) # If the if statement
