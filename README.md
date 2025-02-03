# Kimi

*A distributed task scheduling system based on Huey.*

## Installation

clone:
```
$ git clone https://github.com/sungeer/krathon.git
$ cd krathon
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
$ granian --interface wsgi kimi:app
* Running on http://127.0.0.1:8000/
```

run distributed scheduling:
```
$ huey_consumer kimi.tasks.huey_instance.huey
```

## License

This project is licensed under the MIT License (see the
[LICENSE](LICENSE) file for details).
