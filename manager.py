from info import create_app

app = create_app("develop")

@app.route('/')
def hello_world():
    #
    # redis_store.set("name","los")
    # print(redis_store.get("name"))

    return 'Hello World!'


if __name__ == '__main__':
    app.run()
