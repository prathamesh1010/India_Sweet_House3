# Vercel Deployment Guide

This project is now configured for deployment on Vercel with Python 3.11 backend support.

## Prerequisites

1. A [Vercel account](https://vercel.com/signup) (free tier works)
2. [Vercel CLI](https://vercel.com/docs/cli) installed (optional, but recommended)
3. Git repository pushed to GitHub, GitLab, or Bitbucket

## Deployment Steps

### Option 1: Deploy via Vercel Dashboard (Recommended)

1. **Push your code to GitHub**
   ```bash
   git add .
   git commit -m "Configure for Vercel deployment with Python 3.11"
   git push origin main
   ```

2. **Import Project to Vercel**
   - Go to [Vercel Dashboard](https://vercel.com/dashboard)
   - Click "Add New..." → "Project"
   - Import your GitHub repository
   - Vercel will auto-detect the configuration from `vercel.json`

3. **Configure Build Settings** (should be auto-detected)
   - Framework Preset: Vite
   - Build Command: `npm run build`
   - Output Directory: `dist`
   - Install Command: `npm install`

4. **Deploy**
   - Click "Deploy"
   - Wait for the build to complete (first build may take 2-3 minutes)

### Option 2: Deploy via Vercel CLI

1. **Install Vercel CLI** (if not already installed)
   ```bash
   npm i -g vercel
   ```

2. **Login to Vercel**
   ```bash
   vercel login
   ```

3. **Deploy**
   ```bash
   vercel
   ```
   - Follow the prompts
   - For production deployment, use: `vercel --prod`

## Configuration Details

### Backend API (Python 3.11)
- Location: `/api/index.py`
- Runtime: Python 3.11.0 (specified in `runtime.txt`)
- Dependencies: Listed in `api/requirements.txt`
- Endpoints:
  - `GET /api/health` - Health check
  - `POST /api/process-file` - Process Excel files
  - `POST /api/interest-analysis` - Interest cost analysis

### Frontend (React + Vite)
- Build output: `/dist`
- API calls are environment-aware:
  - Development: Uses `http://localhost:5000`
  - Production: Uses `/api` (relative path)

### Environment Variables
The app uses environment-specific configurations:
- `.env.development` - Local development
- `.env.production` - Production (Vercel)
- `.env.example` - Template file

No additional environment variables need to be set in Vercel dashboard for basic functionality.

## File Structure for Deployment

```
project/
├── api/
│   ├── index.py              # Python serverless function
│   └── requirements.txt      # Python dependencies
├── src/                      # React frontend source
├── dist/                     # Build output (generated)
├── vercel.json              # Vercel configuration
├── runtime.txt              # Python version specification
├── .vercelignore            # Files to exclude from deployment
├── .env.production          # Production environment variables
└── package.json             # Node.js dependencies
```

## Vercel Limits (Free Tier)

- **Serverless Function Size**: 50MB (configured in vercel.json)
- **Execution Timeout**: 10 seconds
- **Bandwidth**: 100GB/month
- **Build Minutes**: 6000 minutes/month

## Post-Deployment

After successful deployment:

1. **Test the API**
   - Visit: `https://your-app.vercel.app/api/health`
   - Should return: `{"status": "healthy", "message": "Backend API is running"}`

2. **Test File Upload**
   - Visit your app URL
   - Upload an Excel file
   - Verify data processing works

3. **Monitor Logs**
   - Go to Vercel Dashboard → Your Project → Logs
   - Monitor for any runtime errors

## Troubleshooting

### Build Fails
- Check the build logs in Vercel dashboard
- Ensure all dependencies are listed in `package.json`
- Verify Python dependencies in `api/requirements.txt`

### API Returns 500 Error
- Check function logs in Vercel dashboard
- Verify Python 3.11 is being used (check runtime.txt)
- Ensure uploaded files don't exceed 10MB (Vercel limit)

### Frontend Can't Connect to API
- Verify `.env.production` has `VITE_API_URL=/api`
- Check browser console for CORS errors
- Ensure API routes are properly configured in `vercel.json`

## Local Development

To test the deployment configuration locally:

1. **Start Backend**
   ```bash
   python backend_api.py
   ```

2. **Start Frontend**
   ```bash
   npm run dev:frontend
   ```

3. **Test Full Stack**
   ```bash
   npm run dev
   ```

## Updating Your Deployment

Simply push changes to your Git repository:
```bash
git add .
git commit -m "Your update message"
git push origin main
```

Vercel will automatically rebuild and redeploy your application.

## Custom Domain (Optional)

To add a custom domain:
1. Go to Vercel Dashboard → Your Project → Settings → Domains
2. Add your domain
3. Follow DNS configuration instructions

## Support

- [Vercel Documentation](https://vercel.com/docs)
- [Vercel Python Runtime](https://vercel.com/docs/functions/serverless-functions/runtimes/python)
- [Vite Deployment Guide](https://vitejs.dev/guide/static-deploy.html#vercel)
