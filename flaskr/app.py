from data.connection import *
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/all")
def hello_world():
    file_path = "C:/SideProjectsCode/SurfReport/flaskr/data/pipeline_616_forecast.json"
    allDataList = get_all_data(file_path)
    return render_template("home.html", all_data=allDataList)


if __name__ == "__main__":
    app.run()
