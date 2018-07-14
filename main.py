# coding:utf-8
'''
The elementary idea of this game is:
People will decide which one company's stock they will buy, based on information of two types: the secret and event.
1. people would rate every company, and buy the one with the highest score
2. after people buy it, the company's stock price would change.
3. people will re-caculate and rate the company a new score.
4. secret will influence the rate score. and secret is leaked slowly . so people will make different decisions.
5. event is known by everybody and gives a strong, trendcy influence on all companies or people.

'''
import data


class Company():
    # company A , developing industry
    # company B, developed industry
    # company C, decline industry
    def __init__(self,name, type, active):
        self.name = name
        self.type = type # = 'developing'
        self.active = active # = 10

class People():
    def __init__(self, name, type, cash):
        self.type = type # = 'risky'
        self.cash = cash # = 100
        self.target_profit = 0.5
        self.stop_loss = 0.5
        self.my_c_ls = []
        self.name = name # id

    def decide(self):
        # c_rated for companies that has been rated, the sell the one with highest score
        c_rated = {}
        c_to_sell = {}
        result = {}

        for c in data.c_ls:
            r = self.rate(c)
            c_rated[c.name] = r
        for c in self.my_c_ls:
            r = self.rate(c)
            c_to_sell[c.name] = r

        if len(c_to_sell) >0:
            best_to_sell = max(c_to_sell,key=c_to_sell.get) # return the max value key
            sell_num = 10
            result['sell'] = [{'name':best_to_sell, 'num':sell_num}]

        if len(c_rated) > 0:
            best_to_buy = max(c_rated, key=c_rated.get)  # return the max value key
            buy_num = 10
            result['buy'] = [{'name':best_to_buy, 'num':buy_num}]


        # 1 decision only buy / sell 1 stock , num fixed to be 10
        '''
        result = {
            'buy':[
            {
                'name':best_to_buy,
                'num':buy_num
            }],
            'sell':[
            {
                'name':best_to_sell,
                'num':sell_num
            }
            ]
        }
        '''
        print(result)
        return result

    def rate(self,c,secret=None, event=None):
        # give a rate score based on market and personal trade stat
        a = self.record(c)
        b = self.history(c)
        return a+b;

    def record(self,c):
        # rate according to personal trade history
        # if it reaches the target profit or stop loss point, the score will be high
        profit = self.calcu_profit(c)
        if profit >= self.target_profit:
            rates = 10
        elif profit <= self.stop_loss:
            rates = 10
        else:
            rates = 1
        return rates

    def history(self, c):
        # rate according to market trade history
        return  10

    def calcu_profit(self,c):
        # calculate how much profit this stock earned since been bought
        return 0.5


# people and company are driven by event and secret
class Secret():
    def __init__(self, id, type, endAt, expose):
        self.type = type # = 'cTypeChange'
        self.endAt = endAt # = '2018/1/10'
        self.expose = expose # = 0.1

class Event():
    def __init__(self, id, type, endAt):
        self.type = type #= 'tradeWar'
        self.endAt = endAt #= '2018/1/10'


# market is a place to calculate the result
class Market():
    def __init__(self, all_people, all_company):
        pass

    def buy(self, p, c, amount):
        pass

    def sell(self, p, c, amount):
        pass

    def caculate_c_price(self, c):
        pass

    def trade(self, p, result):
        pass


# Game thread
class Game():
    def __init__(self):
        self.start_pt = input('press "A" to start:')
        self.p_ls = data.getp_ls()
        self.c_ls = data.getc_ls()
        self.secret_ls = data.getSecret_ls()
        self.event_ls = data.getEvent_ls()

        if self.start_pt == 'a':
            self.start_bl = True
        print("game init")

    def start(self):
        for i in range(3):
            p = People(1,'A',100)
            self.p_ls.append(p)
            print ('build p --- ')

        for i in range(3):
            c = Company('Google','A',100)
            self.c_ls.append(c)
            print('build c ---')

        self.market = Market(self.p_ls, self.c_ls)
        print("start ----")

    def run(self):
        print("run ----")
        while self.start_bl == True:
            if input('next?') == 'a':
                self.next()
            else:
                self.start_bl = False
                self.stop()

    def stop(self):
        print("Bye")
        self.start_bl = False

    def next(self):
        for p in self.p_ls:
            result = p.decide()
            self.market.trade(p, result)
            print ('x ---- ')


if __name__ == '__main__':
    game = Game()
    if game.start_bl:
        game.start()  #init the p_ls and c_ls, people and companies.
        game.run()    # run the game loop
    else:
        game.stop()

