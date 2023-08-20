from django.shortcuts import render


'''
-----------------------Code for API Call---------------------
import http.client
import json

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
  'Authorization': 'Bearer eyJzdiI6IjAwMDAwMSIsImFsZyI6IkhTNTEyIiwidiI6IjIuMCIsImtpZCI6ImZhZDM0MzViLTljODYtNGYyYy05MzVmLWQ3OGM2NTIzOWU1YiJ9.eyJ2ZXIiOjksImF1aWQiOiJkNGFiZGY0MTc5NTk3NGUyYzljZGI0ZTYyMTVmMDNkMiIsImNvZGUiOiJvMTVWY3djSUFNUUZNY2EtbVFYU0tPLXBwOGxtYmdfX0EiLCJpc3MiOiJ6bTpjaWQ6SXJnc01uUzFUaktLSTVGNTBqVmxydyIsImdubyI6MCwidHlwZSI6MCwidGlkIjo3LCJhdWQiOiJodHRwczovL29hdXRoLnpvb20udXMiLCJ1aWQiOiJfVGdoR09KclJlNlF1LVlRZ0szS09RIiwibmJmIjoxNjkyMjAxODg3LCJleHAiOjE2OTIyMDU0ODcsImlhdCI6MTY5MjIwMTg4NywiYWlkIjoidmVsZ2dlVEpUSjZaNnkzYlBBZHpkZyJ9.KiZg6dUhrXUq2B5lOCiye2_lZcEulEup-WLH3DAjHp_38-zQdj5Niztd5AsprMDI6C19aEBno1fOEhNoIpoiJA',
  'Cookie': 'TS018dd1ba=0109ff88b94c7ff5c5c1785c5d3033b4a88f8d4b004d0179fcb9a98d750f853b93cef95d4fdd1dc67b99e420b563da0a71229b8c3a; TS01fdc528=018b99c656f0fc7987ab6775e7d8e31ae00850e1f0e320eeb8a3e7d22061f5079f7aed44bd35964d78474583192353e23c24a4ae2c; __cf_bm=6NYZsdNzCPUG78kGyZiGNAVVLazg4YXZXVSmnsO_HuE-1692201887-0-ARxsenaRcGNL20XrxZucXS3NHsg+uIQ18hYZHwLUI5NKpX+k/Am97ZbBWFRkXTnqvFeIrxK0GhMxsxa5/HRo23M=; _zm_chtaid=894; _zm_ctaid=SszPISCCRm6amYDSWIJL4A.1692201887590.d9d04b035e19aed651bfd317463c6dde; _zm_mtk_guid=ec0be6dd59a64a9e8300f9d37b1a1948; _zm_page_auth=us04_c_VY5PKe77SRKois3pzrKWeQ; _zm_ssid=us04_c_EzsKRkvsQXOILknuO1f8nw; TS01f92dc5=016ab599ce6518b7d19ed92ffbe7a2f9e49cef5969f27c45736cdb059353678db8b420c88cec648011618459f61e00f05e52a0af86; cred=BA50BB9F54B005789CDCFE92423E729E'
}
conn.request("GET", "/v2/users/me/meetings", payload, headers)
res = conn.getresponse()
data = res.read()
print(data.decode("utf-8"))
data1= json.loads(data)
#print(data1["meetings"])
for meeting in data1["meetings"]:
    print("Topic:", meeting["topic"])
    print("Start Time:", meeting["start_time"])
    print("Duration:", meeting["duration"])
    print("Join URL:", meeting["join_url"])'''


#sample response
meetings = [
    {
        'title': 'Computer Netwroks - Section A',
        'professor': 'Professor XYZ',
        'start_time': '8:00 AM - 9:00 AM',
        'link': 'https://us04web.zoom.us/j/76707447361?pwd=LPIcTR2NW74aAFZ3qxX6hhSTVbUNFd.1'
    },
    {
        'title': 'Operating Systems - Section B',
        'professor': 'Professor ABC',
        'start_time': '9:00 AM - 10:00 AM',
        'link': 'https://us04web.zoom.us/j/76707447361?pwd=LPIcTR2NW74aAFZ3qxX6hhSTVbUNFd.1'
    },
    {
        'title': 'Algorithms - Section C',
        'professor': 'Professor XYZ',
        'start_time': '11:00 AM - 12:00 PM',
        'link': 'https://us04web.zoom.us/j/76707447361?pwd=LPIcTR2NW74aAFZ3qxX6hhSTVbUNFd.1'
    },
    {
        'title': 'Operating Systems - Section A',
        'professor': 'Professor ABC',
        'start_time': '10:00 AM - 11:00 AM',
        'link': 'https://us04web.zoom.us/j/76707447361?pwd=LPIcTR2NW74aAFZ3qxX6hhSTVbUNFd.1'
    },
    {
        'title': 'Data Structures - Section B',
        'professor': 'Professor XYZ',
        'start_time': '10:00 AM - 11:00 AM',
        'link': 'https://us04web.zoom.us/j/76707447361?pwd=LPIcTR2NW74aAFZ3qxX6hhSTVbUNFd.1'
    },

]

#views
def meetdeet(request):
    context = {
        'meetings':meetings
    }
    return render(request, 'meetdeet.html', context)

def home(request):
    return render(request, 'home.html')

def sectionA(request):
    context = {
        'meetings':meetings
    }
    return render(request, 'sectionA.html', context)

def sectionB(request):
    context = {
        'meetings':meetings
    }
    return render(request, 'sectionB.html', context)

def sectionC(request):
    context = {
        'meetings':meetings
    }
    return render(request, 'sectionC.html', context)
