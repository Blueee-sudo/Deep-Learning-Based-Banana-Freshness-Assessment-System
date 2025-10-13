from ultralytics import YOLOv10

model_path = 'yolov10m.pt'
data_path = 'data.yaml'

if __name__ == '__main__':
    model = YOLOv10(model_path)
    results = model.train(data=data_path,
                          epochs=500,
                          batch=64,
                          device='0',
                          workers=0,
                          project='runs',
                          name='exp',
                          )