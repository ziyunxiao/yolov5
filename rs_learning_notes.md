# Setup
fork the project ounder your own then clone it.

## setup virtual env
```
python3.9 -m venv .venv

.venv/bin/activate

pip install -r requirements.txt

```

## download weights to local folder

```
wget https://github.com/ultralytics/yolov5/releases/download/v4.0/yolov5s.pt
wget https://github.com/ultralytics/yolov5/releases/download/v4.0/yolov5m.pt
wget https://github.com/ultralytics/yolov5/releases/download/v4.0/yolov5l.pt
wget https://github.com/ultralytics/yolov5/releases/download/v4.0/yolov5x.pt
```

## test run

```
python detect.py --source data/images --weights yolov5s.pt --conf 0.25

```

