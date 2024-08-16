from flask import Flask, request, jsonify
from flask_cors import CORS
import subprocess
import tempfile
app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})




def execute_python_code(code_str, input_data):
    with tempfile.NamedTemporaryFile(suffix=".py", mode="w", delete=False) as temp_code_file:
        temp_code_file.write(code_str)
        code_file_name = temp_code_file.name
    with tempfile.NamedTemporaryFile(suffix=".in", mode="w", delete=False) as temp_input_file:
        temp_input_file.write(input_data)
        input_file_name = temp_input_file.name
    try:
        result = subprocess.run(
            ["python", code_file_name],
            stdin=open(input_file_name, "r"),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE
        )
        output = result.stdout.decode('utf-8')
        error = result.stderr.decode('utf-8')
    finally:
        import os
        os.remove(code_file_name)
        os.remove(input_file_name)

    if error:
        return f"Error: {error}"
    else:
        return output


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

    result = execute_python_code(python_code, input_data)
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

def main(python_code):
    for i in range(1,10):
        data=f"data/d{i}.in"
        if checkpython(data,python_code):
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
        if main(code):
            return jsonify({"result": "AC"})
        else:
            return jsonify({"result": "WA"})
    else:
        return jsonify({"result": "该功能未实现"})

if __name__ == '__main__':
    app.run(debug=True)
