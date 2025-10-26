from flask import Flask, render_template
import os
app = Flask(
    __name__,
    template_folder=os.path.join("..", "Web", "templates"),
    static_folder=os.path.join("..","Web", "static")
    )

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)