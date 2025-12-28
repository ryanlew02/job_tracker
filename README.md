# Job & Interview Tracker API

## Overview
The **Job & Interview Tracker API** is a backend-focused application designed to help users organize and track their job search process. It provides a structured way to store job applications, companies, interviews, contacts, notes, and reminders, all accessible through a clean, well-documented REST API.

This project is built as a standalone backend service and emphasizes real-world backend engineering concepts such as API design, relational data modeling, validation, and persistence. It can be consumed by any frontend (web, mobile, or CLI) and serves as a portfolio-ready backend project.

---

## Key Features
- **Job Application Management**  
  Create, update, and track job applications with statuses such as *Applied*, *Interviewing*, *Offer*, or *Rejected*.

- **Company & Contact Tracking**  
  Store companies, recruiters, and hiring manager contacts associated with applications.

- **Interview Scheduling**  
  Track multiple interview rounds per application, including interview type, date, and notes.

- **Notes & Follow-Ups**  
  Attach notes and reminders to jobs or interviews to manage follow-ups and preparation.

- **Filtering & Search**  
  Query applications by status, company, date range, or keyword.

- **Dashboard & Analytics Endpoints**  
  Aggregate data such as application counts, upcoming interviews, and pipeline conversion metrics.

---

## Tech Stack
- **Backend Framework:** FastAPI  
- **Language:** Python  
- **Database:** SQLite (development), designed to scale to PostgreSQL  
- **ORM:** SQLAlchemy  
- **Data Validation:** Pydantic  
- **API Documentation:** OpenAPI / Swagger UI  
- **Testing:** Pytest  

---

## Architecture
The application follows a clean, layered architecture:
- **Routes** handle HTTP requests and responses  
- **Schemas** define request and response validation  
- **Models** define database tables and relationships  
- **Services / CRUD layer** encapsulate business logic  
- **Database layer** manages sessions and persistence  

This separation keeps the codebase maintainable, testable, and scalable.

---

## Example API Endpoints
```http
POST   /jobs
GET    /jobs?status=interviewing
GET    /jobs/{job_id}
POST   /companies
POST   /interviews
GET    /dashboard/stats
