# ✅ Vercel Deployment Checklist

Use this checklist to verify your project is ready for deployment.

## 📋 Pre-Deployment Checklist

### Configuration Files
- [x] `vercel.json` exists and configured
- [x] `runtime.txt` specifies Python 3.11.0
- [x] `.vercelignore` excludes unnecessary files
- [x] `.env.production` has correct API URL (`/api`)
- [x] `.env.development` has local API URL
- [x] `.gitignore` excludes sensitive files

### Backend (Python)
- [x] `api/index.py` exists with Flask app
- [x] `api/requirements.txt` lists all dependencies
- [x] Backend uses `/tmp/uploads` for file storage
- [x] CORS is configured for cross-origin requests
- [x] All endpoints return JSON responses

### Frontend (React)
- [x] API URL uses environment variable
- [x] FileUpload component updated
- [x] Build command configured: `npm run build`
- [x] Output directory set to: `dist`

### Documentation
- [x] `DEPLOYMENT.md` provides full guide
- [x] `QUICK_START.md` for quick reference
- [x] `README.md` updated with deployment info
- [x] `CHANGES_SUMMARY.md` documents all changes

## 🧪 Pre-Deployment Testing

### Test Locally First

1. **Install Dependencies**
   ```bash
   npm install
   pip install -r requirements.txt
   ```
   - [ ] Node.js dependencies installed
   - [ ] Python dependencies installed

2. **Test Backend**
   ```bash
   python api/index.py
   ```
   - [ ] Server starts without errors
   - [ ] Visit http://localhost:5000/health
   - [ ] Should return: `{"status": "healthy", ...}`

3. **Test Frontend**
   ```bash
   npm run dev:frontend
   ```
   - [ ] Vite dev server starts
   - [ ] Visit http://localhost:8080
   - [ ] Dashboard loads correctly

4. **Test Full Integration**
   ```bash
   npm run dev
   ```
   - [ ] Both frontend and backend start
   - [ ] Can upload Excel file
   - [ ] Data processes correctly
   - [ ] Charts display properly

5. **Test Production Build**
   ```bash
   npm run build
   ```
   - [ ] Build completes without errors
   - [ ] `dist/` folder is created
   - [ ] No TypeScript errors
   - [ ] No missing dependencies

## 🚀 Deployment Steps

### Push to GitHub
```bash
git add .
git commit -m "Configure for Vercel deployment with Python 3.11"
git push origin main
```
- [ ] Code pushed to GitHub
- [ ] No merge conflicts
- [ ] Branch is `main` or `master`

### Deploy on Vercel

#### Option A: Vercel Dashboard
1. [ ] Log in to [vercel.com](https://vercel.com)
2. [ ] Click "New Project"
3. [ ] Import your GitHub repository
4. [ ] Verify auto-detected settings:
   - [ ] Framework: Vite
   - [ ] Build Command: `npm run build`
   - [ ] Output Directory: `dist`
5. [ ] Click "Deploy"
6. [ ] Wait for deployment (2-3 minutes)

#### Option B: Vercel CLI
```bash
vercel login
vercel
```
- [ ] Logged in to Vercel CLI
- [ ] Project linked
- [ ] Deployed successfully

## ✅ Post-Deployment Verification

### 1. Check Deployment Status
- [ ] Deployment shows "Ready" status
- [ ] No build errors in logs
- [ ] No runtime errors in function logs

### 2. Test API Endpoints
Visit and verify each endpoint:

**Health Check**
```
https://your-app.vercel.app/api/health
```
- [ ] Returns 200 OK
- [ ] Returns: `{"status": "healthy", "message": "Backend API is running"}`

### 3. Test Frontend
Visit your app URL:
```
https://your-app.vercel.app
```
- [ ] Dashboard loads correctly
- [ ] No console errors
- [ ] Styling displays properly
- [ ] Navigation works

### 4. Test File Upload
1. [ ] Click file upload area
2. [ ] Select an Excel file
3. [ ] File uploads successfully
4. [ ] Data processes correctly
5. [ ] Results display in dashboard
6. [ ] Charts render properly

### 5. Test All Features
- [ ] Revenue charts display
- [ ] Outlet manager view works
- [ ] Interest analysis (if applicable)
- [ ] Data table loads
- [ ] Filters work correctly
- [ ] Export functionality (if any)

## 🔧 Troubleshooting

If any test fails, check:

### Build Errors
- [ ] Check Vercel build logs
- [ ] Verify all dependencies in package.json
- [ ] Check Python dependencies in api/requirements.txt
- [ ] Ensure Node.js version compatibility

### API Errors (500/502)
- [ ] Check function logs in Vercel dashboard
- [ ] Verify Python 3.11 is being used
- [ ] Check for missing Python packages
- [ ] Verify file size doesn't exceed limits

### Frontend Issues
- [ ] Check browser console for errors
- [ ] Verify environment variables
- [ ] Check if API calls use correct URL
- [ ] Inspect network tab for failed requests

### CORS Errors
- [ ] Verify Flask-CORS is configured
- [ ] Check Vercel routing in vercel.json
- [ ] Ensure API path matches route

## 📊 Performance Check

After deployment:
- [ ] Page load time < 3 seconds
- [ ] API response time < 2 seconds
- [ ] File upload works for files up to 10MB
- [ ] No memory errors in function logs

## 🎉 Success Criteria

Your deployment is successful when:
- ✅ All tests pass
- ✅ API health check returns 200
- ✅ File upload and processing works
- ✅ Dashboard displays data correctly
- ✅ No console errors
- ✅ No function timeout errors

## 📝 Post-Deployment Tasks

- [ ] Share deployment URL with team
- [ ] Update any external links
- [ ] Set up custom domain (optional)
- [ ] Configure monitoring/alerts (optional)
- [ ] Document any deployment issues

## 🔗 Useful Links

- Vercel Dashboard: https://vercel.com/dashboard
- Deployment Logs: Check in Vercel → Your Project → Deployments
- Function Logs: Check in Vercel → Your Project → Functions
- Domain Settings: Vercel → Your Project → Settings → Domains

---

**Need Help?**
- Full deployment guide: `DEPLOYMENT.md`
- Quick start: `QUICK_START.md`
- Changes summary: `CHANGES_SUMMARY.md`
- Vercel Docs: https://vercel.com/docs

---

**Last Updated**: December 2, 2025
**Python Version**: 3.11.0
