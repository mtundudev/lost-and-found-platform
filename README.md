Lost & Found Platform

A public, scalable full-stack web platform that helps individuals and communities report, search for, and recover lost and found items.

The platform is designed for everyone — students, parents, families, workers, residents, visitors, and other members of the community.

It can initially be used within a university or local community, but the architecture is designed to scale beyond a single institution, organization, location, or group.

---

📌 About the Project

Finding a lost item can be difficult when people rely on WhatsApp groups, social media posts, word of mouth, or physical announcements.

The Lost & Found Platform provides a centralized public platform where people can report items they have lost or found and allow others to search for matching information.

For example:

- A student loses a phone on campus.
- A resident loses an identification document in their neighborhood.
- Someone finds a bag and wants to report it.
- A family member searches for an item lost by a relative.
- A person finds an item and publishes its details so the owner can identify it.

The platform is not restricted to students or universities.

---

🌍 Vision

The long-term vision is to build a scalable public Lost & Found platform that can serve individuals and communities across different locations.

The platform should be capable of growing from:

Local Community
      ↓
District
      ↓
Region
      ↓
Country
      ↓
Multiple Countries

without requiring the core system to be redesigned.

---

🎯 Project Goals

The main goals are to:

- Provide a public platform for lost and found items.
- Make it easier for people to report lost items.
- Make it easier for people to report found items.
- Help users discover potentially matching items.
- Reduce dependence on scattered social media and messaging groups.
- Provide organized information about lost and found items.
- Allow users to manage their own posts.
- Build a scalable real-world full-stack application.
- Practice professional backend architecture and API development.

---

👥 Target Users

The platform is public and is not restricted to a specific group.

Potential users include:

- Students
- Parents
- Family members
- Workers
- Business owners
- Residents
- Visitors
- Community members
- Any individual looking for a lost or found item

A user does not need to belong to a university, organization, company, or other institution to use the platform.

---

🔐 Platform Ownership & Administration

The platform has no platform owner, administrator, editor, moderator, or special privileged user in Version 1.0.

There are no administrative roles responsible for controlling other users.

The system is designed around normal user ownership.

A user can manage the resources they create, but cannot manage another user's resources.

For example:

User A
 ├── Lost Item A
 └── Found Item A

User B
 ├── Lost Item B
 └── Found Item B

User A can manage their own posts.

User A cannot edit or delete User B's posts.

---

👤 User Accounts

Users can create accounts to use protected platform functionality.

Users can:

- Register
- Log in
- Log out
- View their profile
- Update their profile
- Manage their own posts
- Create lost item reports
- Create found item reports
- Update their own posts
- Delete their own posts

Authentication is required for actions that create or modify user-owned resources.

Public browsing functionality may be accessible without requiring an account where appropriate.

---

📦 Lost & Found Items

The platform supports two primary types of reports:

Lost Item
Found Item

Lost Item

A user creates a Lost Item report when they have lost something.

Example:

Title: Black Smartphone
Category: Electronics
Location: Mbeya
Date: 2026-08-01
Description: Black smartphone lost near the bus stand.

---

Found Item

A user creates a Found Item report when they find something belonging to another person.

Example:

Title: Black Smartphone Found
Category: Electronics
Location: Mbeya
Date: 2026-08-01
Description: Black smartphone found near the bus stand.

---

✨ Planned Features

User Features

- [ ] User registration
- [ ] User login
- [ ] User logout
- [ ] User profile
- [ ] Update profile
- [ ] Change password

Lost Item Features

- [ ] Create lost item report
- [ ] View lost item
- [ ] Update own lost item
- [ ] Delete own lost item
- [ ] Upload lost item image
- [ ] Mark lost item as recovered

Found Item Features

- [ ] Create found item report
- [ ] View found item
- [ ] Update own found item
- [ ] Delete own found item
- [ ] Upload found item image
- [ ] Mark found item as returned

Discovery Features

- [ ] Search items
- [ ] Filter by item type
- [ ] Filter by category
- [ ] Filter by location
- [ ] Filter by date
- [ ] Sort results
- [ ] Pagination
- [ ] View item details

Communication

- [ ] Contact item poster
- [ ] Provide safe contact information
- [ ] Support communication between people who may have a matching lost/found item

---

🗺️ Location Support

The platform should not be permanently tied to a single location.

Location information should be designed to support future geographic expansion.

Possible hierarchy:

Country
   ↓
Region
   ↓
District
   ↓
Ward / Area
   ↓
Specific Location

For example:

Tanzania
   ↓
Mbeya
   ↓
Mbeya District
   ↓
Iyunga
   ↓
Bus Stand

The exact location model may evolve as the platform grows.

---

🔎 Search

Users should be able to search for lost and found items.

Example:

GET /items?search=phone

Search can consider:

- Item title
- Description
- Category
- Location

Future versions may introduce more advanced matching between lost and found reports.

---

🗂️ Filtering

The platform should support filtering by:

- Item type
- Category
- Location
- Date
- Status

Example:

Type:
Lost / Found

Category:
Electronics

Location:
Mbeya

Status:
Active / Recovered / Returned

---

📄 Pagination

Large result sets must be paginated.

Example:

GET /items?page=1&limit=20

Pagination prevents the API from returning unnecessarily large amounts of data.

---

↕️ Sorting

Users should be able to sort results.

Possible sorting fields:

created_at
event_date
title
location

The exact fields will depend on the final item model.

Supported ordering:

asc
desc

Example:

GET /items?sort=created_at&order=desc

---

🖼️ Image Upload

Users should be able to upload images of lost or found items.

Images can help users identify potential matches.

The system should support:

- Image upload
- Image validation
- Image storage
- Image retrieval
- Image deletion when appropriate

The application should validate uploaded files to prevent unsafe file uploads.

---

🔄 Item Status

Items should have a status representing their current state.

Possible statuses may include:

active
recovered
returned

The exact status model will be finalized during implementation.

Example:

Lost Phone
Status: Active

After the owner recovers it:

Lost Phone
Status: Recovered

---

🤝 Ownership

Every lost or found post belongs to the user who created it.

Relationship:

User
 │
 │ 1
 │
 └──────────< Items

One user can create many items.

Each item belongs to exactly one creator.

The backend must always determine the creator from the authenticated user.

The API must never trust a client-provided "created_by" or "user_id" when determining ownership.

---

🔒 Authorization Rules

Version 1.0 does not have administrators or privileged platform roles.

Authorization is based on resource ownership.

Public users

Depending on the endpoint, public users may:

- Browse available items
- Search items
- Filter items
- View public item information

Authenticated users

Authenticated users can:

- Create their own reports
- Update their own reports
- Delete their own reports
- Manage their own profile
- Change their own password

Ownership Rule

Is the authenticated user the creator?
             │
       ┌─────┴─────┐
      Yes           No
       │             │
       ▼             ▼
   Continue       403 Forbidden

A user cannot modify or delete another user's item.

---

🛡️ Security Principles

The platform must follow these principles:

- Never store plain-text passwords.
- Never expose password hashes.
- Never trust client-provided user IDs.
- Never trust client-provided ownership information.
- Validate all user input.
- Validate uploaded files.
- Store secrets in environment variables.
- Never commit ".env" to GitHub.
- Use authentication for protected operations.
- Use authorization based on resource ownership.
- Use appropriate HTTP status codes.
- Keep sensitive information out of public responses.

---

🏗️ Technology Stack

Frontend

- HTML
- CSS
- JavaScript

The frontend will communicate with the FastAPI backend through HTTP APIs.

---

Backend

- Python
- FastAPI
- Uvicorn

---

Database

- MySQL

---

ORM

- SQLAlchemy

---

Database Migrations

- Alembic

---

Data Validation

- Pydantic

---

Authentication

- JWT

---

Development Tools

- Git
- GitHub
- Visual Studio Code
- Swagger / OpenAPI

---

🏛️ Backend Architecture

The backend follows a layered architecture:

Client
  │
  ▼
Router / API Layer
  │
  ▼
Service Layer
  │
  ▼
Repository Layer
  │
  ▼
SQLAlchemy Models
  │
  ▼
MySQL

Router

Responsible for:

- HTTP requests
- HTTP responses
- Dependency injection
- Calling services
- API-level validation

Routers should remain thin.

---

Service

Responsible for:

- Business logic
- Ownership validation
- Application rules
- Authentication logic
- Item status rules
- Calling repositories

---

Repository

Responsible for:

- Database queries
- Creating records
- Reading records
- Updating records
- Deleting records
- Searching
- Filtering
- Sorting
- Pagination

---

Models

Responsible for:

- Database tables
- Relationships
- Constraints

---

Schemas

Responsible for:

- Request validation
- Response validation
- API data contracts

---

📂 Project Structure

The project will follow a modular structure:

must-lost-and-found/
│
├── app/
│   │
│   ├── main.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── database.py
│   │   ├── dependencies.py
│   │   └── security.py
│   │
│   ├── route/
│   │   ├── health.py
│   │   ├── auth.py
│   │   ├── users.py
│   │   └── items.py
│   │
│   ├── services/
│   │   ├── auth_service.py
│   │   ├── user_service.py
│   │   └── item_service.py
│   │
│   ├── repositories/
│   │   ├── user_repository.py
│   │   └── item_repository.py
│   │
│   ├── models/
│   │   ├── user.py
│   │   └── item.py
│   │
│   ├── schemas/
│   │   ├── user.py
│   │   └── item.py
│   │
│   └── utils/
│
├── alembic/
│
├── tests/
│
├── media/
│
├── docs/
│
├── frontend/
│
├── .env.example
├── .gitignore
├── alembic.ini
├── requirements.txt
└── README.md

The structure may evolve as the project grows.

---

🗄️ Database Concept

The initial database will contain user and item-related information.

Basic relationship:

Users
  │
  │ 1
  │
  └──────────< Items

An item belongs to one user.

A user can create many items.

The database design should remain flexible enough to support future features without requiring a complete rewrite.

---

🔌 API

The backend exposes RESTful APIs.

Initial API areas include:

/auth
/users
/items

Example endpoints:

POST /auth/register
POST /auth/login
POST /auth/logout
GET  /auth/me

PUT  /users/me
PUT  /users/me/password

POST /items
GET  /items
GET  /items/{item_id}
PUT  /items/{item_id}
DELETE /items/{item_id}

The final API specification will be documented in the project's API documentation.

---

📊 API Features

The Items API is expected to support:

- Create
- Read
- Update
- Delete
- Search
- Filtering
- Sorting
- Pagination
- Ownership validation
- Status management

---

❌ No Admin System

Version 1.0 intentionally does not include:

- Admin dashboard
- Super Admin
- Editor role
- Moderator role
- Platform owner account
- Administrative approval workflow

The platform is designed as a public, user-driven system.

---

🚧 Project Status

Status: In Development

Version:

1.0.0

The project is being developed incrementally.

Features will be implemented through GitHub Issues and small, focused commits.

---

🗺️ Development Roadmap

Phase 1 — Foundation

- [x] Project setup
- [x] FastAPI architecture
- [x] MySQL configuration
- [x] SQLAlchemy setup
- [x] Alembic setup
- [x] Environment configuration

Phase 2 — Authentication

- [ ] User registration
- [ ] Login
- [ ] JWT authentication
- [ ] Logout
- [ ] User profile
- [ ] Password change

Phase 3 — Lost & Found

- [ ] Create lost item
- [ ] Create found item
- [ ] View item
- [ ] Update own item
- [ ] Delete own item
- [ ] Item status

Phase 4 — Discovery

- [ ] Search
- [ ] Filtering
- [ ] Sorting
- [ ] Pagination
- [ ] Location-based discovery

Phase 5 — Media

- [ ] Image upload
- [ ] Image validation
- [ ] Image storage
- [ ] Image retrieval

Phase 6 — Recovery

- [ ] Item claim process
- [ ] Ownership verification
- [ ] Contact/report flow
- [ ] Recovered/returned status

Phase 7 — Quality

- [ ] Unit tests
- [ ] Integration tests
- [ ] API tests
- [ ] Security testing
- [ ] Swagger documentation

Phase 8 — Deployment

- [ ] Production configuration
- [ ] Database deployment
- [ ] Backend deployment
- [ ] Frontend deployment
- [ ] Environment configuration
- [ ] Production testing

---

📈 Scalability

The platform is designed with scalability in mind.

The architecture separates:

API
Business Logic
Database Access
Database Models

This allows individual components to evolve independently.

Future versions may support:

- Multiple countries
- Multiple regions
- Multiple communities
- Advanced location search
- Improved item matching
- Notifications
- Mobile applications
- Multiple languages
- External integrations
- Cloud storage
- Advanced search
- Real-time communication

These features are not part of Version 1.0 unless explicitly added to the project requirements.

---

🧪 Testing

The project will include automated tests.

Testing should cover:

- User registration
- Authentication
- Profile management
- Lost item creation
- Found item creation
- Item retrieval
- Item updates
- Item deletion
- Ownership rules
- Search
- Filtering
- Sorting
- Pagination
- Image uploads
- Item status
- Error handling

All API endpoints should also be tested through Swagger during development.

---

📚 API Documentation

FastAPI automatically provides OpenAPI documentation.

Development documentation:

/docs

Alternative documentation:

/redoc

OpenAPI schema:

/openapi.json

All public API endpoints should have clear:

- Endpoint descriptions
- Request schemas
- Response schemas
- Authentication requirements
- HTTP status codes
- Error responses

---

⚙️ Environment Configuration

Create a local ".env" file containing environment-specific configuration.

Example:

APP_NAME=Lost & Found Platform
DEBUG=True

DATABASE_URL=mysql+pymysql://username:password@localhost/lost_and_found

SECRET_KEY=your-secret-key
ACCESS_TOKEN_EXPIRE_MINUTES=30

The ".env" file must never be committed.

Use ".env.example" to document required variables.

---

🚀 Local Development

Clone the repository:

git clone https://github.com/mtundudev/must-lost-and-found.git

Enter the project:

cd must-lost-and-found

Create a virtual environment:

python -m venv venv

Activate it.

Install dependencies:

pip install -r requirements.txt

Configure the ".env" file.

Run database migrations:

alembic upgrade head

Start the API:

uvicorn app.main:app --reload

Open the API documentation:

http://127.0.0.1:8000/docs

---

🌿 Git Workflow

Development should use small, focused commits.

Recommended workflow:

Issue
  ↓
Create Branch
  ↓
Write Code
  ↓
Test
  ↓
Commit
  ↓
Push
  ↓
Pull Request
  ↓
Merge

---

📝 Commit Convention

Use Conventional Commits.

Examples:

feat: add lost item creation

feat: add item search

fix: validate item ownership

test: add item repository tests

docs: update api documentation

refactor: simplify item service

---

🤝 Contribution

The platform is designed as a public project.

Contributions may be accepted as the project develops.

Contributors should:

1. Create or select an Issue.
2. Create a dedicated branch.
3. Implement the change.
4. Write or update tests.
5. Follow the project's architecture.
6. Use Conventional Commit messages.
7. Open a Pull Request.
8. Clearly describe the changes.

All contributions must preserve the core principles of the platform.

---

📜 Development Principles

The project follows these principles:

1. Keep the API simple

Endpoints should be predictable and RESTful.

2. Keep routers thin

Business logic belongs in services.

3. Keep database access isolated

Database queries belong in repositories.

4. Validate everything

All external input must be validated.

5. Protect user ownership

Users can manage only their own resources.

6. Never trust the client

Important information such as ownership must be determined by the backend.

7. Security first

Passwords, secrets, and sensitive information must be protected.

8. Design for growth

Avoid architecture that unnecessarily limits the platform to one organization or location.

9. Build incrementally

Features should be developed through small, testable Issues.

---

⚠️ Scope of Version 1.0

Version 1.0 focuses on the core Lost & Found experience:

User
  ↓
Register / Login
  ↓
Report Lost or Found Item
  ↓
Search
  ↓
View Details
  ↓
Contact / Claim
  ↓
Recover / Return

Advanced features should not be added until the core platform is stable.

---

💡 Future Possibilities

The platform may eventually evolve into a broader community service supporting:

- Universities
- Schools
- Villages
- Neighborhoods
- Bus stations
- Markets
- Workplaces
- Public spaces
- Cities
- Countries

The platform itself remains independent of any particular institution.

---

👨‍💻 Developer

MTUNDEV

GitHub:

https://github.com/mtundudev

Project Repository:

https://github.com/mtundudev/must-lost-and-found

---

📄 License

This project is licensed under the MIT License.

---

Project Summary

Lost & Found Platform is a public, scalable full-stack application designed to connect people with lost and found items.

It is not owned by a university, organization, administrator, or individual within the application.

Users manage their own content, while the platform provides the infrastructure needed to discover, report, and recover lost belongings.

Built with:

Python
FastAPI
MySQL
SQLAlchemy
Alembic
Pydantic
HTML
CSS
JavaScript

Version 1.0.0 — In Development 🚧
