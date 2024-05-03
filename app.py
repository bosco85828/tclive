from project import created_app

app=created_app()

if __name__ == "__main__":
    app.run('0.0.0.0',debug=True)