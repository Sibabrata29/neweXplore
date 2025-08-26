# 🧩 Encore: Streamlit + GitHub + Render

A minimal, reproducible Streamlit app ready for cloud deployment on Render.

## Local run
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Render (two ways)

### A) From this repo (Render Blueprint)
1. Push code to GitHub.
2. On Render: **New +** → **Blueprint** → connect repo → confirm.
3. Add environment variables (e.g., `API_KEY`) in **Settings → Environment**.
4. Deploy.

### B) From Web Service
1. **New +** → **Web Service** → connect GitHub repo.
2. Build: `pip install -r requirements.txt`
3. Start: `streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
4. Add env vars (e.g., `API_KEY`).

## Notes
- Pinned versions for reproducibility.
- Secrets via environment variables (never commit them).
- Ephemeral filesystem: persist data externally (DB, S3, etc).
- Health: root URL responds; use Render’s default health checks.

## Troubleshooting
- **Module not found**: ensure it’s in `requirements.txt`.
- **Port errors**: must bind to `$PORT` and `0.0.0.0`.
- **App sleeps** (free tier): cold starts are normal.
- **Large deps**: use Build Cache, trim packages, or a slimmer Python version.
