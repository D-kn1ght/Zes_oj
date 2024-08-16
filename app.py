'''
Author: Z-Es-0 141395766+Z-Es-0@users.noreply.github.com
Date: 2024-08-14 21:46:51
LastEditors: Z-Es-0 141395766+Z-Es-0@users.noreply.github.com
LastEditTime: 2024-08-16 16:40:33
FilePath: \Zes_oj\app.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import tempfile
import build
import run_code
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})





def check(s):
    for i in range(1,len(s)):
        if 2<=abs(s[i]-s[i-1])<=4:
            pass
        else:
            return False
    return True


def checkpython(data,python_code):
    with open(data, "r") as file:
        input_data = file.read()
    with open(data, "r") as file:
        values = [int(line.strip()) for line in file]

    result = run_code.execute_python_code(python_code, input_data)
    # print(result)
    lst =result.split('\n')
    g=[]
    for i in lst:
        u=i.replace('\r', '')
        g.append(list(map(int,u.split())))
    op=0
    for i in range(1,len(values)):
        k= values[i]
        # print(k)
        # print(g[op])
        if (k % 10 == 1 or k % 10 == 2 or k % 10 == 3) and len(str(k))<=1:
            if g[op][0] != -1:
                return False
        else:
            if max(g[op])==k and check(g[op]):
                pass
            else:
                return False
        op+=1
    return True

def main1(python_code):
    for i in range(1,10):
        data=f"1000/data/d{i}.in"
        if checkpython(data,python_code):
            print(f"AC to data{i}")
        else:
            return False
    return True


def checkcpp(data,cpp_code):
    return

def main2(cpp_code):
    for i in range(1,10):
        data=f"data/d{i}.in"
        if checkcpp(data,cpp_code):
            print(f"AC to data{i}")
        else:
            return False
    return True


@app.route('/api/uppercase', methods=['POST'])
def execute_code():
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"result": "Invalid request format"}), 400
    

    language = data.get('language')
    code = data.get('code')
    if language == 'Python':
        if main1(code):
            return jsonify({"result": "AC"})
        else:
            return jsonify({"result": "WA"})
    else:
        return jsonify({"result": "该功能未实现"})



@app.route('/submit_problem', methods=['POST'])
def submit_problem():
    description = request.form['description'].replace('\r\n', '\n')
    input_example = request.form['inputExample'].replace('\r\n', '\n')
    output_example = request.form['outputExample'].replace('\r\n', '\n')
    
    build.build_news(1000, description, input_example, output_example)
    return jsonify({
        "status": "success",
        "description": description,
        "input_example": input_example,
        "output_example": output_example
    })


if __name__ == '__main__':
    app.run(debug=True)
