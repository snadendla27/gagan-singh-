xfrom flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

excuses = {
    "school": {
        "homework": [f"Lost my notes in a tornado {i}" for i in range(1, 26)],
        "class attendance": [f"My dog ate my schedule {i}" for i in range(1, 26)],
        "cheating": [f"I was helping my twin, not cheating {i}" for i in range(1, 26)]
    },
    "work": {
        "attendance issues": [f"Traffic was literally an episode of Survivor {i}" for i in range(1, 26)],
        "missed deadlines": [f"My laptop caught on fire (figuratively, but still...) {i}" for i in range(1, 26)],
        "quitting job": [f"I'm leaving to follow my dream of professional napping {i}" for i in range(1, 26)]
    },
    "relationships": {
        "avoidance": [f"My WiFi only works when I don't reply {i}" for i in range(1, 26)],
        "breakup": [f"It's not you, it's me—just kidding, it's you {i}" for i in range(1, 26)],
        "reasons to break no contact": [f"Oops, my fingers slipped and I texted {i}" for i in range(1, 26)]
    },
    "legal trouble": {  
        "minor crimes": [f"I thought it was a free sample {i}" for i in range(1, 26)],
        "serious crimes": [f"It wasn’t me, it was my evil twin {i}" for i in range(1, 26)],
        "general excuses": [f"Aliens abducted me and erased my memory {i}" for i in range(1, 26)]
    },
    "friends": {
        "trust issues": [f"My therapist said to set boundaries {i}" for i in range(1, 26)],
        "ex drama": [f"Oops, my ex just tripped into my DMs {i}" for i in range(1, 26)],
        "unreliable friend behavior": [f"My phone was on 'Do Not Disturb'... forever {i}" for i in range(1, 26)]
    }
}

@app.route('/')
def home():
    return render_template('index.html', categories=excuses.keys())

@app.route('/subcategory', methods=['POST'])
def subcategory():
    category = request.form.get("category")
    subcategories = excuses.get(category, {})
    return render_template('subcategory.html', category=category, subcategories=subcategories)

@app.route('/generate_excuse', methods=['POST'])
def generate_excuse():
    category = request.form.get("category")
    subcategory = request.form.get("subcategory")
    
    if category in excuses and subcategory in excuses[category]:
        excuse_list = random.sample(excuses[category][subcategory], 5)
        return render_template('excuses.html', category=category, subcategory=subcategory, excuse_list=excuse_list)
    
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
