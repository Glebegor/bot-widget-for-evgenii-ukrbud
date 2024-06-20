import Bootstrap

def main():
    config = Bootstrap.Config()
    app = Bootstrap.Application(config=config.ToDict())
    app.run()

if __name__ == '__main__':
    main()