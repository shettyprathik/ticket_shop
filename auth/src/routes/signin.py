from src import app
from src.errors.database_connection_error import DatabaseConnectionError

@app.route('/api/users/signin')
def signin():
    raise DatabaseConnectionError()
    
