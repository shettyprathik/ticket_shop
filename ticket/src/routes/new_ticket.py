from src import app


@app.route('/api/tickets', methods=['POST'])
def new_ticket():
    return 'new_ticket'
