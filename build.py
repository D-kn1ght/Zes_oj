'''
Author: Z-Es-0 141395766+Z-Es-0@users.noreply.github.com
Date: 2024-08-16 14:07:03
LastEditors: Z-Es-0 141395766+Z-Es-0@users.noreply.github.com
LastEditTime: 2024-08-16 16:39:24
FilePath: \Zes_oj\ce.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import os
import shutil



def build_news(insert, data0, data1, data2):
    folder_path = f'{insert + 1}'
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"文件夹'{folder_path}'创建成功！")
    else:
        print(f"文件夹'{folder_path}'已存在。")
        return 'error'

    file_path = os.path.join(folder_path, f'question{folder_path}.html')
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(f'''
<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8" />
    <title>zes_oj</title>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <style>
        body {{
            font-family: Arial, sans-serif;
            text-align: left;
            margin: 10px;
        }}
        .button-container {{
            display: flex;
            justify-content: flex-start;
            gap: 20px;
        }}
        .visible-button {{
            background-color: #ffffff;
            border: none;
            color: rgb(0, 0, 0);
            padding: 10px 20px;
            text-decoration: none;
            font-size: 16px;
            cursor: pointer;
            border-radius: 5px;
        }}
        .visible-button:hover {{
            background-color: #c8d6e2;
        }}
    </style>
</head>
<body>
    <div class="button-container">
        <a href="index.HTML" class="visible-button">主页</a>
        <a href="make_question.html" class="visible-button">题目管理</a>
        <a href="README.md" class="visible-button">关于</a>
    </div>
    <h1>题目描述</h1>
    <p>{data0}</p>
    <hr>
    <h1>输入样例</h1>
    <p>
        <textarea id="myText" rows="10" cols="50">{data1}</textarea>
        <button onclick="copyText()">复制文本</button>
        <script src="script.js"></script>
    </p>
    <h1>输出样例</h1>
    <hr>
    <p>
        <textarea id="myText" rows="10" cols="50">
{data2}
        </textarea>
    </p>
    <h1>提示</h1>
    <h1>答案提交</h1>
    <div>
        <select id="languageSelect" onchange="updateText()">
            <option value="C++">C++</option>
            <option value="Python">Python</option>
            <option value="Java">Java</option>
        </select>
        <br><br>
        <textarea id="codeText" rows="30" cols="100">#include<iostream>
int main() {{
std::cout << "Hello, World!";
return 0;
}}</textarea>
        <br>
        <button onclick="displayResult()">提交</button>
        <p id="result"></p>
    </div>
    <script src="solve.js"></script>
</body>
</html>''')
        print(f"ok for '{file_path}'。")
        source_path = 'script.js'
        destination_path = f'{insert+1}/script.js'
        try:
            shutil.copy(source_path, destination_path)
            print("ac")
        except IOError as e:
            print(f"we can not ot{e}")
        except Exception as e:
            print(f"no {e}")

        source_path = 'solve.js'
        destination_path = f'{insert+1}/solve.js'
        try:
            shutil.copy(source_path, destination_path)
            print("ac")
        except IOError as e:
            print(f"we can not build {e}")
        except Exception as e:
            print(f"no! {e}")
        


if __name__ == '__main__':
    build_news(1001, '问题是a+b', "1 1\n1 2", '2\n3')
