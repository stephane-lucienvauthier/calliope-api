# calliope-api
A restful api for the calliope project.

# Create development environment

```bash
python -m venv .venv

# With the seclected local python environment
pip install --upgrade pip
pip install wheel
pip install -r requirements.dev.txt

# Install the database
docker-compose up -d

# Launch the migrate
export POSTGRES_PASS="calliope" && export POSTGRES_HOST="calliope-db.pytech.local" && python manage.py migrate

# Create the super user
export POSTGRES_PASS="calliope" && export POSTGRES_HOST="calliope-db.pytech.local" && python manage.py createsuperuser

```
