# 🚀 Frontend Setup Guide

## Quick Start

1. **Navigate to frontend directory:**
   ```bash
   cd frontend
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start development server:**
   ```bash
   npm run dev
   ```

4. **Open browser:**
   Navigate to `http://localhost:3000`

## Prerequisites

- Node.js 18+ installed
- Backend API running on `http://localhost:8000`

## Configuration

The frontend automatically connects to `http://localhost:8000` by default.

To change the API URL, create a `.env` file in the `frontend/` directory:

```env
VITE_API_URL=http://your-api-url:8000
```

## Available Scripts

- `npm run dev` - Start development server
- `npm run build` - Build for production
- `npm run preview` - Preview production build

## Features

✨ Modern UI with glassmorphism effects
📱 Fully responsive design
🎯 Interactive battle creation
📊 Detailed results visualization
🎭 Persona selection with previews

