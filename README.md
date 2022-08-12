![E-ZCal](/assets/logo.png)

# Inspiration
With the topic of “The Future of Productivity” being an option, we knew what we had to pick. As we become more technologically advanced, we’re slowly becoming less productive as it’s easier to get distracted. We figured one of the best ways to increase productivity was to tackle one of the main issues most people face with being productive, which is that it’s too difficult to find the balance between working and breaks! As college students who face a lot of difficulty with managing our work-life balance and finding convenient times for working and relaxing, we wanted to make something that would help us as much as it would help others. Our thought process was that if we were able to create a convenient way for our tasks to be spaced out throughout the day with appropriate breaks, that would increase our own productivity as much as it would anyone else. If you take the blunt work out of anything, people will surely gravitate towards it. And from there, with the hopes of creating something that could one day be of aid to us, we knew what we had to make.

# What it does
The main function of our project is being able to add your tasks into a queue and it automatically being added to your calendar when you press the “Add” button. Not only is it added into the calendar, every one of your tasks will be given 1 hour of time to do, with breaks included. By default, it will be balanced with 25 minutes of work, a 5 minute break, followed by the same thing again and that’s your hour (25-5-25-5). Our algorithm only functions on the 9AM-5PM time frame only.*

# How we built it
We began by constructing a front-end with Flask, Python, HTML/CSS, and Semantic-Ui; for the backend, we used SQLAlchemy for the database and handled all calendar events through the Google Calendar API for Python.

# Challenges we ran into
Our first major roadblock came when we couldn’t think of a solution to pushed overlaps on the Google Calendar.

# What we learned
We all either learned the tools, such as Flask, Semantic-UI, and SQLAlchemy for the first time, or gained even more experience with these tools through this project. We also learned the value of communication while working on the project and splitting it into multiple parts that each person can handle, such that we can connect everyone's parts synergistically at the end.

# What we are proud of
We are proud that we were actually able to implement an entirely working front and backend in such a short amount of time. We worked incredibly hard to build a minimum viable product that meets our standards, and only hope to extend the project further from here.

# What's next for EZCal
We hope to let users decide custom times for their given events, automate the authentication process, and let a user set a time frame outside of the default 9-5 that is set.
