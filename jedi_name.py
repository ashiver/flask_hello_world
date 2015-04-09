from flask import Flask, render_template
app = Flask(__name__)


@app.route("/jedi/<first>/<last>")
def jedi(first,last):
    jedi_name = last[0:3] + first[0:2]
    return render_template('template.html', first = first.title(), jedi_name = jedi_name.title())


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)