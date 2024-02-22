from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('plan.html')

@app.route('/generate_plan', methods=['POST'])
def generate_plan():
    # Get user input from the form
    age = int(request.form['age'])
    workout_time_preference = request.form['workout-time']
    # Get other input fields

    # Process user input and generate fitness plan
    # You can add your fitness planner logic here

    # For demonstration purposes, let's assume we generate a sample plan
    fitness_plan = {
        'age': age,
        'workout_time_preference': workout_time_preference,
        # Add other parameters
    }

    # Render the plan template with the generated fitness plan
    return render_template('plan.html', fitness_plan=fitness_plan)

if __name__ == '__main__':
    app.run(debug=True)
