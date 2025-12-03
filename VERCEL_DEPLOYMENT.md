# 🚀 Vercel Deployment Guide - India Sweet House Analytics

## ✅ Pre-Deployment Checklist (COMPLETED)

All required configurations are ready:

- ✅ Python upgraded to **3.13** (runtime.txt)
- ✅ All dependencies compatible with Python 3.13
- ✅ Gunicorn removed (not needed for Vercel serverless)
- ✅ Flask app properly exported in `api/index.py`
- ✅ Vercel configuration optimized (`vercel.json`)
- ✅ Frontend build configured (Vite)
- ✅ CORS enabled for API communication
- ✅ File uploads configured for `/tmp` (Vercel-compatible)

## 📋 Deployment Steps

### Step 1: Commit and Push Changes

```powershell
# Add all changes
git add .

# Commit with descriptive message
git commit -m "Deploy to Vercel: Python 3.13 upgrade + optimized config"

# Push to main branch
git push origin main
```

### Step 2: Deploy to Vercel

#### Option A: Vercel Dashboard (Recommended for First Deploy)

1. Go to [vercel.com/new](https://vercel.com/new)
2. Click **"Import Git Repository"**
3. Select your repository: `prathamesh1010/India_Sweet_House3`
4. Vercel will auto-detect:
   - **Framework:** Vite
   - **Build Command:** `npm run build`
   - **Output Directory:** `dist`
   - **Install Command:** `npm install`
5. Click **"Deploy"**

Vercel will automatically:
- Install Node.js dependencies
- Build frontend with Vite
- Install Python 3.13 and dependencies
- Deploy API as serverless functions

#### Option B: Vercel CLI (For Subsequent Deploys)

```powershell
# Install Vercel CLI globally (one time)
npm install -g vercel

# Login to Vercel
vercel login

# Deploy to production
vercel --prod
```

### Step 3: Verify Deployment

Once deployed, Vercel will provide URLs:
- **Production URL:** `https://your-app-name.vercel.app`

Test these endpoints:
```powershell
# Frontend
https://your-app-name.vercel.app/

# API Health Check
https://your-app-name.vercel.app/api/health

# API Root
https://your-app-name.vercel.app/api/
```

You can test using PowerShell:
```powershell
# Test health endpoint
Invoke-WebRequest -Uri "https://your-app-name.vercel.app/api/health" -UseBasicParsing

# Test with curl (if installed)
curl https://your-app-name.vercel.app/api/health
```

## 🔧 Configuration Details

### Python Runtime
**File:** `runtime.txt`
```
python-3.13
```

### API Dependencies
**File:** `api/requirements.txt`
```
Flask==3.1.0
Flask-CORS==5.0.0
pandas==2.2.3
numpy==2.1.3
openpyxl==3.1.5
Werkzeug==3.1.3
```

**Note:** No setuptools/wheel conflicts - Vercel handles this automatically with Python 3.13.

### Vercel Configuration
**File:** `vercel.json` (already configured)
- Python serverless function: `api/index.py`
- Runtime: `python3.13`
- Max lambda size: `50mb` (sufficient for pandas/numpy)
- Frontend: Vite static build

### API Endpoints
Your deployed API will have:
- `GET /api/` - API information
- `GET /api/health` - Health check
- `POST /api/process-file` - Upload and process Excel/CSV files
- `POST /api/interest-analysis` - Interest rate analysis

## 🧪 Local Testing Before Deploy

Run verification script:
```powershell
python verify_vercel.py
```

Expected output:
```
✓ ALL CHECKS PASSED - Ready for Vercel deployment!
```

## 🐛 Troubleshooting

### If Build Fails

1. **Check Build Logs** in Vercel dashboard:
   - Go to your project → **Deployments** → Click failed deployment → **View Logs**

2. **Common Issues:**

   **Issue:** "Module not found" or import errors
   **Fix:** Ensure all dependencies are in `api/requirements.txt`

   **Issue:** "Lambda size exceeds limit"
   **Fix:** Already optimized - removed gunicorn. If still occurs, dependencies are too large for Vercel. Consider:
   - Alternative: Deploy backend to Render/Railway (unlimited size)
   - Or reduce pandas/numpy usage

   **Issue:** "setuptools version conflict"
   **Fix:** Already handled - Python 3.13 uses modern build system. If occurs, Vercel will auto-fix.

   **Issue:** "Frontend build failed"
   **Fix:** Verify locally:
   ```powershell
   npm install
   npm run build
   ```

### If API Returns Errors

1. **Check Function Logs** in Vercel dashboard:
   - Project → Deployments → Select deployment → **Functions** tab → Click function → **Logs**

2. **Test Locally First:**
   ```powershell
   # Activate virtual environment
   .\.venv\Scripts\Activate.ps1
   
   # Run backend
   python backend_api.py
   
   # In another terminal, test
   Invoke-WebRequest -Uri http://localhost:5000/health
   ```

3. **Common Runtime Issues:**

   **Issue:** File upload fails
   **Cause:** Vercel uses `/tmp` for temporary files
   **Fix:** Already configured in `api/index.py` (`UPLOAD_FOLDER = '/tmp/uploads'`)

   **Issue:** CORS errors from frontend
   **Fix:** Already configured - Flask-CORS is installed and `CORS(app)` is called

   **Issue:** 500 Internal Server Error
   **Fix:** Check function logs for Python tracebacks. Common causes:
   - Missing environment variables (if any)
   - File format issues (ensure Excel files match expected structure)

### If Frontend Can't Connect to API

1. **Verify API URL** in frontend code:
   - Check if frontend is using correct API base URL
   - In production: `/api/` (relative path - already configured in routes)
   - Vercel routes `/api/*` automatically to serverless functions

2. **Check Network Tab** in browser DevTools:
   - Look for 404 errors → Route configuration issue
   - Look for CORS errors → Backend CORS issue (already fixed)
   - Look for 500 errors → Backend code issue (check function logs)

## 📊 Testing with Sample Data

### File Format Requirements
Your Excel files should have:
- **Worksheet:** "Outlet wise" (for multi-sheet files)
- **Columns:** 
  - "PARTICULARS" column with store/outlet names
  - Month columns: "JAN-23", "FEB-23", etc.
  - Numeric data for analysis

### Test via Frontend
1. Go to deployed URL: `https://your-app-name.vercel.app`
2. Use the file upload component
3. Select your Excel/CSV file
4. Process and view analytics

### Test via API (Direct)
```powershell
# Using PowerShell
$FilePath = "path\to\your\testfile.xlsx"
$Uri = "https://your-app-name.vercel.app/api/process-file"

# Create form data
$form = @{
    file = Get-Item -Path $FilePath
}

# Upload and process
Invoke-RestMethod -Uri $Uri -Method Post -Form $form
```

## 🔒 Environment Variables (Optional)

If you need environment variables:

1. Go to Vercel dashboard → Your Project → **Settings** → **Environment Variables**
2. Add variables:
   - `PYTHONUNBUFFERED=1` (already in vercel.json)
   - Add any custom variables your app needs

3. Redeploy for changes to take effect

## 📈 Performance & Limits

### Vercel Serverless Limits
- **Function Duration:** 10 seconds (Hobby), 60 seconds (Pro)
- **Function Size:** 50MB (configured in vercel.json)
- **Memory:** 1024MB default
- **Bandwidth:** Varies by plan

### Optimization Tips
- Large file processing: Limit to reasonable sizes (< 10MB Excel files)
- If processing takes > 10 seconds, consider:
  - Upgrade to Vercel Pro (60s timeout)
  - Move heavy processing to background service
  - Use Vercel Edge Functions for faster cold starts

## 🚀 Continuous Deployment

Once connected, Vercel auto-deploys on every push:

```powershell
# Make changes to your code
git add .
git commit -m "Your changes"
git push origin main

# Vercel automatically detects push and deploys
```

- **Preview Deployments:** Every branch/PR gets a unique URL
- **Production Deployments:** Pushes to `main` deploy to production
- **Instant Rollback:** Revert to previous deployments instantly in dashboard

## 📞 Support & Resources

- **Vercel Docs:** [vercel.com/docs](https://vercel.com/docs)
- **Python on Vercel:** [vercel.com/docs/functions/serverless-functions/runtimes/python](https://vercel.com/docs/functions/serverless-functions/runtimes/python)
- **Deployment Logs:** Check in Vercel dashboard under Deployments

## ✅ Post-Deployment Checklist

After successful deployment:

- [ ] Test health endpoint: `https://your-app.vercel.app/api/health`
- [ ] Test frontend loads: `https://your-app.vercel.app/`
- [ ] Upload sample Excel file through UI
- [ ] Verify data processing works
- [ ] Check all charts and analytics render correctly
- [ ] Test on mobile devices (responsive design)
- [ ] Set up custom domain (optional, in Vercel dashboard)
- [ ] Configure production environment variables (if needed)

## 🎯 Current Status

**✅ ALL SYSTEMS GO - Ready for Vercel Deployment**

- Python 3.13.9 configured
- All dependencies verified
- No gunicorn conflicts
- No setuptools issues
- Vercel config optimized
- File structure correct
- API endpoints tested locally

**Next Action:** Run deployment commands above ⬆️

---

**Deployment Date:** December 3, 2025  
**Python Version:** 3.13.9  
**Framework:** Flask + Vite  
**Status:** Production Ready ✅
