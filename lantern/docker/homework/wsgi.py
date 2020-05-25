from app.app import get_app

app = get_app()

if __name__ == "__main__":
    app.run(debug=True, port=5000)
    # app.run(debug=True, port=5000, use_reloader=False)
