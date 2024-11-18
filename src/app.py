from fastapi import FastAPI
import requests
from typing import Dict, Any
import uvicorn
from pydantic import BaseModel
import json 
import subprocess
import uuid
import os 

class SourceCode(BaseModel):
    code_content: str

app = FastAPI()

@app.post("/ally-ide/python-runtime/output")
def root(source_code: SourceCode):
	python_cmd = "python"
	script_name = f"test_file_{str(uuid.uuid4())}.py"
	with open(script_name, "w") as f:
		f.write(source_code.code_content)
	output = subprocess.run([python_cmd, script_name], capture_output=True, text=True)
	os.remove(script_name)

	return {
		"output" : output.stdout,
		"error" : output.stderr
	}