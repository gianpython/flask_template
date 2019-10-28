from app import app

if __name__ == "__main__":
    #app.config['DEBUG']  = True
    if app.config["ENV"] == "production":
        app.config.from_object("config.ProductionConfig")
    else:
        app.config.from_object("config.DevelopmentConfig")

    print(f'ENV is set to: {app.config["ENV"]}')

    app.run()
