# CS-340-12642-M01-Client-Server-Development-2026-C-3-May-Jun-
Course repository for CS-340 Client/Server Development, containing project files, database work, and application code for the 2026 C-3 term.


## Reflection

### How do you write programs that are maintainable, readable, and adaptable?

I write maintainable, readable, and adaptable programs by separating responsibilities, using clear names, and organizing code so that each part has a specific purpose. In this project, the CRUD Python module from Project One helped keep the database logic separate from the dashboard code in Project Two. Instead of writing database queries directly inside the dashboard, I was able to call methods from the CRUD module to create, read, update, and delete data. This made the dashboard easier to understand because the dashboard focused on user interaction and visual display, while the CRUD module handled communication with MongoDB.

The advantage of working this way is that the code becomes easier to update, test, and reuse. If the database connection or query logic needs to change, I can update the CRUD module without rewriting the entire dashboard. In the future, this same CRUD module could be reused in other applications that need to connect to the animal shelter database, such as a web app, reporting tool, or another dashboard for different rescue organizations.

### How do you approach a problem as a computer scientist?

As a computer scientist, I approach a problem by first understanding the client’s requirements and then breaking the problem into smaller parts. For the Grazioso Salvare project, I had to think about what data the client needed, how the database should be queried, and how the dashboard should present the information in a useful way. I focused on filtering animals based on rescue type, displaying the results in a table, and showing visual information such as charts and a map.

This project was different from previous assignments because it felt more like a real client request. Instead of only writing code to meet a small requirement, I had to connect multiple parts together: the database, the CRUD module, the dashboard layout, filtering logic, and visualizations. In the future, I would use similar strategies by reviewing the client’s needs, designing the database queries carefully, testing the results, and making sure the final application is useful and easy to understand.

### What do computer scientists do, and why does it matter?

Computer scientists solve problems using technology, data, and logical thinking. They design systems, write programs, manage data, and create tools that help people complete tasks more efficiently. This matters because many organizations rely on software to make better decisions, save time, and organize large amounts of information.

For a company like Grazioso Salvare, this type of project could help them do their work better by making it easier to find animals that match specific rescue training needs. Instead of manually searching through shelter records, the dashboard allows users to filter animals, review important details, and view location information quickly. This helps the organization make faster, more informed decisions and supports their mission of identifying animals that may be good candidates for rescue work.
