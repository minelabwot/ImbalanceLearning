Introduction
=====
We predict when the freezing failure is going to happen by analyzing some real-time data of industrial system without any prior domain knowledge. Meanwhile, we also proposed an imbalance learning algorithm for freezing failure prognostics-Easy-SMT. The file train.rar is the data sets, the file code.rar is the code for dealong with the question. 


Data Description
=====
The data is provided by a wind turbine manufacturer for PHM competition held by Chinese government (Ministry of Industry and Information Technology, MIIT), which is generated from SCADA of a wind electricity generation system. The data contains 28 dimensional continuous time series, including working conditions, environment parameters and state parameters.

Two wind turbine¡¯s data (#15 and #21) are available and labeled with normal and freezing durations (start time,
end time). It is noted that the unlabeled data in training dataset are ineffective data which are not used for training in our experiment. Each wind turbine contains three files:

1.*_data.csv: original data from SCADA, including time stamp, 26 sensors&actuator, and group information;
2.*_normalinfo.csv: the labeled normal durations, including start time and end time;
3.*_failureinfo.csv: the labeled freezing durations, including start time and end time;


Model 
========
The framework of dealing with the imbalance learning task on turbine wind data is proposed. The overall
learning and prediction pipeline consists of four parts: 1) Data preprocessing and feature extraction; 2)
Model selection and composition; 3) Model training and crossvalidation; 4) Fault prediction and result adjusting

#Data preprocessing and feature extraction

The time series are segmented into time windows by sliding window mechanism. The length of time window is denoted as K and sliding step as L.

#Model selection

we propose the Easy-SMT ensemble algorithm based on EasyEnsemble and SMOTE to deal with the class-imbalance problems in industrial system.

#Model training and crossvalidation

we perform a 5-fold cross validation based on XGBoost algorithm to verify the generalization performance of
our model. Each fold of training set is used as a validation dataset, the whole cross-validation process is repeated for five times, and final values from this method are the best of these five cross-validation runs.

#Fault prediction

We use the best classfier for the testing to predict the fault time. 


The detail description about code as follows:
1.timewindow.py: data preprocessing and set the windows length and slide step for feature extraction.
2.processing.py: transform the data into an available format for XGBoost input.
3.sampling.py: random undersampling and oversampling.
4.smote.py: SMOTE oversampling.
5.class.py: train for class.
6.score.py: train for score.
7.result_class.py: the proposed model for class results.
8.result_score.py: the proposed model for score results.


Experiments
=========
We use XGBoost for the base classifier. The installation steps can learn from http://blog.csdn.net/bon_mot/article/details/51742869.







