This project is to generate a random data of coordinate points of a linear progression graph and use a microservice to display the same in json format.

**#Prerequisites -**
Python (version 3.12)
Flask (version 3.0.2)
To install flask, use: **_pip install flask_**

**#How to use -**
Navigate to the project directory and create the data in a textfile using:
**_python create_coordinates_data.py_**

Run the Flask microservice using:
**_python task.py_**
The microservice will then be accessible at **http://127.0.0.1:8080**

**#Usage -**
Endpoint for Coordinates: **http://127.0.0.1:8080/get_coordinates**

The microservice returns the coordinate values from the coordinates.txt file in JSON format.
