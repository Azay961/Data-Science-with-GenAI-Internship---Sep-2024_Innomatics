from flask import Flask, request, render_template
import re

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    test_string = None
    regex = None
    if request.method == "POST":
        regex = request.form.get("regex")
        test_string = request.form.get("test_string")
        regex_pattern = re.compile(regex)
        matches = re.findall(regex_pattern, test_string)
        def highlight_match(match):
            return f'<span class="highlight">{match.group(0)}</span>'

        
        result = re.sub(regex_pattern, highlight_match, test_string)
        return render_template("index.html", regex=regex, test_string=test_string, matches=matches, highlighted=result)

    return render_template("index.html", regex=" ", test_string="")

if __name__ == "__main__":
    app.run(debug=True, port=5001)