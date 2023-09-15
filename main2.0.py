# coding:utf-8
import random

class news(object):
    def __init__(self):
        self.current_events = {
            '科技突破':{
                'desc':'电池科技突破：新电池技术有望让电池能量密度比现在提升一个数量级！',
                'code':'tech',
                'effects':[
                    {'area':'高科技', 'price':1.1 },
                    {'code':'300750', 'price':1.5}
                ],
                'last': 3,
                'source': '证券时报'
                          },

            '财报不佳':{
                'desc':'销量不佳: 苹果公司新手机iphone15销量不及预期',
                'code':'bad_finance_report',
                "effects":[
                    {'code':'AAPL', 'price': 0.8}
                ],
                'last': 2,
                'source':'小道消息'
            }
        }

        self.known_events= {

        }

        self.area_ls = ['高科技', '互联网', '新能源', '银行', '农业', '基建']
        self.company_ls = ['AAPL', 'NVDA', '300750', '601398', '00700']
        self.source = ['证券时报', '小道消息', '内幕消息', '神秘人', '新闻联播']


    def generate_new_event(self):
        pass

    def use_event(self, market):
        new_market = market

        to_be_deleted_event = []
        for event_key, event in self.current_events.items():
            effects = event['effects']

            for effect in effects:
                # 判断effect类型
                if 'code' in effect:
                    # 某个公司的价格受到影响
                    effect_company = new_market[effect['code']]
                    effect_company['price'] += effect['price']


                elif 'area' in effect:
                    # 某个领域的价格受到影响
                    for company_code, company in market.items():
                        if effect['area'] in company['area'] :
                            new_market[company_code]['price'] *= effect['price']

                # print(effect)

            # 减去持续时间
            event['last'] -= 1
            if event['last']< 1:
                to_be_deleted_event.append(event_key)

            # print(new_market)

        # 删除失效的事件
        for e_key in to_be_deleted_event:
            self.current_events.pop(e_key)

        return new_market

    def game_tips(self):
        gametips = [
            '消息不是花了钱就一定能获得的！',
            '你的人格魅力，决定了你从熟人获得消息的机会',
        ]
        tip_i = random.randint(0, len(gametips))
        return tip_i


class market(object):
    def __init__(self):
        self.market_obj = {
            'AAPL': {'name': '苹果', 'price': 10.2, 'code': 'AAPL', 'name_en':'APPLE_PINGGUO', 'area':['互联网', '高科技'], 'tendency':'-'},
            'NVDA':{'name': '英伟达', 'price': 20.2, 'code': 'NVDA', 'name_en':'NVIDA_YINGWEIDA', 'area':['高科技'], 'tendency':'-'},
            '300750':{'name': '宁德时代', 'price': 4.25, 'code': '300750', 'name_en':'CATI_NINGDESHIDAI', 'area':['新能源'], 'tendency':'-'},
            '601398':{'name': '工商银行', 'price': 1.25, 'code': '601398','name_en':'CBC_GONGSHANG', 'area':['银行'], 'tendency':'-'},
            '00700':{'name': '腾讯  ', 'price': 3.25, 'code': '00700','name_en':'TENCENT_TENGXUN', 'area':['高科技'], 'tendency':'-'},
        }

        self.last_round_market_obj = {}

    def next_round(self):

        for company_code, company in self.market_obj.items():
            # 随机变化金额
            x = random.randint(90, 110)
            xx = x/100
            company['price'] *= xx
            last_round_company = self.last_round_market_obj[company_code]
            print(last_round_company)

            if last_round_company['price'] > company['price']:
                # 下跌
                company['tendency'] += '↘'
            elif last_round_company['price'] < company['price']:
                # 上涨
                company['tendency'] += '↗'
            else:
                company['tendency'] += '-'


    def fuzzy_search_company_name(self,target):
        for key, content in self.market_obj.items():
            # print(key)
            # print(target)
            # print(content['name_en'])
            if target in content['name'] or target in content['name_en']:
                return key
        return None


class investor(object):
    def __init__(self, fund):
        self.fund = float(fund)
        self.hold_obj = {
            'AAPL': {'name': '苹果', 'price': 10.2, 'code': 'AAPL', 'amount': 200, }
        }

class company(object):
    pass

class play_console(object):
    # def __init__(self):
    #     self.market_obj = {
    #         'AAPL': {'name': '苹果', 'price': 10.2, 'code': 'AAPL'},
    #         'NVDA': {'name': '英伟达', 'price': 20.2, 'code': 'NVDA'},
    #         '300750': {'name': '宁德时代', 'price': 4.25, 'code': '300750'},
    #         '601398': {'name': '工商银行', 'price': 1.25, 'code': '601398'}
    #     }
    #     self.hold_obj = {
    #         'AAPL': {'name': '苹果', 'price': 10.2, 'code': 'AAPL', 'amount': 200, }
    #     }

    def draw_board_fragment(self, company_obj, type):
        print('-'*50)
        print('公司' + '\t'*10 + type)
        print('-'*50)
        # 对齐股价
        n = 0

        for company_code, company in company_obj.items():
            #对齐股价
            if len(company['name']) >= 4:
                n = -1

            if type == '股价':
                # tendency留个口看历史趋势
                tendency = company['tendency'][-1:]
                print('%s(%s)'%(company['name'], company['code']) + '\t' * (8+n) + '%.3f'%company['price'] + '\t' + tendency)
            elif type == '数量':
                print('%s(%s)' % (company['name'], company['code']) + '\t' * (8+n) + '%d' % company['amount'])


    def draw_console_fragment(self, button1, button2):
        print('_'*50)
        print(button1 + '\t'*8 + button2)


    def draw_hold_page(self, hold_obj):
        print('\t' * 5 + '【持仓】')
        self.draw_board_fragment(hold_obj, '数量')
        self.draw_console_fragment('市场（m）', '交易（t）')

    def draw_market_page(self, market_obj):
        print('\t' * 5 + '【市场】')
        self.draw_board_fragment(market_obj, '股价')
        self.draw_console_fragment('持仓（w）', '交易(t)')

    def draw_news_page(self, current_events):
        print('\t' * 5 + '【消息】')
        for event_key, event in current_events.items():
            news_desc = event['desc']
            print(event['source'])
            self.draw_box_multiline(news_desc, '-', '')
        self.draw_console_fragment('获取(g)消息，花费100', '')


    def draw_top_info_fragment(self, start_date, fund):
        # print('=' * 50)
        top_info = '第%d回合 现金: %.3f' % (start_date, fund)
        # top_info_n = len(top_info)
        # top_info_tab_n = (48 - top_info_n) // 4
        # top_info_tab_a_n = top_info_tab_n // 2
        # top_info_tab_b_n = top_info_tab_n - top_info_tab_a_n
        # print('|' + '\t' * round(top_info_tab_a_n) + top_info + '\t' * round(top_info_tab_b_n) + '|')
        # print('=' * 50)
        self.draw_box_major(top_info, '=', '|')


    def draw_box_major(self, content, type, side):
        print(type*50)
        content_n = len(content)
        content_tab_n = (48 - content_n) // 4
        content_tab_a_n = content_tab_n // 2
        content_tab_b_n = content_tab_n - content_tab_a_n
        print(side + '\t' * round(content_tab_a_n) + content + '\t' * round(content_tab_b_n) + side)
        print(type * 50)

    def draw_box_multiline(self,content, up='-', down='-'):
        print(up*50)
        result = ''
        for i in range(0, len(content), 25):
            result += content[i:i + 25] + '\n\t'

        print('\t'+result)
        print(down*50)


    def do_transaction(self, company_code, amount):
        pass

    def run(self):
        # 初始化数据
        start_date = 1
        cmd = ''
        player = investor(1000)
        this_market = market()
        this_news = news()

        while cmd != 'exit':
            # 顶部 信息板 宽度计算
            self.draw_top_info_fragment(start_date, player.fund)

            # 默认展示市场
            self.draw_market_page(this_market.market_obj)
            cmd = input('\n输入字母操作：')

            # 点击n进入下一个回合
            while cmd != 'n':

                # 持仓
                if cmd == 'w':
                    self.draw_hold_page(player.hold_obj)

                # 市场
                elif cmd == 'm':
                    self.draw_market_page(this_market.market_obj)

                # 消息面板
                elif cmd == 'r':
                    self.draw_news_page(this_news.known_events)

                # 调研信息
                elif cmd == 'g':
                    is_get_news = input('确定花费100搜集消息？(Y/N)')
                    if is_get_news.upper() == 'Y':
                        # 检查用户余额是否够100
                        if player.fund < 100:
                            print('你的钱不够！你当前只有%.3f' % player.fund)
                        else:
                            player.fund += -100.0
                            is_get_message_success = False

                            for current_event_key, current_event in this_news.current_events.items():
                                # 获取消息的概率
                                success_chance = random.randint(0, 100)/100
                                # 0.1表示有90%的概率获得
                                if success_chance > 0.5:
                                    # 如果已经收到过的消息，就pass掉
                                    if current_event_key in this_news.known_events:
                                        pass
                                    else:
                                        this_news.known_events[current_event_key] = current_event
                                        # 显示
                                        self.draw_news_page(this_news.known_events)
                                        is_get_message_success = True
                                        print('你现在的资金：%.2f'%player.fund)
                                        break

                            if is_get_message_success is False:
                                print('没什么消息，一无所获！当前资金：%.2f' % player.fund)

                    elif is_get_news.upper() == 'N':
                        pass

                    else:
                        pass

                elif cmd == 't':

                    company_code = input('公司代码：')
                    company_code = company_code.upper()

                    # 检查company_code是否在市场里
                    try:
                        market_company = this_market.market_obj[company_code]
                    except KeyError as e:
                        # 没找到，模糊搜索
                        company_code = this_market.fuzzy_search_company_name(company_code)
                        if company_code is not None:
                            c = input('你要找的是%s(%s)吗 (Y/N)'%(this_market.market_obj[company_code]['name'], this_market.market_obj[company_code]['code']))
                            if c.upper() == 'Y':
                                market_company = this_market.market_obj[company_code]
                            elif c.upper() == 'N':
                                continue
                            else:
                                print('公司代码不存在')
                                continue
                        else:
                            print('公司代码不存在')
                            continue

                    try:
                        amount = float(input('买入正整数，卖出负整数：'))
                    except ValueError as e:
                        print('买入/卖出不是数字')
                        continue


                    transaction_money = amount * market_company['price']
                    # 判断买入还是卖出，卖出要判断是否超卖，买入要判断是否现金够
                    # 买入需要在库存里增加，卖出需要减少
                    # 首次买入要建仓，卖光之后要清仓
                    # 买入
                    if transaction_money > 0:
                        # 金额充足
                        if player.fund >= transaction_money:
                            # 建仓还是加仓
                            if company_code in player.hold_obj:
                                # 加仓
                                player.hold_obj[company_code]['amount'] += amount

                                player.fund = player.fund - transaction_money
                                print('交易成功，交易金额%.3f, 现金总量%.3f' % (transaction_money, player.fund))

                            else:
                                # 建仓
                                player.hold_obj[company_code] = {'name': market_company['name'],
                                                               'price': market_company['price'], 'amount': amount,
                                                               'code': company_code}

                                player.fund = player.fund - transaction_money
                                print('交易成功，已经建仓，交易金额%.3f, 现金总量%.3f' % (transaction_money, player.fund))

                        else:
                            print('金额不足')

                    # 卖出
                    elif transaction_money < 0:
                        if company_code in player.hold_obj:
                            # 库存充足
                            if int(player.hold_obj[company_code]['amount']) + int(amount) > 0:
                                player.hold_obj[company_code]['amount'] += amount

                                player.fund = player.fund - transaction_money
                                print('交易成功，交易金额%.3f, 现金总量%.3f' % (transaction_money, player.fund))

                            # 清仓
                            elif int(player.hold_obj[company_code]['amount']) + int(amount) == 0:
                                player.hold_obj.pop(company_code)

                                player.fund = player.fund - transaction_money
                                print('交易成功，已经清仓，交易金额%.3f, 现金总量%.3f' % (transaction_money, player.fund))

                            else:
                                print('股票数不够')
                        else:
                            print('没有持仓此股票')
                    else:
                        pass

                cmd = input('\n输入字母操作：')

            print('\n')
            start_date += 1

            # 把市场行情记录下来
            this_market.last_round_market_obj = this_market.market_obj

            # 消息面影响市场
            this_market.market_obj = this_news.use_event(this_market.market_obj)

            # 消息清理掉
            this_news.known_events.clear()

            # 更新市场
            this_market.next_round()
            
            print('--*--'*30)




if __name__ == '__main__':
    p = play_console()
    p.run()
