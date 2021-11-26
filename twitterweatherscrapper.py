import snscrape.modules.twitter as snt
import pandas as pd
from deep_translator import GoogleTranslator
import datetime,pytz
import yagmail

def runFilesendMail():

    #Final email to be sent
    final_msg = ""

    #Time config
    #Current time config
    currentcentraltime=datetime.datetime.utcnow()   #utcnow class method
    currentindiantime=currentcentraltime.replace(tzinfo=pytz.UTC) #replace method
    current_time_kolkata=currentindiantime.astimezone(pytz.timezone("Asia/Kolkata")) #astimezone method
    #------------------------------------------------------------------------------------
    #Threshold time
    threshold_time = current_time_kolkata - pd.DateOffset(hours=12)
    #------------------------------------------------------------------------------------

    tweetslistone = []
    for ione, tweetone in enumerate(snt.TwitterSearchScraper('from:APWeatherman96').get_items()):
        checkeronearr = []
        checkeronearr.append([tweetone.date])
        checkeronearr_org = pd.DataFrame(checkeronearr, columns=['Datetime'])
        if (checkeronearr_org.Datetime[0]<=threshold_time):
            break
        mentusers = []
        mentusers.append(tweetone.mentionedUsers)
        if mentusers[0] is None:
            tweetslistone.append([tweetone.date,tweetone.content])


    tweetslistone_org = pd.DataFrame(tweetslistone, columns=['Datetime', 'Text'])
    final_msg = final_msg+"Last 2hrs reports by AndhraWeatherMan @APWeatherman96: \n"
    for xone in range(len(tweetslistone_org)):
        
        latestone = tweetslistone_org.Text[xone]
        latesttimeone = tweetslistone_org.Datetime[xone]
        translatedone = GoogleTranslator(source='auto', target='te').translate(latestone)
        final_msg = final_msg+"Original tweet: \n"
        final_msg = final_msg+latestone
        final_msg = final_msg+"\n"
        final_msg = final_msg+"Translated to Telugu: \n"
        final_msg = final_msg+translatedone
        final_msg = final_msg+"\n"
        final_msg = final_msg+"Time of tweet: \n"
        final_msg = final_msg+str(latesttimeone)
        final_msg = final_msg+"\n \n \n"

    #------------------------------------------------------------------------------------
    tweetslisttwo = []
    for itwo, tweettwo in enumerate(snt.TwitterSearchScraper('from:VizagWeather247').get_items()):
        checkertwoarr = []
        checkertwoarr.append([tweettwo.date])
        checkertwoarr_org = pd.DataFrame(checkertwoarr, columns=['Datetime'])
        if (checkertwoarr_org.Datetime[0]<=threshold_time):
            break
        mentusers = []
        mentusers.append(tweettwo.mentionedUsers)
        if mentusers[0] is None:
            tweetslisttwo.append([tweettwo.date,tweettwo.content])


    tweetslisttwo_org = pd.DataFrame(tweetslisttwo, columns=['Datetime', 'Text'])
    final_msg = final_msg+"Last 2hrs by VizagWeatherMan @VizagWeather247: \n"
    for xtwo in range(len(tweetslisttwo_org)):
        
        latesttwo = tweetslisttwo_org.Text[xtwo]
        latesttimetwo = tweetslisttwo_org.Datetime[xtwo]
        translatedtwo = GoogleTranslator(source='auto', target='te').translate(latesttwo)
        final_msg = final_msg+"Original tweet: \n"
        final_msg = final_msg+latesttwo
        final_msg = final_msg+"\n"
        final_msg = final_msg+"Translated to Telugu: \n"
        final_msg = final_msg+translatedtwo
        final_msg = final_msg+"\n"
        final_msg = final_msg+"Time of tweet: \n"
        final_msg = final_msg+str(latesttimetwo)
        final_msg = final_msg+"\n \n \n"

    #------------------------------------------------------------------------------------
    tweetslistthree = []
    for ithree, tweetthree in enumerate(snt.TwitterSearchScraper('from:Rajani_Weather').get_items()):
        checkerthreearr = []
        checkerthreearr.append([tweetthree.date])
        checkerthreearr_org = pd.DataFrame(checkerthreearr, columns=['Datetime'])
        if (checkerthreearr_org.Datetime[0]<=threshold_time):
            break
        mentusers = []
        mentusers.append(tweetthree.mentionedUsers)
        if mentusers[0] is None:
            tweetslistthree.append([tweetthree.date,tweetthree.content])


    tweetslistthree_org = pd.DataFrame(tweetslistthree, columns=['Datetime', 'Text'])
    final_msg = final_msg+"Last 2hrs by HyderabadWeatherMan @Rajani_Weather: \n"
    for xthree in range(len(tweetslistthree_org)):
        
        latestthree = tweetslistthree_org.Text[xthree]
        latesttimethree = tweetslistthree_org.Datetime[xthree]
        translatedthree = GoogleTranslator(source='auto', target='te').translate(latestthree)
        final_msg = final_msg+"Original tweet: \n"
        final_msg = final_msg+latestthree
        final_msg = final_msg+"\n"
        final_msg = final_msg+"Translated to Telugu: \n"
        final_msg = final_msg+translatedthree
        final_msg = final_msg+"\n"
        final_msg = final_msg+"Time of tweet: \n"
        final_msg = final_msg+str(latesttimethree)
        final_msg = final_msg+"\n \n \n"

        final_msg = final_msg+"*(if empty then no reports from the source in last 2hrs)"

    #EMAIL 

    #-----------------------------------------------------------------------------------
    #Enter your EMAIL-ID (after allowing access to less secure apps in email settings), and then Enter email password in the given fields
    yag = yagmail.SMTP('ENTER YOUR EMAIL (SENDER EMAIL) HERE (ALLOW ACCESS TO LESS SECURE APPS IN YOUR EMAIL SETTINGS)', 'ENTER EMAIL PASSWORD')
    #-----------------------------------------------------------------------------------
    contents = [final_msg]
    #Here we enter the EMAIL-ID'S of people who we want to send this data to
    yag.send('RECEIVERS-MAIL-ID-1', 'Latest Weather Report of last 2hrs', contents)
    yag.send('RECEIVERS-MAIL-ID-2', 'Latest Weather Report of last 2hrs', contents)
    yag.send('RECEIVERS-MAIL-ID-3', 'Latest Weather Report of last 2hrs', contents)
    yag.send('RECEIVERS-MAIL-ID-4', 'Latest Weather Report of last 2hrs', contents)

    #END

if __name__=="__main__":
    runFilesendMail()
