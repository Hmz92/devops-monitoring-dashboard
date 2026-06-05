import subprocess
import sys
import os
import time

# Default ports
api_port = os.environ.get("PORT", "8000")
dashboard_port = "8501"

# Set API Key default if not set
if "API_KEY" not in os.environ:
    os.environ["API_KEY"] = "demo-key"

# Start the FastAPI API in the background
print(f"Starting FastAPI API on port {api_port}...")
api_process = subprocess.Popen([
    sys.executable, "-m", "uvicorn", "api.main:app",
    "--host", "0.0.0.0",
    "--port", api_port
])

# Give FastAPI a moment to spin up
time.sleep(1.5)

# Start Streamlit
print(f"Starting Streamlit Dashboard on port {dashboard_port}...")
try:
    subprocess.run([
        "streamlit", "run", "dashboard/app.py",
        "--server.port", dashboard_port,
        "--server.address", "0.0.0.0"
    ], check=True)
finally:
    print("Terminating FastAPI API...")
    api_process.terminate()
    api_process.wait()
