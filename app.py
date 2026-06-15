import json
from flask import Flask, render_template, request
from questions import questions
from evaluator import evaluate_answer
from results import results

app = Flask(__name__)

current_question = 0

@app.route("/")
def home():

    global current_question

    current_question = 0

    results.clear()

    return render_template("index.html")


@app.route("/interview", methods=["GET", "POST"])
def interview():

    global current_question

    score = None

    if request.method == "POST":

        answer = request.form["answer"]

        score = evaluate_answer(answer)

        results.append({
            "question": questions[current_question],
            "answer": answer,
            "score": score
        })

        current_question += 1

        if current_question >= len(questions):

            with open("results.json", "w") as file:
                json.dump(results, file, indent=4)

            return render_template(
                "completed.html",
                results=results
            )

    return render_template(
        "interview.html",
        question=questions[current_question],
        score=score
    )


if __name__ == "__main__":
    app.run(debug=True)