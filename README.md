# BookingCalendar
The interface that allows to book time slots for small service companies like hairdressers or restaurants etc. 

# Basic information
- BookingCalendar stores 3 types of users:
  - User - person who can book the time slot in specified calendar
  - Client - person who can create and update calendars. Calendars are assigned to Clients
  - Admin person who can add and remove Clients and Users
- One Client can have many Calendars (like one company can have many employees) 
- Time slots can be booked in specific calendar

# Getting Started
To start project you have:
- Run virtual environment. Details: [Virtual environment instruction](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)
- install Flask
```
pip install -U Flask
```
- Flask-SQLAlchemy
```
pip install -U Flask-SQLAlchemy
```
- Flask-JWT
```
pip install -U Flask-JWT
```
- clone project to directory next to virtual environment
- run app.py

