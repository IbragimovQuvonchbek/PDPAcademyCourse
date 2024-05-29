from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def family():
    family_members = ["Ibragimov Baxtiyor", "Xo'jamurodova Shozoda", "Ibragimov Bobir", "Ibragimova Iroda", "Ibragimov Quvonchbek"]
    return render_template('family.html', family_members=family_members)


if __name__ == '__main__':
    app.run(debug=True)
