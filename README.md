# 🗳️ BharatVote Guide

> An interactive, bilingual (English + Hindi) web application that educates Indian citizens about the complete election process — from voter registration to government formation.

**Powered by Google Gemini AI · Deployed on Google Cloud Run**

---

## ✨ Features

| Feature | Description |
|---|---|
| **📅 Interactive Timeline** | 6-phase election process from announcement to results |
| **🧭 Step-by-Step Wizard** | Walk through registration → nomination → campaign → voting → counting → results |
| **📝 Knowledge Quiz** | 10-question bilingual quiz with scoring and explanations |
| **❓ FAQ Section** | 8+ common questions with clear answers |
| **🗺️ State Info Selector** | Election data for 28 states + 8 UTs |
| **🤖 AI Assistant** | Google Gemini–powered Q&A for personalised guidance |
| **🌐 Bilingual** | Full English ↔ Hindi toggle |
| **🎨 Premium UI** | Dark theme with gradient accents, Inter font, and responsive design |
| **♿ Accessible** | ARIA labels, keyboard navigation, skip-to-content, high contrast |

---

## 🏗️ Architecture

```
Vote-Path-/
├── app.py                    # Main Streamlit entry point
├── Dockerfile                # Cloud Run–ready container
├── requirements.txt          # Python dependencies
├── .env.example              # Environment variable template
├── .streamlit/
│   └── config.toml           # Streamlit theme & server config
├── src/
│   ├── config.py             # App configuration (env-based)
│   ├── gemini_client.py      # Gemini API client (rate-limited, sanitised)
│   ├── components/
│   │   ├── home.py           # Landing page with hero & feature cards
│   │   ├── timeline.py       # Interactive election timeline
│   │   ├── wizard.py         # Step-by-step election guide
│   │   ├── quiz.py           # Interactive quiz with scoring
│   │   ├── faq.py            # FAQ accordion
│   │   ├── states.py         # State information selector
│   │   ├── ai_chat.py        # Gemini AI chat interface
│   │   └── sidebar.py        # Navigation & language toggle
│   ├── data/
│   │   ├── election_data.py  # Timeline & wizard content (EN/HI)
│   │   ├── quiz_data.py      # 10 quiz questions per language
│   │   ├── faq_data.py       # FAQ entries (EN/HI)
│   │   └── state_data.py     # State election statistics
│   └── utils/
│       ├── i18n.py           # Translation system (140+ strings)
│       ├── rate_limiter.py   # Sliding-window rate limiter
│       └── sanitizer.py      # Input sanitisation (XSS prevention)
└── tests/
    ├── test_sanitizer.py     # Sanitizer unit tests
    ├── test_rate_limiter.py   # Rate limiter unit tests
    ├── test_i18n.py          # Translation tests
    ├── test_data.py          # Data integrity tests
    └── test_gemini_client.py  # Gemini client tests (mocked)
```

---

## 🚀 Quick Start (Local Development)

### 1. Clone & install

```bash
git clone https://github.com/your-repo/Vote-Path-.git
cd Vote-Path-
pip install -r requirements.txt
```

### 2. Set your Gemini API key

```bash
cp .env.example .env
# Edit .env and add your key from https://aistudio.google.com/apikey
```

### 3. Run the app

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501)

---

## 🧪 Running Tests

```bash
pytest tests/ -v --tb=short
```

With coverage:

```bash
pytest tests/ -v --cov=src --cov-report=term-missing
```

---

## ☁️ Deploy to Google Cloud Run

### Prerequisites

- [Google Cloud CLI](https://cloud.google.com/sdk) installed & authenticated
- A GCP project with billing enabled
- Gemini API key from [AI Studio](https://aistudio.google.com/apikey)

### Step 1 — Set your project

```bash
gcloud config set project YOUR_PROJECT_ID
```

### Step 2 — Enable required APIs

```bash
gcloud services enable \
  run.googleapis.com \
  cloudbuild.googleapis.com \
  artifactregistry.googleapis.com
```

### Step 3 — Deploy

```bash
gcloud run deploy bharatvote-guide \
  --source . \
  --region asia-south1 \
  --allow-unauthenticated \
  --set-env-vars "GEMINI_API_KEY=your-api-key-here" \
  --memory 512Mi \
  --cpu 1 \
  --min-instances 0 \
  --max-instances 3 \
  --timeout 300 \
  --port 8080
```

### Step 4 — Access your app

The CLI will output a URL like:
```
https://bharatvote-guide-xxxxx-el.a.run.app
```

---

## 🔒 Security

- **No secrets in code** — API key loaded from environment variables only
- **Input sanitisation** — All user inputs are sanitised via `bleach` (HTML stripping, truncation)
- **Rate limiting** — Sliding-window limiter prevents API abuse (10 calls/60s)
- **XSRF protection** — Enabled in Streamlit config
- **Safety filters** — Gemini safety settings block harmful content

---

## ♿ Accessibility

- Skip-to-content link for keyboard users
- ARIA `role`, `aria-label`, `aria-selected` attributes throughout
- High-contrast colour palette (WCAG AA compliant)
- Focus-visible outlines on all interactive elements
- Semantic HTML structure
- Screen-reader–friendly navigation

---

## 📄 License

MIT © 2026 BharatVote Guide
