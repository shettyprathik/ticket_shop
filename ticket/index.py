from src import app, consume_broker


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=6000)
