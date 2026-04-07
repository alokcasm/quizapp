import json
import random
import sqlite3
from flask import Flask, render_template, request, session, redirect


app = Flask(__name__)
app.secret_key = 'alok' #secret key to encrypt browser cookie 

#sqlite db
def init_db():
    conn = sqlite3.connect('database.db')
    c = conn.cursor() #for executing sqlite query

    c.execute('''
        CREATE TABLE IF NOT EXISTS leaderboard (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            score REAL
        )
    ''')

    conn.commit() #to save in db if we didn't use commit() data will not saved
    conn.close()

#load json file for questions
# f = open("data/questions.json")
# questions = json.load(f) #parsed into dictionary
# f.close()

#reading data/questions.json file
with open("data/questions.json") as f:
    questions = json.load(f) #coversion json-disctionary


#routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/start_quiz', methods=['POST'])
def start_quiz():
    #gettingg username and username from form by post method
    username = request.form['username'] 
    category = request.form['category']

    session['username'] = username #store username
    session['category'] = category   # store category

    return redirect('/quiz')


@app.route('/quiz')
def quiz():
    if 'username' not in session: #if username is not stored in browser cookie
        return redirect('/')  #redirect to index.html

    category = session.get('category') #getting category from browser cookie
    filtered_questions = [] # iniializing filtered question with null list
    for q in questions:
        if q['category'] == category:  #comparing json question category to user selected cateogry
            filtered_questions.append(q) #appending in filter_questions array
            
    if not filtered_questions:
        return "No questions available for this category!" #if filter_questions found null

    num_questions = 10
    selected_questions = random.sample(filtered_questions, num_questions) #we used random.sample() to get random questions

    session['questions'] = selected_questions #storing selected questions in browser cookie

    return render_template('quiz.html', questions=selected_questions)

@app.route('/result', methods=['POST'])
def result():
    if 'questions' not in session:
        return redirect('/')  #checks there is questions in cookie or not if not it will redirect to home

    #initializing score and negative marks with 0 and results with empty list
    score = 0
    negative_marks = 0
    results = []

    selected_questions = session.get('questions', []) #getting selected question from cookie

    for q in selected_questions: #we used loop to check answers of all questions
        user_answer = request.form.get(str(q['id'])) #getting user answer 
        correct_answer = q['answer']

        #calculating marks correct = +1,incorrect = -0.25 also added result_status
        if user_answer:
            if user_answer == correct_answer:
                score += 1
                result_status = "Correct"
            else:
                negative_marks += 0.25
                result_status = "Wrong"
        else:
            result_status = "Not Attempted"

        #Storing result for review
        results.append({
            "question": q['question'],
            "your_answer": user_answer if user_answer else "Not Answered",
            "correct_answer": correct_answer,
            "status": result_status
        })

    final_score = score - negative_marks #final score for negative marking

    total_questions = len(selected_questions) #getting length of selected questions

    #calculating percentage
    percentage = (score / total_questions) * 100 if total_questions > 0 else 0

    status = "Pass" if percentage >= 40 else "Fail" #pass or fail in test

    #clear questions from cookie after form submission 
    session.pop('questions', None)

    return render_template('result.html',
                           score=score,
                           negative=negative_marks,
                           final=final_score,
                           percentage=round(percentage, 2),
                           status=status,
                           results=results)


@app.route('/save_score', methods=['POST'])
def save_score():
    name = session.get('username')
    score = float(request.form['score']) 
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("INSERT INTO leaderboard (name, score) VALUES (?, ?)", (name, score)) #inserting name & score in local database sqlite

    conn.commit() #save data permantely in db 
    conn.close() #closing the connection from db

    return redirect('/leaderboard')

@app.route('/leaderboard')
def leaderboard():
    conn = sqlite3.connect('database.db')
    c = conn.cursor()

    c.execute("SELECT name, score FROM leaderboard ORDER BY score DESC") 
    data = c.fetchall() #fetching all rows from database

    conn.close()

    return render_template('leaderboard.html', data=data)



if __name__ == '__main__':
    init_db()
    app.run(debug=True)