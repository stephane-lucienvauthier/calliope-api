# calliope-api
A restful api for the calliope project.

# Create development environment

```bash
# Create virtual environment
python -m venv .venv

# With the seclected local python environment
pip install --upgrade pip
pip install wheel
pip install -r requirements.dev.txt

# Install the database
docker-compose up -d

# Launch the migrate
python manage.py makemigrations
python manage.py migrate

# Create the super user
python manage.py createsuperuser

```
