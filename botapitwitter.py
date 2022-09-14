import tweepy
import time
import array as arr
import random


api = tweepy.Client(
    consumer_key='suaKEYaqui',
    consumer_secret='suaKEYaqui',
    access_token='suaKEYaqui',
    access_token_secret='suaKEYaqui'
)

nomes_linguagens_program = ['Java', 'PHP', 'C', 'C++','C#', 'Python', 'Kotlin', 'Swift', 'Go', 'Ruby', 'Rust', 'R' ,'Assembly', 'F#', 'Cobol', 'Pascal', 'Fortran', 'Perl', 'Scala']

nome_01 = random.choice(nomes_linguagens_program)

running = True
seconds = 1
end = 0
while(running):
    seconds -=1
    if(seconds <= end):
        try:
            nome_01 = random.choice(nomes_linguagens_program)
            tweet = api.create_tweet(text=nome_01)
            print(tweet)
            time.sleep(5)
                
        except Exception as error:
            print("Erro:", error)
