
import requests




myjsonData = {

    "prompt":"what is formula of water?"

}


print("Request sent.. waiting for chatGPT response....")
r = requests.post("http://127.0.0.1:5000/prompt", json={

    "prompt":"what is formula of wateR? avoid any special charactors"
})


print("status_code: ",r.status_code)
response = r.json()['chatGPT']
print("Response: ",response)