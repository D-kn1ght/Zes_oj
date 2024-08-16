function updateText() {
    var lang = document.getElementById("languageSelect").value;
    var codeText = document.getElementById("codeText");

    if (lang === "C++") {
        codeText.value = '#include<iostream>\nint main() {\n    std::cout << "Hello, World!";\n    return 0;\n}';
    } else if (lang === "Python") {
        codeText.value = 'print("Hello, World!")';
    } else if (lang === "Java") {
        codeText.value = 'public class Main {\n    public static void main(String[] args) {\n        System.out.println("Hello, World!");\n    }\n}';
    }
}



async function displayResult(event) {
 

    const selectedLanguage = document.getElementById("languageSelect").value;
    const codeContent = document.getElementById("codeText").value;

    try {
        const response = await fetch('http://localhost:5000/api/uppercase', {  
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ language: selectedLanguage, code: codeContent })
        });

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        const result = data.result;
        const resultElement = document.getElementById("result");
        resultElement.textContent = result;

        if (result === "AC") {
            resultElement.style.color = 'green';
        } else if (result === "WA") {
            resultElement.style.color = 'red';
        } else {
            resultElement.style.color = 'black';
        }
    } catch (error) {
        console.error('Error:', error);
        const resultElement = document.getElementById("result");
        resultElement.textContent = "Error";
        resultElement.style.color = 'black';
    }
}
