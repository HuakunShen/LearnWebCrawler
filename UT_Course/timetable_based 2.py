
import requests

url = 'https://timetable.iit.artsci.utoronto.ca/api/20199/courses?org=&code=MAT137&section=&studyyear=&daytime=&weekday=&prof=&breadth=&online=&waitlist=&available=&title='

params = dict(
    origin='Chicago,IL',
    destination='Los+Angeles,CA',
    waypoints='Joplin,MO|Oklahoma+City,OK',
    sensor='false'
)

resp = requests.get(url=url)
data = resp.json() # Check the JSON Response Content documentation below
print(data)

print("hello world")