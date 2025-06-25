# Lost and Found Django App

A web application for reporting and searching lost and found items in university campus, built with Django. Users can add items they’ve found or lost, search through listed items, and get in touch with each other to recover lost property.

---

## Features

- Submit lost or found items with pictures and details
- Search for items by name or description
- View recent lost & found items on the home page
- Responsive, modern design (Tailwind CSS + custom styles)


### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**

   ```sh
   git clone https://github.com/Al1husse1n/Lost-and-Found-Django-.git
   cd Lost-and-Found-Django-
   ```

2. **Create and activate a virtual environment**

   ```sh
   python -m venv venv
   # On Windows:
   venv\Scripts\activate
   # On Mac/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations**

   ```sh
   python manage.py migrate
   ```

5. **Create a superuser (for admin access)**

   ```sh
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```sh
   python manage.py runserver
   ```

7. **Visit the app**

   Open your browser and go to [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Project Structure

```
Lost_and_found/
├── Lost_and_found/         # Django project settings
├── main/                   # Main app: models, views, templates
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── models.py
│   ├── views.py
│   └── ...
├── db.sqlite3
├── manage.py

```

---

## Core Models

- **LostItem**
  - `item_name`: Name of item
  - `item_picture`: Image upload
  - `item_description`: Description
  - `item_founder` : username of submitter
  - `contactEmail`: Owner’s/submitter’s email
  - `found_at`: Location where found/lost
  - `reported_datetime`: When reported
  - `found_datetime`: When found
  - `status`: lost/found
  - `claimed_by`: (if enabled) User who claims the item

---





## Credits

Developed by [@Al1husse1n](https://github.com/Al1husse1n)

---

