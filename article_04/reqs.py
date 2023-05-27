import requests, time, threading

url = 'http://127.0.0.1:8000/names'

def request_loop(url):
    while True:
        try:
            response = requests.get(url, headers={'Connection': 'close'})
            if response.status_code == 200:
                data = response.json()
                print(data)
                time.sleep(0.2)
            else:
                continue
        except requests.exceptions.RequestException as e:
            print(e)

threads = []
for i in range (500):
    t = threading.Thread(target=request_loop, args=(url,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()