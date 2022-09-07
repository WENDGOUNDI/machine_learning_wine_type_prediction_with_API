# Machine Learning API For Wine Type Prediction
The aim of this project is to develop a machine learning model able to predict the type of wine after receiving data regarding its characteristics. The machine learning model is trained using three different models: DecisionTreeClassifier, MLPClassifier and RandomForestClassifier. Once training is completed, we convert the model into API for production use.

# Dependencies
 - Pickle
 - Numpy
 - Requests
 - Json
 - Flask
 - Matplotlib
 - Pandas
 - Seaborn
 - Sklearn
 
 
# Datasets
The wine type prediction dataset is a classic multi-class classification dataset. It has 3 classes respectively large of 59,71 and 48 elements. The total sample is 178. It can be downloaded via sklearn.
 ## Preview the dataset
 ![dataset_preview](https://user-images.githubusercontent.com/48753146/188765069-8e5cb5a3-1417-4c86-b8a0-7f828b16cdb8.PNG)

 ## Class repartition
 ![target_repartition](https://user-images.githubusercontent.com/48753146/188765064-243e3c40-6a82-43c8-9562-6f5c257b9438.PNG)
 
 
 # Training result:
  - Accuracy Score on RandomForestClassifier() is: 95.0%
  - Accuracy Score on MLPClassifier() is: 85.0%
  - Accuracy Score on DecisionTreeClassifier() is: 85.0%
  Models are saved into pickle file after the training.
  
  # API
  the API is built via flask.
  ![model](https://user-images.githubusercontent.com/48753146/188765938-f228c564-d90e-4808-ab12-f44538128ff1.PNG)
 
 

