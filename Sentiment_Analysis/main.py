from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
import time
import json
from textblob import TextBlob
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style

ckey = 'dl2C9UePjgyidl6SkQPTEtzaK'
csecret = 'KS9B1FZnfDVvyz8hbDMGV0rMYqDDcLue78atS8iG0CO4iUEfkR'
atoken = '827462914579787777-OM3bcV4tu7WuKrKjnIVUNhQ4NEOOJ5T'
asecret = 'upBgJ3LPF4siuwrsTpxYoEsgOPT2QPaA6jw4jsoTkTaOF'


class listener(StreamListener):
    def on_data(self, data):
        all_data = json.loads(data)
        tweet = all_data['text']
        print tweet
        sentence = TextBlob(tweet)
        print sentence.sentiment
        time.sleep(3)

        if sentence.subjectivity * 100 >= 80:
            output = open('twitter-out.csv', 'a')
            output.write(str(sentence.polarity))
            output.write('\n')
            output.close()

        return True

    def on_error(self, status):
        print status


auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

twitterStream = Stream(auth, listener())
twitterStream.filter(track=['happy'])


# class animate():
#
#
#     style.use('ggplot')
#
# fig = plt.figure()
# ax1 = fig.add_subplot(1, 1, 1)
#
# def animate(i):
#     data = open('twitter-out.txt', 'r').read()
#     lines = data.split('\n')
#
#     x_array = []
#     y_array = []
#
#     x = 0
#     y = 0
#
#     for l, value in lines:
#         x += 1
#         if value >= 0.5 in l:
#             y += 1
#
#         elif value < 0.5 in l:
#             y -= 1
#
#     x_array.append(x)
#     y_array.append(y)
#
#     ax1.clear()
#     ax1.plot(x_array, y_array)
#
#
# ani = animation.FuncAnimation(fig, animate, interval=1000)
# plt.show()
