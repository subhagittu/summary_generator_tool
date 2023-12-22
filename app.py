from flask import Flask, render_template, request
from text_summary import summarizer

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('main.html')

@app.route('/analyze', methods=['GET', 'POST'])
def analyze():
    if request.method == 'POST':
        rawtext = request.form['rawtext']
        summary, original_text, len_orig_text, len_summary = summarizer(rawtext)

        return render_template('generating_summary.html', summary=summary, original_text=original_text, len_orig_text=len_orig_text ,len_summary=len_summary)

if __name__ == "__main__":
    app.run(debug=True)
