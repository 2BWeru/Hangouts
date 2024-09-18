# Hangouts
Hangouts is a dynamic events platform that allows users to discover, create, and manage events effortlessly. Whether you're hosting a small meetup or a large conference, 
Hangouts provides all the tools you need to make event planning and participation seamless.

This project uses Django Rest Framework and Django for the backend and Angular for the frontend, creating a highly responsive and efficient web application.

### Partner
This project was developed in collaboration with `DeanKago`. Check out their profile for more amazing projects!

## Features
- Event Discovery: Browse and discover events based on your interests.
- Event Creation and Management: Create, edit, and manage your own events, including setting dates, descriptions, and locations.
- User Registration & Authentication: Sign up, log in, and manage your account.
- Ticketing: Users can reserve and manage event tickets.
- Responsive Design: Enjoy a smooth experience across all devices.
- Backend: Built with Django Rest Framework to handle data efficiently.
- Frontend: Interactive and responsive interface built with Angular for a dynamic user experience.

## Installation
To set up the project locally, follow these steps:

### Prerequisites
Ensure you have the following installed:
- Python (version 3.8 or higher)
- Node.js (version 14 or higher)
- npm or yarn
- Angular CLI
- Django

#### Backend Setup (Django)
1. Clone the repository:
`git clone https://github.com/your-username/Hangouts.git`

2. Navigate to the backend directory:
`cd Hangouts/backend`

4. Create a virtual environment:
`python -m venv env`

5. Activate the virtual environment:
On Windows:
`env\Scripts\activate`

On Mac/Linux:
`source env/bin/activate`

6. Install backend dependencies:
`pip install -r requirements.txt`

7. Run migrations:
`python manage.py migrate`

8. Run the Django development server:
`python manage.py runserver`


### Frontend Setup (Angular)
1. Navigate to the frontend directory:
`cd ../frontend`
2. Install frontend dependencies:
`npm install`
3. Run the Angular development server:
`ng serve`
4. Open your browser and navigate to:
`http://localhost:4200`

## Usage
- Sign up / Log in: Create an account to start creating or joining events.
- Browse Events: Use the event discovery tool to find upcoming events based on your location and interests.
- Create an Event: Organize your own event by filling in details like event title, description, location, and ticketing options.
- Manage Events: Edit or cancel your event as needed, track attendees, and manage ticket sales.

## Contributing
We welcome contributions from the community! To contribute:

Fork the repository.
- Create a new branch: `git checkout -b feature/your-feature-name`.
- Commit your changes: `git commit -m 'Add some feature'`.
- Push to the branch: `git push origin feature/your-feature-name`.
- Submit a pull request.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

