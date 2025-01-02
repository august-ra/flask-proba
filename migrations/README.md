Single-database configuration for Flask Proba.

List of commands with it:
- `flask db init` to create folder "migrations"
- `flask db migrate -m "meaningful name"` to create migration and new db at the first time
- `flask db upgrade` to allow migration
- `flask db downgrade` to cancel migration
