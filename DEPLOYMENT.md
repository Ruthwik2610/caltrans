# Caltrans AI Application - Streamlit Cloud Deployment Guide

## Prerequisites

1. **GitHub Account** - Push your code to a GitHub repository
2. **Streamlit Cloud Account** - Sign up at [share.streamlit.io](https://share.streamlit.io)
3. **API Keys** - Have your API keys ready:
   - `OPENAI_API_KEY`
   - `GROQ_API_KEY`
   - `HF_TOKEN` (if using Hugging Face)
   - `ANTHROPIC_API_KEY` (if using Claude)
   - `CALTRANS_PERSONAL_NARRATIVE_INSIGHTS_ASSISTANT_ID`

## Step 1: Push to GitHub

```bash
# Initialize git (if not already)
git init

# Add all files (respecting .gitignore)
git add .

# Commit
git commit -m "Initial commit for Streamlit Cloud deployment"

# Add remote and push
git remote add origin https://github.com/YOUR_USERNAME/YOUR_REPO.git
git branch -M main
git push -u origin main
```

## Step 2: Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Click **"New app"**
3. Select your GitHub repository
4. Set the following:
   - **Repository**: `YOUR_USERNAME/YOUR_REPO`
   - **Branch**: `main`
   - **Main file path**: `app.py`
5. Click **"Advanced settings"**

## Step 3: Configure Secrets

In the "Advanced settings" → **Secrets** section, add:

```toml
OPENAI_API_KEY = "sk-your-openai-api-key"
GROQ_API_KEY = "gsk_your-groq-api-key"
HF_TOKEN = "hf_your-huggingface-token"
ANTHROPIC_API_KEY = "sk-ant-your-anthropic-key"
CALTRANS_PERSONAL_NARRATIVE_INSIGHTS_ASSISTANT_ID = "asst_your-assistant-id"
```

> **Note**: Copy values from your local `.env` file (do NOT commit `.env` to GitHub!)

## Step 4: Deploy

Click **"Deploy!"** and wait for the app to build (first build takes 3-5 minutes).

## Troubleshooting

### Build fails with missing packages
- Check `requirements.txt` includes all dependencies
- Remove version pinning for problematic packages

### App crashes on startup
- Check Streamlit Cloud logs for errors
- Verify all secrets are configured correctly

### API errors
- Verify API keys are valid and have sufficient credits
- Check that secrets are spelled exactly as expected

## Files Required for Deployment

- `app.py` - Main application file
- `requirements.txt` - Python dependencies
- `.streamlit/config.toml` - Streamlit configuration
- `src/` - Source code directory
- `style/` - CSS styles
- `image/` - Image assets

## Files NOT to Commit

These are excluded via `.gitignore`:
- `.env` - Local environment variables
- `.streamlit/secrets.toml` - Local secrets
- `venv/` or `.venv/` - Virtual environments
- `__pycache__/` - Python cache
