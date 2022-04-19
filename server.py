from flask import Flask
from flask import render_template
from flask import Response, request, jsonify
app = Flask(__name__)

# ROUTES

bsc_rul_data = {
    "1": {
        "rule_id": "1",
        "title": "Don’t Put Stuffs on the Table",
        "img": ["1.png"],
        "text": ["Keep your elbows off the table. Putting elbows on the table is considered rude.",
                 "Don’t put your bags, sun glasses, phones, and other personal belonging on the table"],
        "next_rule": "2"
    },
    "2": {
        "rule_id": "2",
        "title": "Start at the Outside and Work Your Way In",
        "img": ["2-2.png"],
        "text": [],
        "next_rule": "3"
    },
    "3": {
        "rule_id": "3",
        "title": "Put Napkin on Your Lap",
        "img": ["4.png", "5.png"],
        "text": ["Fold your napkin in half and place it on your lap. Keep it there while you’re eating",
                 "Leave the napkin on the chair if you would like leave the table for a moment"],
        "next_rule": "4"
    },
    "4": {
        "rule_id": "4",
        "title": "Wait for Everyone to be Served",
        "img": ["6.png"],
        "text": [],
        "next_rule": "5"
    },
    "5": {
        "rule_id": "5",
        "title": "When Finished, Leave Your Fork and Knife Like This!",
        "img": ["7.png"],
        "text": [],
        "next_rule": "6"
    },
    "6": {
        "rule_id": "6",
        "title": "Basic Rules Review!",
        "img": ["1.png"],
        "text": ["Don’t Put Stuffs on the Table",
                 "Start at the Outside and Work Your Way In",
                 "Put Napkin on Your Lap",
                 "Wait for Everyone to be Served",
                 "When Finished, Leave Your Fork and Knife Diagonally"],
        "next_rule": None
    }
}


table_settings = {
    "1": {
        "title": "Table Setting",
        "text": 'The golden rule, "Start at the Outside and Work Your Way In"',
        "image": "#",
        "next_lesson": "2"
    },
    "2": {
        "title": "Click on Each Item to See Its Name",
        "text": "n/a",
        "image": "/static/imgs/table_setting_1.png",
        "next_lesson": "3"
    },
    "3": {
        "title": "Table Setting Review",
        "text": "n/a",
        "image": "/static/imgs/table_setting_2.png",
        "next_lesson": "end"
    }
}

quiz_data = {
    "1": {
        "question_id": "1",
        "img": [],
        "question": "Test Your Knowledge. <br> How much do you know?",
        "choices":["5 question", "1 drag and drop"],
        "answer": None,
        "next_question": "2"
    },
    "2": {
        "question_id": "2",
        "img": ["/static/imgs/quiz1_img.png"],
        "question": "Where do you put the napkin when you leave the table for bathroom break?",
        "choices":["Bring it with you", "On the plate", "On your lap", "On the chair"],
        "answer": "On the chair",
        "next_question": "3"
    },
    "3": {
        "question_id": "3",
        "img": ["/static/imgs/quiz2_img.png"],
        "question": "What's the golden rule of the table setting?",
        "choices":["Pick any for or spoon available",  "Big utensils first, small utensils second", "Start at the outside and work your way in", "There is no rule"],
        "answer": "Start at the outside and work your way in",
        "next_question": "4"
    },
    "4": {
        "question_id": "4",
        "img": ["/static/imgs/quiz3_img.png"],
        "question": "You are served fried calamari as an appetizer, which utensil do you use?",
        "choices": ["A", "B", "C", "D","E", "None of the above"],
        "answer":  "A",
        "next_question": "5"
    },
    "5": {
        "question_id": "5",
        "img": ["/static/imgs/quiz4_img.png", ],
        "question": "You and your friends are in a restaurant having dinner torgether and your're really hungry. All of your food have been sered except the order for Abby who is seating next to you. What is the polite way to behave in this situation?",
        "choices": [ "Start eating first",  "Ask Abby if it's okay to start eating first", "Wait for Abby's dish to be served"],
        "answer": "Wait for Abby's dish to be served",
        "next_question": "6"
    },
    "6": {
        "question_id": "6",
        "img": ["/static/imgs/quiz5_img1.png", "/static/imgs/quiz5_img2.png", "/static/imgs/quiz5_img3.png"],
        "question": "Which fork is which? Choose the correct labels.",
        "choices": ["A", "B", "C"],
        "answer": "B",
        "next_question": None
    }
}

# ROUTES
@app.route('/')
def welcome():
    return render_template('home.html')


@app.route('/basic_rules/<id>')
def basic_rules(id):
    return render_template('basic_rules.html', data=bsc_rul_data[str(id)])


@app.route('/table_setting/<table_setting_id>')
def table_setting(table_setting_id):
    table_setting = table_settings[str(table_setting_id)]
    id = table_setting_id
    return render_template('table_setting.html', table_setting=table_setting, id=id)


@app.route('/quiz/<id>')
def quiz(id):
    return render_template('quiz.html', data=quiz_data[str(id)])

# AJAX FUNCTIONS


if __name__ == '__main__':
    app.run(debug=True)
