'''
Author: Z-Es-0 zes18642300628@qq.com
Date: 2024-08-16 14:20:34
LastEditors: Z-Es-0 zes18642300628@qq.com
LastEditTime: 2024-09-03 19:34:57
FilePath: \Zes_oj\run_code.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

import subprocess
import tempfile
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
    

def execute_cpp_code(code_str, input_data):
    return
    

def execute_java_code(code_str, input_data):
    return
    