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
import random

import data


class Company():
    # company A , developing industry
    # company B, developed industry
    # company C, decline industry
    def __init__(self,name, type, share_num, price):
        self.name = name
        self.type = type # = 'developing'
        self.share_num_start = share_num
        self.share_num = share_num
        self.share_num_last_time = share_num
        self.demand = 1
        self.price_start = price
        self.price = price # price per share
        self.price_last_time = price

class People():
    def __init__(self, name, type, cash):
        self.type = type # = 'risky'
        self.start_cash = cash # = 100
        self.cash = cash
        self.target_profit = 0.5
        self.stop_loss = 0.5
        self.my_c_ls = {}
        self.name = name # id
        self.risk_preference = 0.5
        self.own_share = {}

    def decide(self):
        # c_rated for companies that has been rated, the sell the one with highest score
        c_rated = {}
        c_to_sell = {}
        result = {}

        for k,c in data.getc_ls().items():
            r = self.rate(c)
            c_rated[k] = r

        for k,c in self.my_c_ls.items():
            r = self.rate(c)
            c_to_sell[k] = r

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
        return result

    def rate(self,c,secret=None, event=None):
        # give a rate score based on market and personal trade stat
        a = self.record(c)
        b = self.history(c)
        score = random.randint(-5,5)
        return score

    def record(self,c):
        # rate according to personal trade history
        # if it reaches the target profit or stop loss point, the score will be high
        profit = self.calcu_profit(c)
        if profit > self.target_profit:
            rates = 10
        elif profit < self.stop_loss:
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

    @classmethod
    def buy(cls, p, c_name, amount):
        actual_result = {'isSuccess':False, 'result':{'name':'google', 'num':5}}
        return actual_result

    @classmethod
    def sell(cls, p, c_name, amount):
        actual_result = {'isSuccess': False, 'result': {'name': 'google', 'num': 5}}
        return actual_result

    @classmethod
    def trade(cls, p, result):
        buy_success = -1
        sell_success = -1

        if 'buy' in result:
            buy_name = result['buy'][0]['name']
            buy_num = result['buy'][0]['num']
            actual_result = cls.buy(p,buy_name,buy_num)

            if actual_result['isSuccess'] == True:
                buy_success = 1
                buy_result = actual_result['result']

            elif actual_result['isSuccess'] == False:
                buy_success = 0

        if 'sell' in result:
            sell_name = result['sell'][0]['name']
            sell_num = result['sell'][0]['num']
            actual_result = cls.sell(p,sell_name, sell_num)

            if actual_result['isSuccess'] == True:
                buy_success = 1
                buy_result = actual_result['result']

            elif actual_result['isSuccess'] == False:
                buy_success = 0

    @classmethod
    def getc_history(cls, c):
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
        # loop num is how many people/companies created
        print('build p')
        for i in range(10):
            name = data.getRandom_notrepeat_name(data.people_name_pool)
            p = People(name,'A',100)
            self.p_ls[name] = p
        print('build c')
        for i in range(3):
            name = data.getRandom_notrepeat_name(data.company_name_pool)
            c = Company(name,'A',10, 5)
            self.c_ls[name] = c

        # self.market = Market(self.p_ls, self.c_ls)
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
        c_ls = data.getc_ls()
        p_ls = data.getp_ls()

        print()

        print('People\n'+40*'=')
        for k, v in p_ls.items():
            # print(k + ' ' + v.cash + ' ' + v.risk_preference)
            print(k, end='\t\t\t')
            print('$%.2f'%v.cash, end='\t\t\t ')
            print('%d%%'%(v.risk_preference*100))

        print()

        print('Company\n' + 40*'=')
        for k, v in c_ls.items():
            print(k, end='\t\t\t')
            print(v.share_num, end='\t\t\t')
            print('$%.2f'%v.price)

        print(40*'*')

        for k, v in p_ls.items():
            print()
            print(k, end='\t\t')
            print('$%.2f'%v.cash)
            print('='*80)
            print('rate')
            temp_c_ls = {}

            for c_name, c_obj in c_ls.items():
                print('\t\t%s'%c_name, end='\t')
                score = v.rate(c_obj)
                print(score, end = '\t')
                temp_c_ls[c_name] = score
            c_max = max(temp_c_ls, key=temp_c_ls.get)
            c_min = min(temp_c_ls, key=temp_c_ls.get)

            print()
            print('-'*80)
            print('share')

            for c_name, c_num in v.own_share.items():
                print('\t\t%s' % c_name, end='\t')
                share = c_num
                print('%.2f'%share, end='\t')

            print()
            print('-'*80)

            # buy
            if temp_c_ls[c_max] > 0:
                c_buy = c_max
                expection_rise = temp_c_ls[c_max]
                buy_percent = expection_rise / 5 * v.risk_preference
                cost = buy_percent * v.start_cash
                if v.cash - cost >= 0:
                    c_buy_obj = data.getc_ls()[c_buy]
                    buy_shares = cost / c_buy_obj.price
                    if c_buy_obj.share_num - buy_shares >=0:
                        v.cash = v.cash - cost
                        v.own_share[c_buy] = buy_shares
                        c_buy_obj.share_num -= buy_shares
                        print('buy \t%s   \t%s/5 * %.2f = %.2f\t\t%.2f\t\t cost %.2f ' % (c_buy, expection_rise, v.risk_preference, buy_percent, buy_shares, cost))
                    else:
                        buy_shares = c_buy_obj.share_num
                        cost = buy_shares * c_buy_obj.price
                        v.cash = v.cash - cost
                        if c_buy in v.own_share:
                            original_share = v.own_share[c_buy]
                            v.own_share[c_buy] = buy_shares+original_share
                            c_buy_obj.share_num -= buy_shares
                        else:
                            v.own_share[c_buy] = buy_shares
                            c_buy_obj.share_num -= buy_shares
                        print('buy %s\t %.2f failed: %s' %(c_buy, buy_shares, 'insuffcient share'))
                else:
                    print('buy %s\t %.2f failed: %s' % ( c_buy, cost, 'insuffcient gold'))
            else:
                print('buy \tnone')

            # sell
            if temp_c_ls[c_min] < 0:
                c_sell = c_min
                expection_fall = temp_c_ls[c_min]
                sell_percent = expection_fall/5
                if c_sell in v.own_share:
                    c_obj = data.getc_ls()[c_sell]
                    sell_shares = v.own_share[c_sell] * sell_percent
                    earn = abs(sell_shares  * c_obj.price)
                    v.cash = v.cash + earn
                    c_obj.share_num += sell_shares
                    print('sell\t%s   \t%.2f' % (c_sell, sell_percent))
                else :
                    print('sell\t%s   \t%.2f\tfailed: %s'%(c_sell, sell_percent, 'insuffcient share'))
            else:
                print('sell\tnone')

        print('\nSummary\n' + 40*'=')
        for k, v in c_ls.items():
            print(k, end='\t\t\t')
            print('%.2f'%v.share_num, end='\t\t\t')
            print('$%.2f'%v.price, end='\t\t\t')
            # -(5 / 5 - 1) * $5 / s = $0 / s
            # compare with last time or orgin pubish price? this is a problem unsolved
            # new_price = -(v.share_num/v.share_num_last_time - 1) * v.price
            v.demand = -(v.share_num/v.share_num_start - 1)
            new_price = -(v.share_num/v.share_num_start - 1) * v.price
            # prevent the price below 0, for test
            if new_price <= 0.1:
                new_price = 0.1
            print('-(%.2f/%.2f-1)* %.2f'%(v.share_num, v.share_num_start, v.price), end='\t\t\t')
            print('newprice %.2f, newshare %.2f demand %.2f'%(new_price, v.share_num, v.demand))
            v.share_num_last_time = v.share_num
            v.price_last_time = v.price
            v.price = new_price


            # result = p.decide()
            # isSuccess = Market.trade(p,result)

if __name__ == '__main__':
    game = Game()
    if game.start_bl:
        game.start()  #init the p_ls and c_ls, people and companies.
        game.run()    # run the game loop
    else:
        game.stop()

