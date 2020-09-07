## React-Django Image Classifier

### Webapp that classifies an uploaded image <br/>
Techs: <br/>

* Frontend : React.js
* Backend: Django Rest Api

### Example Prediction
![Output sample](https://github.com/hrithikkothari1234/Image-Classifier/raw/master/example/examplepred.gif)

### Homepage after prediction 
![](https://github.com/hrithikkothari1234/Image-Classifier/blob/master/example/predicted_example.png)

### Historypage with all previous predictions 
![](https://github.com/hrithikkothari1234/Image-Classifier/blob/master/example/historypage.png)

### To clone this project
1) Setup Frontend

```
$ cd frontend_react
$ npm install           
$ npm start              
```

2) Setup Backend

```
$ cd backend_djangoapi
$ pip install requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```