# Agenda Planner

## Team Members:
- Bhuvana Kotha - vkoth006 - https://github.com/bhuvanak04
- Mahir Patel - mpate141 - https://github.com/mahirpatel04
- Shaun Mansoor - smans029 - https://github.com/Mansoorkid
- Trisha Siva - tsiva006 - https://github.com/sivatrisha

## Project Description:

### Why is it important or interesting to you?
- Good for time management as a college student 
- Important to plan out projects
- Interesting because there are a lot of different features we can implement that are both functional and appealing to users
- Online planners allows users to access to manage their schedules from anywhere, compared to traditional written planners

### What languages/tools/technologies do you plan to use?
- C++

### What will be the input/output of your project?
- User inputs in details about upcoming events and deadlines they have
    - Start time, end time, date
    - People involved in the event
    - Description about task
    - So they can know when to plan the event/task and where it may fit best
    - User gets a clear view of their weekly tasks, events, etc
- Can get cool statistics such as:
    - XX% of your week was spent on homework
    - Completed XXX homework assignments
    - You average X hrs of sleep for the week


### What are the features that the project provides?
- Customization feature: user can select theme they like
- Allows users to input events and tasks to keep track of them
- Reminder feature
  - notifs for upcoming deadlines and events
- Event scheduling
  - Create multiple agendas for different purposes or events
- Task management
  - Allows users to add tasks or items to the agenda, set deadlines, etc
  - Suggests potential free days to schedule new events
  - Provides info and statistics on tasks completed during the 

  > ## Phase II

  ## User Interface Specification
### Navigation Diagram

 ![image](https://github.com/cs100/final-project-smans029-tsiva006-mpate141-vkoth006/assets/157240155/234196ca-56da-440d-ae35-3239d1f7b5f8)

 The user is first greeted with a simple Welcome message before proceeding to the main menu. Here, the user will be able to see and select several options of what they would like to do on their calendar application. Each option available corresponds to a different action they can perform, such as viewing the entire calendar, editing an existing event, removing an existing event, or adding a new one. The program then navigates to the appropriate page, based on the user input. From each section, the user will also be able to navigate back to the main menu page to then again choose what toher actions they would like to take int the program. 


### Screen Layouts

<img width="15000" alt="image" src="https://github.com/cs100/final-project-smans029-tsiva006-mpate141-vkoth006/assets/157240155/7ab21705-3c6a-4f03-904f-6dc87d49c778">





## Class Diagram
![image](https://github.com/cs100/final-project-smans029-tsiva006-mpate141-vkoth006/assets/46858459/910b2141-c66e-424c-93aa-f578fe20387e)

The week class contains an array of 7 day pointers, in which you can add, remove, display, or edit an event. These functions call helper functions from the Day class, which contains the events in it. It also conaints the struct of date, which contains the exact date that the user entered their data from, allowing them to plan out their week. The Day class contains the doubly linked list of events. It also contains the exact date that the day resides in after we calculate it from the time std library. The functions are almost all helper functions to those in Week. The eventNode class has all the components of the event, such as the title, start and end time, description, ID (in case 2 days have the same event), and the pointers to the events before and after it. 
 
 > ## Phase III
 > You will need to schedule a check-in for the second scrum meeting with the same reader you had your first scrum meeting with (using Calendly). Your entire team must be present. This meeting will occur on week 8 during lab time.
 
 > BEFORE the meeting you should do the following:
 > * Update your class diagram from Phase II to include any feedback you received from your TA/grader.
 > * Considering the SOLID design principles, reflect back on your class diagram and think about how you can use the SOLID principles to improve your design. You should then update the README.md file by adding the following:
 >   * A new class diagram incorporating your changes after considering the SOLID principles.
 >   * For each update in your class diagram, you must explain in 3-4 sentences:
 >     * What SOLID principle(s) did you apply?
 >     * How did you apply it? i.e. describe the change.
 >     * How did this change help you write better code?
 > * Perform a new sprint plan like you did in Phase II.
 > * You should also make sure that your README file (and Project board) are up-to-date reflecting the current status of your project and the most recent class diagram. Previous versions of the README file should still be visible through your commit history.
 
> During the meeting with your reader you will discuss: 
 > * How effective your last sprint was (each member should talk about what they did)
 > * Any tasks that did not get completed last sprint, and how you took them into consideration for this sprint
 > * Any bugs you've identified and created issues for during the sprint. Do you plan on fixing them in the next sprint or are they lower priority?
 > * What tasks you are planning for this next sprint.

 
 > ## Final deliverable
 > All group members will give a demo to the reader during lab time. ou should schedule your demo on Calendly with the same reader who took your second scrum meeting. The reader will check the demo and the project GitHub repository and ask a few questions to all the team members. 
 > Before the demo, you should do the following:
 > * Complete the sections below (i.e. Screenshots, Installation/Usage, Testing)
 > * Plan one more sprint (that you will not necessarily complete before the end of the quarter). Your In-progress and In-testing columns should be empty (you are not doing more work currently) but your TODO column should have a full sprint plan in it as you have done before. This should include any known bugs (there should be some) or new features you would like to add. These should appear as issues/cards on your Project board.
 > * Make sure your README file and Project board are up-to-date reflecting the current status of your project (e.g. any changes that you have made during the project such as changes to your class diagram). Previous versions should still be visible through your commit history. 
 
 ## Screenshots
 > Screenshots of the input/output after running your application
 ## Installation/Usage
 > Instructions on installing and running your application
 ## Testing
 > How was your project tested/validated? If you used CI, you should have a "build passing" badge in this README.
 


