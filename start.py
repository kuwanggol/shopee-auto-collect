import requests
import sys
from datetime import datetime
import pytz
import time

def repeatSend():
  timezoneDefault = pytz.timezone("Asia/Manila") 
  timeInPH = datetime.now(timezoneDefault)
  currentTime = timeInPH.strftime("%I:%M:%P")
  return(currentTime)




def loopme():
  if repeatSend() == "12:01:am":
    url = 'https://shopee.ph/mkt/coins/api/v2/checkin_new'
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
    configs = [".OGl2TGUxbWY3eEdkcm9TRe1Q8VV1km4ufSS7aJDdgb1QZfJoZsmRl6481yFoJLOvu4tf3EV8sTHvedFQQKoO7CuDXJySJkuI/bDEib8Sjdebl0yKuUZ/2qQmzglO5EdUZBMU/vW2I8/yXYJzaI0IGboFennac0AaQiR5sqs7V7HuKplcJjUBmd9D2Lm3RhFRc31xSPtY8KQorNETSY3HLA==",
       ".YmtZc09KMmJZeGRSVlZEaxj2H5LoeVj2TSK7TOarEFehQj6ONBn3yQZxpeoagqe8DLJO/k8/h4Q5HybjUgmwkzzoij8UMKNLUMSQpNxJsO+uZGfzgkqbI2+7p/EI6tNr+IMvOZXj/ed47672l7zDYdDDjhZF+jsNV9FgV/VNazcXLXb1ugEkfzc4C+pBvNoA1+bolaJOqxKwWygCsfhuOQ==",
       ".VUFBcGF5ZXRxMFVRYm9waEK1AH+HdqITPM5UjZB4aZjwpm4P6F/256xPv0InQgS6Y8v/MoHy2y1CurNCgoqPcl2/wVHdlF+AcSvKvl7iU+oCrZx7QHsDWjT6h60WMyHZMG9+/6LKBM0pFOogC3KwzLkC9kPDjzrq3Ksl1CjBHWCDqYgZaVd0L/bqep76p0nzvLVUDLAjRx/bIx61DcGwYQ==",
       ".b3dOMUliRm1zTzcwZ1hCcEuNHH9q/rQ42QalCgdsRmXkjAh52KNDCsWhjO6h2QGkWi0/J1DbOeJ+3EygOGn7Vjq5RHirpyCJdKgoO0/vOUOKk35dtZxP6WpRq0n1F443I0GoIA/cXU3qJORL9DMEYhreUa1yDDqzxny9GAeGkP53XH/AnbDj2SwOH51M1MWonHBPqtu7yYGHg/3w+GyXhQ=="]
    for wew in configs:
      x = requests.post(url, headers=headers, cookies={
          "__LOCALE__null" : "PH",
          "SPC_ST" : wew,
      }
      )
      if (x.json()["data"]["success"]):
        print("Success Earning To Day + " + x.json()["data"]["username"])
        sys.stdout.flush()
      else:
        print("Failed Earning to Day " + x.json()["data"]["username"])
        sys.stdout.flush()
      spinMed = requests.post("https://games.shopee.ph/luckydraw/api/v1/lucky/event/8d0eac94b64bf045", headers=headers, cookies={
          "__LOCALE__null" : "PH",
          "SPC_ST" : wew,
          }, json={"request_id": "1",
                   "app_id":"5CX7XjYqk81xCNxpoL",
                   "activity_code":"67fb90b56800c6a9",
                   "source":2})
      if ("no chance" not in spinMed.json()["msg"] and "Unauthorization" not in spinMed.json()["msg"]):
        print("Success " + x.json()["data"]["username"] + " " + spinMed.json()["msg"])
      else:
        print("Failed " + x.json()["data"]["username"] + " " + spinMed.json()["msg"])
    time.sleep(50)
  else:
    print(repeatSend())
    time.sleep(59)
    sys.stdout.flush()
print("Bot Starting...")
sys.stdout.flush()
while True:
 loopme()

