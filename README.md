# Music Controller

A collaborative music controller that lets multiple users in a shared room vote to skip songs and control Spotify playback in real-time.

## Features

- Create or join a music room with a unique code
- Host controls Spotify playback (play, pause, skip)
- Guests can vote to skip songs — skip triggers when vote threshold is reached
- Real-time song info (title, artist, album art, progress bar)
- Built with Django REST Framework + React

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python, Django, Django REST Framework |
| Frontend | React, JavaScript |
| Real-time | Django Sessions |
| Auth | Spotify OAuth 2.0 |
| Database | SQLite (dev) |

## Getting Started

### Prerequisites

- Python 3.8+
- Node.js 14+
- A [Spotify Developer App](https://developer.spotify.com/dashboard) with credentials

### 1. Clone & install dependencies

```bash
git clone https://github.com/patelabhi1607/music_controller.git
cd music_controller
pip install django djangorestframework requests
cd frontend && npm install && cd ..
```

### 2. Configure environment variables

```bash
cp .env.example .env
```

Edit `.env` with your values:

```
DJANGO_SECRET_KEY=your-django-secret-key
SPOTIFY_CLIENT_ID=your-spotify-client-id
SPOTIFY_CLIENT_SECRET=your-spotify-client-secret
SPOTIFY_REDIRECT_URI=http://127.0.0.1:8000/spotify/redirect
```

> In your Spotify app dashboard, add `http://127.0.0.1:8000/spotify/redirect` as a Redirect URI.

### 3. Apply migrations & run

```bash
python manage.py migrate
python manage.py runserver
```

In a separate terminal, build the React frontend:

```bash
cd frontend
npm run dev
```

Open `http://127.0.0.1:8000` in your browser.

## How It Works

1. A user creates a room and authenticates with Spotify — they become the host
2. Other users join via the room code
3. The host's Spotify account controls playback
4. Guests vote to skip; when votes reach the threshold the song skips automatically
5. Current song info updates in real-time via polling the Spotify API

## Project Structure

```
music_controller/
├── api/            # Room model, create/join/leave endpoints
├── spotify/        # Spotify OAuth, playback control, credentials
├── frontend/       # React app (webpack bundled)
├── music_controller/ # Django settings & URL routing
└── manage.py
```
