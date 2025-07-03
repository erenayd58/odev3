Bu proje, YOLOv5s modeli kullanarak görsellerdeki **STOP trafik işaretlerini** tespit eder. Tespit edilen işaretler görsel üzerine yeşil kutu ve merkez noktası ile işaretlenir. Model, COCO veri kümesinde eğitildiği için sınıf ID'si 11 olan "stop sign" nesnesini algılar.


git clone https://github.com/<erenayd58>/odev3.git

cd odev3


pip install -r requirements.txt

python detect_stop_sign.py
