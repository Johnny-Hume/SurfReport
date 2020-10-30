from data.connection import get_all_data
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/all")
def all_data_page():
    file_path = "C:/SideProjectsCode/SurfReport/flaskr/data/pipeline_616_forecast.json"
    allDataList = get_all_data(file_path)
    print(type(allDataList[1]["timestamp"]))
    return render_template("home.html", all_data=allDataList)


@app.route("/index")
def index_testing():
    file_path = "C:/SideProjectsCode/SurfReport/flaskr/data/pipeline_616_forecast.json"
    allDataList = get_all_data(file_path)
    return render_template("index.html", allData=allDataList)


if __name__ == "__main__":
    app.run(debug=True)
