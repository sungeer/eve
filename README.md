# Eve

*A distributed task scheduling system based on Huey.*

## Installation

clone:
```
$ git clone https://github.com/sungeer/eve.git
$ cd eve
```
create & activate virtual env then install dependency:

with venv + pip:
```
$ python -m venv venv
$ source venv/bin/activate  # use `venv\Scripts\activate` on Windows
$ pip install -r requirements.txt
```

run:
```
$ granian --interface wsgi eve:app
* Running on http://127.0.0.1:8000/
```

run distributed scheduling:
```
$ huey_consumer eve.tasks.huey_instance.huey
```

## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
