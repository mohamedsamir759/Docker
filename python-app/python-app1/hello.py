import fire
def hello(name="World"):
  return "Hello %s!" % name

if __name__ == '__main__':
  fire.Fire(hello)
  app.run(host='0.0.0.0', port=6000)
