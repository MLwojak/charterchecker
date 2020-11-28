import speedtest
import tweepy

# This script will test whether or not your speed matches 
# what you pay for in Mbps. It will then grab and 
# compare the values to determine if CharterChecker
# needs to tag @AskSpectrum in a tweet. If it does, then 
# it will pass the values to CharterChecker, who will format
# the message, authenticate to Twitter, and send the tweet.

# You can test against a specific server with its ID number. This can be found
# in results_dict dictionary after a test with the basic speedtest API 
# under the "id" key. It is recommended to choose a server close to you. 
# To see a list of closest servers, run this command in a terminal:
# curl -s https://raw.githubusercontent.com/sivel/speedtest-cli/master/speedtest.py | python - --list
# Uncomment the s.get_best_server() function and comment out s.get_servers(servers) to 
# let the API select the best server.

# E.g. 18857 is Bel Air Internet LLC from Los Angeles, CA
servers = [18857]

s = speedtest.Speedtest()
s.get_servers(servers)
#s.get_best_server()
s.download()
s.upload()
results_dict = s.results.dict()

# Replace these values with the advertised internet speed
# from the contract with your ISP.
trueDownload = 200
trueUpload = 10

# Data formatting, from raw bits to Mbps with decimal values
mbps = "Mbps"
downloadSpeed = str(round(results_dict["download"] / 1048576 , 2))
uploadSpeed = str(round(results_dict["upload"] / 1048576 , 2))
    
# Summarized test 
print("Download Speed:",downloadSpeed + mbps,"\nUpload Speed:",uploadSpeed + mbps)

# Compares value
if float(downloadSpeed) < trueDownload or float(uploadSpeed) < trueUpload:
    isSpeedOkay = False
elif float(downloadSpeed) >= trueDownload and float(uploadSpeed) >= trueUpload:
    isSpeedOkay = True

print(isSpeedOkay)