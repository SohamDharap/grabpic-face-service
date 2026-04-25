# GrabPic Face Service

## Setup (WSL/Linux recommended)

1. Create venv
python3 -m venv venv

2. Activate
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Run server
uvicorn app.main:app --host 0.0.0.0 --port 8001 --reload

## API

POST /embed
- Input: image file
- Output: 512-d embedding

GET /health
