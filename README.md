# 🧠 Quiz Application (Flask Project)

A web-based Quiz Application built using Python Flask with features like random questions, timer, negative marking, category-based quiz, and leaderboard system.

---

## 🚀 Features

- 🎯 Random question selection from JSON
- ⏳ Timer-based quiz system (auto submit)
- ❌ Negative marking system
- 📊 Score calculation with percentage
- ✅ Pass/Fail system
- 📖 Answer review after quiz
- 🧑 Username-based quiz attempt
- 📚 Category-based quiz (GK, Math, Programming)
- 🏆 Leaderboard using SQLite database

---

## 🛠️ Tech Stack

- Python (Flask)
- HTML, CSS, JavaScript
- SQLite (Database)
- JSON (Question storage)

---

## 📁 Project Structure
quiz_app/
│
├── app.py
├── requirements.txt
├── database.db
│
├── data/
│ └── questions.json
│
├── templates/
│ ├── index.html
│ ├── quiz.html
│ ├── result.html
│ ├── leaderboard.html
│
├── static/
│ ├── style.css
│ ├── script.js


---

## ⚙️ Installation & Setup

1. Clone the repository:
--bash
git clone 
cd quiz_app

--Install dependencies:
pip install -r requirements.txt

--Run the application:
python app.py

--Open browser:
http://127.0.0.1:5000/


🧠 How It Works
1. User enters name and selects category
2. Questions are filtered and randomized
3. Timer starts automatically
4. User submits answers (or auto submit)
5. Score is calculated with negative marking
6. Result + answer review displayed
7. Score stored in leaderboard database


📊 Scoring System
✔ Correct Answer: +1
❌ Wrong Answer: -0.25
📈 Percentage calculated
🎯 Pass if ≥ 40%

