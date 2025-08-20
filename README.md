# Church Manager Pro

**A comprehensive, role-based church management system designed to streamline operations, track ministry progress, and empower church leaders with data-driven insights.**

---

## 🚀 Overview

Church Manager Pro is more than just a membership database; it's a centralized platform for modern church administration. This system is built to support the unique structure of different churches, from managing members and groups to tracking projects and reporting on key metrics. With a robust role-based access control system, it ensures that church leaders have the right tools and information to guide their congregations effectively.

---

## ✨ Features

### **Role-Based Access**

* **Chairman:** The highest authority within a church's account. A Chairman can create and manage all other roles and users.
* **Elders:** Created by the Chairman, Elders can create and manage Deacons, and view statistics and members specific to their assigned district.
* **Deacons:** (Details to be added by the Chairman or Elders)

### **Key Pages**

* **Landing Page (Unauthorized):** A public-facing marketing page to showcase the application's features and benefits to potential new churches.
* **Dashboard (Authorized):** Upon login, users see a personalized dashboard with their church's key statistics, recent member activity, and subscription status.
* **User Management:** Dedicated pages to view and manage lists of Elders, Deacons, and general members.
* **Church and District Registry:** Tools to register and organize churches into districts.
* **Groups & Activities:** Manage all church groups (e.g., youth, worship, Bible study) and a calendar for upcoming events.
* **Projects & Development:** Track the progress and details of church projects and initiatives.

### **Special Features**

* **Nicknames:** The system supports nicknames like "Mama Maina," which are common in many church communities, allowing for a more personal touch.
* **Custom Color Themes:** Users can select their preferred color scheme for a personalized interface.
* **File Backups:** Secure, regular backups to ensure all data is safe and recoverable.

---

## 🛠️ Technology Stack

This application is built using the following technologies:

* **Django:** The web framework for Python.
* **PostgreSQL:** The database for storing data.
* **React:** The JavaScript library for building the user interface.
<!-- * **Docker:** Containerization for easy deployment and management. -->
<!-- * **Nginx:** The web server for serving static files and handling requests. -->
<!-- * **Gunicorn:** The web server for serving Django applications. -->

### **Core Modules**

The application is structured around the following key modules:

* **`Subscribers`:** Manages potential leads from the public landing page.
* **`Churches`:** The core entity for each church using the system.
* **`Members`:** Stores detailed user information for every member of a church.
* **`MemberRoles`:** A joint table to link members to their specific roles and districts.
* **`Districts`:** Organizes members under a specific Elder.
* **`ChurchGroups`:** Manages various groups within a church.
* **`Projects` & `ProjectDetails`:** Tables to track project information.

---

## 📈 Future Enhancements

* **Accounting Module:** A comprehensive module to track church finances, including donations, expenditures, and budgeting.
<!-- * **(Add any other features you envision here)** -->

---

## 🤝 Contributing

We welcome contributions! If you're interested in helping with development, please read our `CONTRIBUTING.md` file for guidelines on how to get started.

---

## 📄 License

This project is licensed under the [Your License Here] - see the `LICENSE.md` file for details.