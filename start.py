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
  if repeatSend() == "01:27:pm":
    url = 'https://shopee.ph/mkt/coins/api/v2/checkin_new'
    headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:105.0) Gecko/20100101 Firefox/105.0"}
    configs = [".OGl2TGUxbWY3eEdkcm9TRe1Q8VV1km4ufSS7aJDdgb1QZfJoZsmRl6481yFoJLOvu4tf3EV8sTHvedFQQKoO7CuDXJySJkuI/bDEib8Sjdebl0yKuUZ/2qQmzglO5EdUZBMU/vW2I8/yXYJzaI0IGboFennac0AaQiR5sqs7V7HuKplcJjUBmd9D2Lm3RhFRc31xSPtY8KQorNETSY3HLA==",
       ".WDBNa01ibmdrSkZITmpCdZiYVvN4aX1VhduNUXEE159DLUOIIdiKl/opLh3K5NR2WyRT77iHTlThWDY/i4JhzA1aJz78MuuvsGt7HF3YTnIHHPtgjDdRHf8mxi7GGiCyFS4ymJhDdQG2ycH7EmUr4lInc3X1OPThu3dTgl0k6llbE+PGf+3vyHSl7D3vIJD39pZyZMxWwmbg+0CmPdAESg==",
       ".Q0dWNnRRYWl3MXU5Z1AyYercc9ch+p6rbXHgc3zqW8uPuXYcj0MQsQrvD4ZebBUpam3RU03upAmKStUeQcskyceJxUtNkM4nC0/KH2yEaI09iFU/nVPYIxoem04jeTcsjnhXT03rjK1vOFYOXsdSXJBhNdar33Os7t3CBG7H5+jEtdQDGccVzlif9k6ZC0WeBtq1fG4sJZsdDxbGfAEpkg==",
       ".cVNpTzNjekZZeFBHcDhpSHrxH2E1tkaSXDSdtUCqBI7Cl4BdSmpiVdAFSUVxS4+Rs2WfGwa/XHfImO2dM/FIAKKxdd65EXZHrb0ydGPgtjsSwAAKof+JrZYWklW7TnKU3iiSnjU5qVE/mRqkoP0pJndY3x7hDn9x8eupO/F9zoi8XRxjc2TVUUgoGwcIk+4fRfB7BFl85VOf41+xES/Iug=="]
    for wew in configs:
      x = requests.post(url, headers=headers, cookies={
          "__LOCALE__null" : "PH",
          "SPC_ST" : wew,
      }
      )
      if (x.json()["data"]["success"]):
        print("Success + " + x.json()["data"]["username"])
      else:
        print("Failed " + x.json()["data"]["username"])
    time.sleep(50)
  else:
    pass
print ("hello world") # python 3
sys.stdout.flush()
while True:
 loopme()
