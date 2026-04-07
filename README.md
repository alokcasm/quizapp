🧠 Quiz Application (Flask Project)
An interactive Quiz Web Application built using Python Flask.  
It supports category-based quizzes, timer system, negative marking, answer review, and leaderboard tracking using SQLite.
---
🚀 Features
🎯 Random question selection from JSON file
📚 Category-based quiz (GK, Math, Programming)
⏳ Timer-based quiz with auto submit
❌ Negative marking system
📊 Score calculation with percentage
✅ Pass/Fail evaluation
📖 Answer review after submission
🧑 Username-based quiz attempt
🏆 Leaderboard using SQLite database
---
🛠️ Tech Stack
Backend: Python (Flask)
Frontend: HTML, CSS, JavaScript
Database: SQLite
Data Storage: JSON
---
📁 Project Structure
quiz_app/
│
├── app.py
├── requirements.txt
├── database.db
│
├── data/
│   └── questions.json
│
├── templates/
│   ├── index.html
│   ├── quiz.html
│   ├── result.html
│   ├── leaderboard.html
│
├── static/
│   ├── style.css
│   ├── script.js
---
⚙️ Installation & Setup
Clone the repository:
git clone https://github.com/your-username/quiz-app.git
cd quiz-app
Install dependencies:
pip install -r requirements.txt
Run the application:
python app.py
Open in browser:
http://127.0.0.1:5000/
---
🧠 How It Works
User enters name and selects category
Questions are filtered and randomized
Timer starts automatically
User submits answers (or auto submit)
Score is calculated with negative marking
Result with percentage and status is shown
Answer review is displayed
Score is stored in leaderboard
---
📊 Scoring System
✔ Correct Answer: +1
❌ Wrong Answer: -0.25
📈 Percentage = (score / total questions) × 100
🎯 Pass if ≥ 40%
---
⭐ Give a star if you like this project!
