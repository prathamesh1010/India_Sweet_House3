# Python 3.13 Upgrade and Vercel Deployment Guide

## ✅ Completed Upgrades

### 1. Python Version Upgrade
- **Upgraded from:** Python 3.12
- **Upgraded to:** Python 3.13.9 (Latest Stable)
- **Status:** ✅ Successfully tested and verified

### 2. Updated Dependencies
All packages upgraded to latest compatible versions with Python 3.13:

| Package | Version | Status |
|---------|---------|--------|
| Flask | 3.1.0 | ✅ Tested |
| Flask-CORS | 5.0.0 | ✅ Tested |
| pandas | 2.2.3 | ✅ Tested |
| numpy | 2.1.3 | ✅ Tested |
| openpyxl | 3.1.5 | ✅ Tested |
| Werkzeug | 3.1.3 | ✅ Tested |
| requests | 2.32.3 | ✅ Tested |
| gunicorn | 23.0.0 | ✅ Added |

### 3. Files Updated
- ✅ `runtime.txt` - Updated to python-3.13
- ✅ `requirements.txt` - All packages updated
- ✅ `api/requirements.txt` - All packages updated + gunicorn
- ✅ `vercel.json` - Updated runtime to python3.13

## 🚀 Vercel Deployment Configuration

### Vercel Configuration Status
Your project is **READY** for Vercel deployment with:

1. **Serverless Function:** `api/index.py` configured as Vercel Python serverless function
2. **Runtime:** Python 3.13 specified in `vercel.json`
3. **Frontend Build:** Vite build system configured
4. **API Routes:** Properly routed to `/api/*`

### API Endpoints
Your API includes these endpoints:
- `GET /` - Root endpoint with API info
- `GET /health` - Health check endpoint
- `POST /process-file` - Process uploaded Excel/CSV files
- `POST /interest-analysis` - Interest rate analysis

### Environment Variables (Optional)
If needed, add these in Vercel Dashboard:
- `PYTHONUNBUFFERED=1` (already configured in vercel.json)
- Add any custom environment variables your app needs

## 📝 Deployment Steps

### Step 1: Push to GitHub
```bash
git add .
git commit -m "Upgrade to Python 3.13 and optimize for Vercel deployment"
git push origin main
```

### Step 2: Connect to Vercel
1. Go to [vercel.com](https://vercel.com)
2. Import your GitHub repository: `prathamesh1010/India_Sweet_House3`
3. Vercel will auto-detect:
   - Framework: Vite
   - Build Command: `npm run build`
   - Output Directory: `dist`
   - API: Python serverless functions in `/api`

### Step 3: Deploy
- Click "Deploy"
- Vercel will automatically:
  - Install Python 3.13
  - Install dependencies from `api/requirements.txt`
  - Build frontend with Vite
  - Deploy serverless functions

### Step 4: Verify Deployment
Once deployed, test these URLs:
- `https://your-app.vercel.app/` - Frontend
- `https://your-app.vercel.app/api/health` - API health check
- `https://your-app.vercel.app/api/` - API root

## 🧪 Local Testing

### Start Backend API (Development)
```powershell
# Activate virtual environment
.\.venv\Scripts\Activate.ps1

# Start Flask server
python backend_api.py
```

### Test API Endpoints
```powershell
# Test health endpoint
Invoke-WebRequest -Uri http://localhost:5000/health -UseBasicParsing

# Test with file upload (replace with your test file)
$boundary = [System.Guid]::NewGuid().ToString()
$FilePath = "path\to\your\testfile.xlsx"
$fileBytes = [System.IO.File]::ReadAllBytes($FilePath)
$fileEnc = [System.Text.Encoding]::GetEncoding('iso-8859-1').GetString($fileBytes)

$body = @"
--$boundary
Content-Disposition: form-data; name="file"; filename="testfile.xlsx"
Content-Type: application/vnd.openxmlformats-officedocument.spreadsheetml.sheet

$fileEnc
--$boundary--
"@

Invoke-WebRequest -Uri http://localhost:5000/process-file `
    -Method POST `
    -ContentType "multipart/form-data; boundary=$boundary" `
    -Body $body
```

### Run Test Script
```powershell
python test_api.py
```

## 📊 Testing with Sample Data

To test the `/process-file` endpoint, you need an Excel file with:
- A worksheet named "Outlet wise" (for multi-sheet files)
- Columns including "PARTICULARS" and month-year columns (e.g., "JAN-23", "FEB-23")
- Financial data for outlets/stores

Upload your test file through:
1. The frontend UI (when running)
2. Direct POST to `/process-file` endpoint
3. Using the test script with file upload

## ⚙️ Configuration Files

### vercel.json
```json
{
  "version": 2,
  "builds": [
    {
      "src": "api/index.py",
      "use": "@vercel/python",
      "config": {
        "maxLambdaSize": "50mb",
        "runtime": "python3.13"
      }
    }
  ]
}
```

### runtime.txt
```
python-3.13
```

## 🔍 Troubleshooting

### If Vercel Build Fails
1. Check build logs in Vercel dashboard
2. Verify all files are committed to GitHub
3. Ensure `api/requirements.txt` has all dependencies
4. Check that Python 3.13 is compatible with all packages

### If API Returns 500 Error
1. Check Vercel function logs
2. Verify file upload format matches expected structure
3. Test locally first with same data
4. Check CORS configuration for frontend

### If Frontend Can't Connect to API
1. Verify API routes in `vercel.json`
2. Check frontend API base URL configuration
3. Ensure CORS is enabled (Flask-CORS is installed)

## 📈 Performance Optimizations

The following optimizations are already in place:
- **maxLambdaSize:** 50mb for handling large Excel files
- **CORS:** Enabled for frontend communication
- **Temp Storage:** Uses `/tmp` for Vercel serverless environment
- **Error Handling:** Comprehensive error handling with tracebacks

## 🎯 Next Steps

1. ✅ All dependencies tested and working on Python 3.13.9
2. ✅ Vercel configuration optimized
3. 📤 Ready to push to GitHub
4. 🚀 Ready for Vercel deployment

### To Deploy Now:
```bash
git add .
git commit -m "Upgrade to Python 3.13 with optimized Vercel config"
git push origin main
```

Then import your repository in Vercel dashboard - it will auto-deploy!

## 📞 Support

If you encounter issues:
1. Check Vercel deployment logs
2. Test locally first using the commands above
3. Verify all environment variables are set
4. Ensure your data files match the expected format

---

**Status:** ✅ Ready for Production Deployment
**Python Version:** 3.13.9
**All Tests:** Passed
