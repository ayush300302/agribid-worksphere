
# AgriBid WorkSphere - Technical Architecture

## 1. Project Overview

AgriBid WorkSphere is a project management and team collaboration
platform designed to manage users, teams, projects and tasks.

## 2. Technology Stack

### Frontend
- Next.js
- React
- TypeScript
- Tailwind CSS
- shadcn/ui

### Backend
- Python
- FastAPI
- SQLAlchemy
- Pydantic

### Database and Infrastructure
- PostgreSQL
- Docker
- Alembic
- Psycopg

## 3. Application Architecture

The application follows a frontend-backend architecture.

Browser
   |
   v
Next.js Frontend
Port: 3000
   |
   | HTTP REST API
   v
FastAPI Backend
Port: 8000
   |
   v
SQLAlchemy
   |
   v
Psycopg PostgreSQL Driver
   |
   v
PostgreSQL Database
Docker Container

## 4. Backend Responsibilities

- Handle API requests.
- Implement business logic.
- Authenticate and authorize users.
- Validate incoming data.
- Communicate with PostgreSQL.
- Manage database transactions.

## 5. Frontend Responsibilities

- Display application interfaces.
- Handle user interactions.
- Manage forms and validation.
- Communicate with backend APIs.
- Display application data.

## 6. Database Management

SQLAlchemy is used for ORM and database operations.

Alembic manages database schema migrations.

PostgreSQL stores application data.

Docker provides an isolated environment for PostgreSQL.

## 7. Current Database Models

- User
- Role

## 8. Implemented Features

- FastAPI application setup.
- PostgreSQL Docker configuration.
- SQLAlchemy database connection.
- Alembic migration setup.
- User and Role tables.
- Default role seeding.
- Backend health endpoint.
- Frontend-to-backend connectivity.

## 9. Planned Modules

- Authentication and authorization.
- User management.
- Team management.
- Project management.
- Ticket management.
- Comments and attachments.
- Notifications.
- Dashboards and reports.

## 10. Application Ports

| Application | Port |
|---|---|
| Next.js Frontend | 3000 |
| FastAPI Backend | 8000 |
| PostgreSQL Host | 5433 |
| PostgreSQL Container | 5432 |
