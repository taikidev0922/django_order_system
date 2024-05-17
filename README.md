## Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-repository.git
   cd django_order_system
   ```

2. Create and start Docker containers:

   ```bash
   docker-compose up --build
   ```

3. Create and apply migrations:

   ```bash
   docker-compose run web python manage.py makemigrations
   docker-compose run web python manage.py migrate
   ```

django_order_system/
├── api/
│ ├── migrations/
│ ├── models/
│ │ ├── init.py
│ │ ├── customer.py
│ │ ├── product.py
│ │ └── order.py
│ ├── serializers/
│ │ ├── init.py
│ │ ├── customer.py
│ │ ├── product.py
│ │ └── order.py
│ ├── views/
│ │ ├── init.py
│ │ ├── customer.py
│ │ ├── product.py
│ │ └── order.py
│ ├── urls.py
│ ├── admin.py
│ ├── apps.py
│ ├── tests.py
│ └── views.py
├── django_order_system/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
├── .devcontainer/
│ └── devcontainer.json
├── manage.py
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
