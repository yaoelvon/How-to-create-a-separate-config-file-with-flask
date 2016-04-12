First create a config.cfg file.
Contents:
```
HELLO='Hi!'
```
Then in your main python file for flusk (where you run everything):
```
app = Flask(__name__)

app.config.from_pyfile('config.cfg')

# And use it like so:
app.config['HELLO']
```
