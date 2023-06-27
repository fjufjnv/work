from flask import Flask, render_template
import viewdata.tools as tool
from flask import jsonify, json
from flask_cors import CORS

app = Flask(__name__, static_folder='', static_url_path='')
CORS(app, resources='/*')
app.config['JSON_AS_ASCII'] = False
app.config['JSONIFY_PRETTYPRNT_REGULAR'] = False
app.config['JSON_SORT_KEYS'] = False

@app.route("/")
def index():
    return render_template("bigdata.html")

@app.route("/bigdata/toplist")
def task():
    data = tool.bigdata_toplist()
    return jsonify({"data": data})

@app.route("/bigdata/company")
def task2():
    data = tool.bigdata_company()
    return jsonify(data)

@app.route("/bigdata/chart3")
def task3():
    data = tool.bigdata_chart3()
    return jsonify(data)

@app.route("/bigdata/sales_rank")
def task4():
    data = tool.bigdata_sales_rank()
    return jsonify(data)

@app.route("/bigdata/chart2")
def task5():
    data = tool.bigdata_chart2_data()
    y_data = data[0]
    x_data = data[1]
    return jsonify({"ydata": y_data, "xdata": x_data})

@app.route("/bigdata/ceshi5")
def task6():
    data = tool.bigdata_ceshi5_data()
    return jsonify({"data1": data[0], "data2": data[1], "data3": data[2], "data4": data[3], "data5": data[4], "data6": data[5]})

@app.route("/bigdata/chart4")
def task7():
    data = tool.bigdata_chart4_data()
    return jsonify({"monthvalue": data[0], "ordervalue": data[1], "pays": data[2], "avgs": data[3]})

@app.route("/bigdata/chart5")
def task8():
    data = tool.bigdata_chart5_data()
    return jsonify({"CountryName": data[0], "CountryValue": data[1]})

@app.route("/js/data-1482909892121-BJ3auk-Se.json", methods=['GET'])
def survey_json_get():
    with open(r"C:\Users\R-shuo\Desktop\全国物流大数据分析\Viewdata-master\statics\js\data-se.json", encoding='utf-8') as f:
        jsonStr = json.load(f)
        return json.dumps(jsonStr)



if __name__ == '__main__':
    app.debug = True
    app.run()