# Grid-Coding Backend (Python Runtime)
This repository contains the backend code for Grid-Coding. The backend is written in Python using Flask and FastAPI. It uses the system runtime to execute python code and return the output to the frontend. 

## Installation
1. Make sure you have python installed on your system and the command `python` or `python3` is available in the terminal.
2. Download/clone the repository.
3. In the `src/app.py` file, change the `python_cmd` variable to the command that you use to run python on your system. For example, if you use `python3`, change the variable to `python_command = "python3"`.
3. open the terminal and navigate to the downloaded folder
```bash
cd path/to/folder
```
4. Install the required packages using the following command:
```bash
pip install -r requirements.txt
```
5. Change the directory to the src folder
```bash
cd src
```
6. Run the backend using the following command:
```bash
uvicorn --reload app:app
```
7. Note the hostname and port on which the backend is running to use it in the frontend.

## Usage
The backend provides a single endpoint to execute python code and return the output. The endpoint is `/ally-ide/python-runtime/output`. The endpoint accepts a POST request with a JSON body containing the python code to be executed. The code should be sent in the `code_content` field. The endpoint returns a JSON response containing the output of the code execution. The response contains two fields: `output` and `error`. The `output` field contains the output of the code execution, and the `error` field contains any error that occurred during the execution.

### Request Example
JSON Body:
```json
{
  "code_content": "print('Hello World')"
}
```
cURL Request:
```bash
curl '<http://<hostname>:<port>/ally-ide/python-runtime/output' \
  -H 'Content-Type: application/json' \
  --data-raw '{"code_content":"print('Hello World')"}'
```

### Response Example
```json
{
  "output": "Hello World\n",
  "error": ""	
}
```