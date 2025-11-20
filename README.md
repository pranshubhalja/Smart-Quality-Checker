##### Smart Quality Checker



This project proposes a system that monitors various parameters in manufacturing in real-time and detects deviations using statistical methods and machine learning. 



Data: Contains the original dataset downloaded from Kaggle (CSV file).



EDA: Contains an HTML exploratory data analysis report.



Feature\_engineering: Contains a Python script that computes control limits and adds two new columns (status\_detail and severity).



Data\_with\_status: Contains the processed dataset with the new engineered columns.



Control\_chart\_code: Contains a Python script used to generate control charts for all variables.



Control\_charts: Contains the output control chart images for each variable.



###### Data

The dataset includes the following variables:

Current\_Temperature, Temperature\_Error, Overshoot, Response\_Time, Steady\_State\_Error, Ambient\_Temperature, Humidity.

These features represent performance measurements of a control system.



###### EDA

The eda\_report.html file includes:



* Missing value analysis
* Data type inspection
* Descriptive statistics
* Variable interactions
* Correlation analysis
* Sample preview of the dataset



###### Feature Engineering

The feature\_engineering.py script:



* Calculates upper and lower control limits for each variable
* Determines whether each data point is in control or out of control



Creates two new fields:



1. status\_detail: indicates whether the row is within control limits
2. severity: identifies which variable is out of control and by how much



###### Data With Status

The processed dataset includes all original variables plus status\_detail and severity. This dataset is suitable for monitoring, anomaly detection, or further modeling.



###### Control Chart Code

The control\_charts.py script:



* Reads the processed dataset
* Computes control limits
* Produces control charts for each variable
* Saves the charts in the Control\_charts folder



###### Control Charts

This folder contains the generated PNG images of control charts for:

Current Temperature, Response Time, Steady State Error, Ambient Temperature, and Humidity. These charts highlight points outside the control limits.
