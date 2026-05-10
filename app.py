## Setup

### 1. Clone

```bash
git clone https://github.com/ARCHanavedUlla/forest-fire-prediction.git
cd forest-fire-prediction
```


### 2. Install dependencies

```bash
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Download FIRMS data (optional — sample included)

```bash
# Get a free API key from https://firms.modaps.eosdis.nasa.gov/api/
export FIRMS_API_KEY=your_key_here
python data/fetch_firms_data.py
```
