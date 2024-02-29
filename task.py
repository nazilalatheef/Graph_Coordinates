from flask import Flask, jsonify

app = Flask(__name__)

#define the end point
@app.route('/get_coordinates', methods=['GET'])
def get_coordinates():
    # Read coordinates from the text file
    coordinates = read_coordinates_from_file('coordinates.txt')

    # Return coordinates in JSON format
    return jsonify(coordinates)

def read_coordinates_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()

    # Extract x and y values from each line
    coordinates = [tuple(map(int, line.strip().split(', '))) for line in lines]
    return [{'x': x, 'y': y} for x, y in coordinates]

if __name__ == '__main__':
    app.run(debug=True, port=8080)
