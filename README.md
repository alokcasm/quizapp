# 🧠 Quiz Application (Flask)

![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

A feature-rich, web-based Quiz Application built with Python Flask. This application supports dynamic question loading, category selection, real-time timers, and a global leaderboard.

---

## ✨ Features

- 🎯 **Category Selection:** Choose from General Knowledge, Math, or Programming.
- 🔀 **Randomized Questions:** Questions are pulled and shuffled from a JSON data source.
- ⏳ **Smart Timer:** Real-time countdown with automatic submission when time expires.
- ❌ **Negative Marking:** Includes a penalty system for incorrect answers (+1 for correct, -0.25 for wrong).
- 🏆 **Leaderboard:** Persistent ranking system powered by SQLite.
- 📖 **Review System:** Detailed post-quiz summary showing correct vs. chosen answers.
- 🎨 **Responsive UI:** Clean, modern interface designed with CSS and JavaScript.

---

## 🛠️ Tech Stack

- **Backend:** Python (Flask)
- **Frontend:** HTML5, CSS3, JavaScript (ES6)
- **Database:** SQLite (for scores and leaderboard)
- **Data Format:** JSON (for question storage)

---

## 📂 Project Structure

```text
quiz_app/
├── app.py              # Main Flask application logic
├── requirements.txt    # Project dependencies
├── database.db         # SQLite database (auto-generated)
├── data/
│   └── questions.json  # Question bank (organized by category)
├── templates/          # HTML files
│   ├── index.html      # Landing page / User info
│   ├── quiz.html       # The quiz interface
│   ├── result.html     # Score summary & review
│   └── leaderboard.html# Top scores display
└── static/             # Assets
    ├── style.css       # Custom styling
    └── script.js       # Timer and UI logic
```

---

## ⚙️ Installation & Setup

Follow these steps to get the project running locally:

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/quiz-app-flask.git
cd quiz-app-flask
```

### 2. Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv venv
# Activate on Windows:
venv\Scripts\activate
# Activate on macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the Application
```bash
python app.py
```

### 5. Access the App
Open your browser and navigate to:
`http://127.0.0.1:5000/`

---

## 📊 Scoring & Rules

| Action | Points |
| :--- | :--- |
| **Correct Answer** | +1.0 |
| **Incorrect Answer** | -0.25 |
| **Unanswered** | 0.0 |
| **Passing Grade** | 40% |

---

## 🛠️ Customization

### Adding Your Own Questions
To add or modify questions, edit the `data/questions.json` file following this format:
```json
{
  "Programming": [
    {
      "id": 1,
      "question": "What does CSS stand for?",
      "options": ["Cascading Style Sheets", "Creative Style System", "Computer Style Sheets"],
      "answer": "Cascading Style Sheets"
    }
  ]
}
```


---

**⭐ If you like this project, give it a star!**
