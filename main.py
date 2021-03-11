from internet_speed_twitter_bot import InternetSpeedTwitterBot


# creating bot that will check and tweet post regarding internet speed
new_test = InternetSpeedTwitterBot()
# bot is checking your machine current internet speed
new_test.get_internet_speed()
# bot is logging to twitter account and posting a tweet if the your internet speed is slower then internet service provider promised
new_test.tweet_to_provider()