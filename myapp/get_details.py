import http.client
import json
import certifi
import requests

ca_bundle_path = certifi.where()
response = requests.get('https://api.zoom.us/v2/some_endpoint', verify=certifi.where())


conn = http.client.HTTPSConnection("api.zoom.us")
payload = json.dumps({
  "topic": "test",
  "type": 2,
  "start_time": "2023-08-01T03:32:55Z",
  "duration": 6,
  "settings": {
    "host_video": True,
    "participant_video": True,
    "join_before_host": True,
    "mute_upon_entry": True,
    "watermark": True,
    "audio": "telephony",
    "auto_recording": "cloud"
  }
})
headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJzdiI6IjAwMDAwMSIsImFsZyI6IkhTNTEyIiwidiI6IjIuMCIsImtpZCI6Ijc1YjU2ZTNkLTUzZTItNGYxOC04ZDk2LThjOGI5ZDJhM2E1NSJ9.eyJ2ZXIiOjksImF1aWQiOiJkNGFiZGY0MTc5NTk3NGUyYzljZGI0ZTYyMTVmMDNkMiIsImNvZGUiOiJvMTVWY3djSUFNUUZNY2EtbVFYU0tPLXBwOGxtYmdfX0EiLCJpc3MiOiJ6bTpjaWQ6SXJnc01uUzFUaktLSTVGNTBqVmxydyIsImdubyI6MCwidHlwZSI6MCwidGlkIjo5LCJhdWQiOiJodHRwczovL29hdXRoLnpvb20udXMiLCJ1aWQiOiJfVGdoR09KclJlNlF1LVlRZ0szS09RIiwibmJmIjoxNjkyMjg0NDc0LCJleHAiOjE2OTIyODgwNzQsImlhdCI6MTY5MjI4NDQ3NCwiYWlkIjoidmVsZ2dlVEpUSjZaNnkzYlBBZHpkZyJ9.And7sYfM1UP91hrpFVgBhlgFFTGT57oc_Lvs7EU701l_dl2LbPAx_sWFX6bCgrpfeDRMHNYquL_LDbR3CKkUsg',
  'Cookie': 'TS018dd1ba=0109ff88b94c7ff5c5c1785c5d3033b4a88f8d4b004d0179fcb9a98d750f853b93cef95d4fdd1dc67b99e420b563da0a71229b8c3a; TS01fdc528=018b99c656f0fc7987ab6775e7d8e31ae00850e1f0e320eeb8a3e7d22061f5079f7aed44bd35964d78474583192353e23c24a4ae2c; __cf_bm=JagQa9ZlL2oGjuO2dzPRNC_nCqjDHVW7WF_mZ5ueKXY-1692284474-0-Aat4Xvy00NFvjs/+zwfpcTAk+iP34WABq18umkS6z0g0lQvHdLrDEjt4ezcjt/UbKIsjIOwurjhb5qHPYmuEJQ4=; _zm_chtaid=448; _zm_ctaid=GGfNZqfvQFO2mB3U7ez7bA.1692284474211.0459cc7e5fc83d128806642e2a68da65; _zm_mtk_guid=ec0be6dd59a64a9e8300f9d37b1a1948; _zm_page_auth=us04_c_TClOWzFdQ-iKKncpw7kZbg; _zm_ssid=us04_c_EzsKRkvsQXOILknuO1f8nw; TS01f92dc5=016ab599ce6518b7d19ed92ffbe7a2f9e49cef5969f27c45736cdb059353678db8b420c88cec648011618459f61e00f05e52a0af86; cred=BA50BB9F54B005789CDCFE92423E729E'
}
conn.request("GET", "/v2/users/me/meetings", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
data1= json.loads(data)
#print(data1["meetings"])
'''for meeting in data1["meetings"]:
    print("Topic:", meeting["topic"])
    print("Start Time:", meeting["start_time"])
    print("Duration:", meeting["duration"])
    print("Join URL:", meeting["join_url"])'''