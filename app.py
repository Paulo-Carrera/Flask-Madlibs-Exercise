from flask import Flask, request, render_template, redirect , url_for
from stories import Story

app = Flask(__name__)

@app.route('/')
def story_form():
    return render_template('story_form.html')

@app.route('/story', methods=['POST','GET'])
def show_story():
    if request.method == 'POST':
        # data from form submission
        place = request.form["place"]
        noun = request.form["noun"]
        verb = request.form["verb"]
        adjective = request.form["adjective"]
        plural_noun = request.form["plural_noun"]

        # create a story instance
        story = Story(
            ["place", "noun", "verb", "adjective", "plural_noun"],
            """Once upon a time in a long-ago {place}, there lived a
               large {adjective} {noun}. It loved to {verb} {plural_noun}."""
        )

        # generate the story using user input
        story_result = story.generate({
            "place": place,
            "noun": noun,
            "verb": verb,
            "adjective": adjective,
            "plural_noun": plural_noun
        })

        # render the story on the story.html template
        return render_template('story.html', story=story_result)
    elif request.method == 'GET' :
        return redirect(url_for('story_form'))

if __name__ == '__main__':
    app.run(debug=True)
