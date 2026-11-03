# 🧮 Calculator

A Streamlit calculator app with result chaining and a persistent history log.

## Run it

```bash
pip install -r requirements.txt
streamlit run calculator_ui.py
```

Then open http://localhost:8501 in your browser.

## Features

- Four operations (+, −, ×, ÷) selected from a dropdown
- **Continue with result** — feeds the last answer into the next calculation
- **History** — every calculation is saved to `history.txt` and shown in the app (with a Clear history button)
- Divide-by-zero is handled with a clean error message
