from flask import Flask, render_template, abort, jsonify, request, redirect, url_for
from db_helper import db, save_db
import json

app = Flask(__name__)
 
@app.route('/')
def home():
	return render_template("home.html", cards=db)

@app.route('/set_<int:num>', methods=['GET','POST'])
def set_view(num):
	set=db[num]
	if request.method == "POST":
		card = {"question":request.form['question'],
				"answer":request.form['answer']}
		db[num]["content"].append(card)
		save_db()
		return redirect(url_for('set_view', num=num))
	else:
		return render_template("set.html", set=set, num=num)

@app.route('/set_<int:num>/remove_term', methods=['GET','POST'])
def term_remove(num):
	set=db[num]
	try:
		if request.method == "POST":
			question=int(request.form['question'])
			del db[num]["content"][question]
			return render_template('remove_term.html', set=set, num=num)
		else:
			return render_template("remove_term.html", set=set, num=num)
	except IndexError:
		abort(404)

@app.route('/create_new_cards', methods=['GET', 'POST'])
def newFlashcards():
	return render_template("newCard.html")

@app.route('/api/card/<int:index>')
def api_card_detail(index):
	try:
		return db[index]
	except IndexError:
		abort(404)

if __name__ == "__main__":
    app.run(debug=True)