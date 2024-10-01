from flask import Flask, render_template, request
import itertools

app = Flask(__name__)

def count_star(word):
    return word.count("*")

def generate_combinations(name):
    temp = ['']
    
    for char in name:
        if char == "*":
            # Expand combinations with A-Z for each '*'
            new_temp = []
            for combination in temp:
                for letter in range(ord("A"), ord("Z") + 1):
                    new_temp.append(combination + chr(letter))
            temp = new_temp
        else:
            # Append the current character to each existing combination
            temp = [combination + char for combination in temp]
    
    return temp

@app.route("/", methods=["GET", "POST"])
def index():
    combinations = []
    if request.method == "POST":
        name = request.form["name"].upper()
        combinations = generate_combinations(name)
    
    return render_template("index.html", combinations=combinations)

if __name__ == "__main__":
    app.run(debug=True)
