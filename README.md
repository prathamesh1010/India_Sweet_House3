# India Sweet House - Analytics Dashboard

## Project Overview

A comprehensive financial analytics dashboard for India Sweet House restaurant chain, providing insights into sales performance, revenue analysis, and operational metrics.

## How can I edit this code?

**Use your preferred IDE**

Clone this repo and work locally using your own IDE. You can push changes directly to the repository.

The only requirement is having Node.js & npm installed - [install with nvm](https://github.com/nvm-sh/nvm#installing-and-updating)

Follow these steps:

```sh
# Step 1: Clone the repository using the project's Git URL.
git clone <YOUR_GIT_URL>

# Step 2: Navigate to the project directory.
cd <YOUR_PROJECT_NAME>

# Step 3: Install the necessary dependencies.
npm i

# Step 4: Start the development server with auto-reloading and an instant preview.
npm run dev
```

**Edit a file directly in GitHub**

- Navigate to the desired file(s).
- Click the "Edit" button (pencil icon) at the top right of the file view.
- Make your changes and commit the changes.

**Use GitHub Codespaces**

- Navigate to the main page of your repository.
- Click on the "Code" button (green button) near the top right.
- Select the "Codespaces" tab.
- Click on "New codespace" to launch a new Codespace environment.
- Edit files directly within the Codespace and commit and push your changes once you're done.

## What technologies are used for this project?

This project is built with:

- Vite
- TypeScript
- React
- shadcn-ui
- Tailwind CSS
- Python 3.11 (Backend API)
- Flask (REST API)
- Pandas (Data Processing)

## How can I deploy this project?

### Quick Deploy to Vercel (Recommended)

This project is configured for seamless deployment on Vercel with Python 3.11 backend support.

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/prathamesh1010/India_Sweet_House3)

**Deployment Steps:**
1. Push your code to GitHub
2. Import the project to Vercel
3. Vercel will automatically detect the configuration
4. Click "Deploy" and wait for the build to complete

For detailed deployment instructions, see [DEPLOYMENT.md](./DEPLOYMENT.md)

### Other Platforms

This project can also be deployed to:
- Netlify (with serverless functions)
- Railway
- Render
- AWS Amplify

Note: Backend API requires Python 3.11 runtime support.

## Project Structure

```
project/
├── api/                     # Python backend (Flask)
│   ├── index.py            # Serverless function
│   └── requirements.txt    # Python dependencies
├── src/                    # React frontend
│   ├── components/         # UI components
│   ├── pages/             # Page components
│   └── utils/             # Utilities
├── vercel.json            # Vercel configuration
├── runtime.txt            # Python version (3.11)
└── DEPLOYMENT.md          # Deployment guide
```

## Local Development

### Prerequisites
- Node.js (v18 or higher)
- Python 3.11
- npm or yarn

### Setup

1. **Install Node.js dependencies:**
   ```bash
   npm install
   ```

2. **Install Python dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the full stack (frontend + backend):**
   ```bash
   npm run dev
   ```

   Or start separately:
   ```bash
   # Terminal 1 - Backend
   npm run dev:backend
   
   # Terminal 2 - Frontend
   npm run dev:frontend
   ```

4. **Access the application:**
   - Frontend: http://localhost:8080
   - Backend API: http://localhost:5000
   - Health Check: http://localhost:5000/health

## Features

- **Financial Analytics Dashboard**: Comprehensive analysis of restaurant performance
- **Revenue Tracking**: Monitor sales and revenue across multiple outlets
- **Data Visualization**: Interactive charts and graphs for better insights
- **Admin Console**: Manage data and system settings
- **Responsive Design**: Works seamlessly on desktop and mobile devices
