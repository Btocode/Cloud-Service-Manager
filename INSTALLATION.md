# Cloud Service Management

This Django application is designed to accomplish cloud service management for admin and users.

## Prerequisites

- Python version 3.10 or higher
- Virtual environment (optional but recommended)

## Installation

1. **Unzip the Project:**

   Unzip the downloaded project to your desired location.

2. **Navigate to the Project Directory:**

   ```bash
   cd <Project directory>
   ```

3. **Create a Virtual Environment (Optional but Recommended):**

   ```bash
   python -m venv venv
   ```

4. **Activate the Virtual Environment:**

   - For Unix/Linux:

     ```bash
     source venv/bin/activate
     ```

   - For Windows:

     ```bash
     .\venv\Scripts\activate
     ```

5. **Install Dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

6. **Apply Database Migrations:**

   ```bash
   python manage.py migrate
   ```

7. **Run the Development Server:**

   ```bash
   python manage.py runserver
   ```

8. **Visit [http://localhost:8000/](http://localhost:8000/) in Your Web Browser to Access the Application.**
