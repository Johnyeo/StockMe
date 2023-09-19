# coding:utf-8
import random
from copy import deepcopy

from pypinyin import pinyin, Style

class caculate():

    def generate_random_number_short_curve(self, curve_index=2):
        # return的结果0-100
        r = random.randint(0, 100)
        rr = r ** curve_index
        result = rr / 100
        return result

    def generate_random_number_tall_curve(self, curve_index=0.5):
        # return 的结果 0 - 100
        r = random.randint(0, 10000)
        rr = r ** curve_index
        result = rr
        return round(result, 2)


class names(object):
    def __init__(self):
        self.company_word_warehouse = '伊利平安美迪华威宁德三一顺丰泰山腾讯东方小鹏'

    def generate_company_name_first(self):
        name = random.sample(self.company_word_warehouse, 2)
        random.randint(0, len(self.company_word_warehouse))
        name = ''.join(name)
        return name

    def generate_company_name_second(self, area):
        # area_ls = ['高科技', '互联网', '新能源', '银行', '农业', '房地产', '医药',
        # '物流', '消费', '能源', '军工', '游戏传媒'， '采矿'，'汽车']

        if area == '高科技':
            name = ['科技', '电子', '智能']

        elif area == '互联网':
            name = ['网络', '信息']

        elif area == '新能源':
            name = ['时代', '科技', '电子']

        elif area == '银行':
            name = ['银行', '财富']

        elif area == '农业':
            name = ['股份', '科技', '集团', '养殖']

        elif area == '房地产':
            name = ['地产', '股份', '集团']

        elif area == '医药':
            name = ['生物', '制药', '健康']

        elif area == '物流':
            name = ['股份', '速递', '物流']

        elif area == '消费':
            name = ['酒业', '啤酒', '集团', '食品']

        elif area == '能源':
            name = ['电力', '石油', '煤矿']

        elif area == '军工':
            name = ['航天', '电子']

        elif area == '游戏传媒':
            name = ['互娱', '娱乐', '传媒', '网络', '信息']

        elif area == '采矿':
            name = ['矿业', '金属', '制造']

        elif area == '汽车':
            name = ['汽车']

        else:
            name = [' ']

        result_name = random.choice(name)
        return result_name

    def generate_company_code(self, name):
        # 取前2个字的序号
        i = self.company_word_warehouse.find(name[0])
        j = self.company_word_warehouse.find(name[1])

        # 4位的代码，目前确保名字仓库不超过100
        if i < 10:
            m = '0' + str(i)
        else:
            m = str(i)

        if j < 10:
            n = '0' + str(j)
        else:
            n = str(j)

        company_code = m + n
        return company_code

    def generate_quick_name(self, name):
        pinyin_str = pinyin(name, style=Style.NORMAL)
        quick_name = ''
        for p in pinyin_str:
            quick_name += p[0]
        quick_name = quick_name.upper()
        return quick_name


class news(object):
    def __init__(self, area_ls, market_obj, start_date):

        self.source = ['证券时报', '小道消息', '内幕消息', '神秘人', '新闻联播']

        # self.current_events = {
        #     'xxcc': {
        #         'desc': '电池科技突破：新电池技术有望让电池能量密度比现在提升一个数量级！',
        #         'effects': [
        #             {'area': '高科技', 'price': 1.1},
        #             {'code': '300750', 'price': 1.5}
        #         ],
        #         'last': 3,
        #         'source': '证券时报'
        #     },
        #
        #     'ccdd': {
        #         'desc': '销量不佳: 苹果公司新手机iphone15销量不及预期',
        #         "effects": [
        #             {'code': 'AAPL', 'price': 0.8}
        #         ],
        #         'last': 2,
        #         'source': '小道消息'
        #     }
        # }

        self.current_events = {}

        self.known_events = {

        }

        self.topics = [
            # 科技突破
            {'type': '特定领域',
             'desc': 'qh大学发现一种新材料，电池能量密度有望突破！',
             'pro_area': ['新能源'],  # 利好行业
             'cons_area': ['能源'],  # 利空行业
             },

            # 随机公司
            {'type': '随机公司',
             'desc': '产品曝出质量问题，正在花钱撤热搜！',
             'is_pro': 0
             },
            {'type': '随机公司',
             'desc': '内部问题重重，高管相继离职！',
             'is_pro': 0
             },
            {'type': '随机公司',
             'desc': '获得一笔战略投资，准备积极扩张！',
             'is_pro': 1
             },

            # 房地产企业
            {'type': '特定领域',
             'desc': '为应对炒房客，政府准备实行更严格的限购政策',
             'cons_area': ['房地产'],
             'group': '房地产调控'
             },
            {'type': '特定领域',
             'desc': '为提振低迷的房地产行业，政府准备放松限购政策',
             'pro_area': ['房地产'],
             'group': '房地产调控'
             },

            # 医药
            {'type': '特定领域',
             'desc': '政府酝酿开启新一轮的医疗集采，据说谈判非常激烈！',
             'cons_area': ['医药'],
             },
            {'type': '特定领域',
             'desc': 'mRNA疫苗重大突破，多种癌症都有望通过疫苗预防！',
             'pro_area': ['医药']
             },

            # 银行
            {'type': '特定领域',
             'desc': '央行准备降准，商业银行的困境有望缓解',
             'pro_area': ['银行']
             },
            {'type': '特定领域',
             'desc': '金融领域的危机比想象的严重，银行业面临洗牌',
             'cons_area': ['银行']
             },

            # 游戏传媒
            {'type': '特定领域',
             'desc': '显卡的制造成本大降，游戏开发者不用为了优化游戏画面而掉头发了！',
             'pro_area': ['游戏传媒']
             },
            {'type': '特定领域',
             'desc': '家长成立联盟，共同起诉游戏公司危害孩子视力！',
             'cons_area': ['游戏传媒']
             },

            # 农业
            {'type': '特定领域', 'desc': '猪肉价快速上涨，可能和近期的粮食危机有关', 'pro_area': ['农业']},
            {'type': '特定领域', 'desc': '一篇新闻稿引起广泛讨论，大多数的转基因食品其实并不安全', 'cons_area': ['农业']},


        ]

        print(area_ls)
        self.area_ls = area_ls
        self.market_obj = market_obj
        self.start_date = start_date
        self.event_num = 0

    def generate_new_event(self):
        event_chance = random.randint(0, 100) / 100
        # 有20%的概率发生事件
        # 每回合加一个事件
        if event_chance < 0.7:
            # 随机选择事件
            topic = random.choice(self.topics)
            # todo 需要检验，有没有矛盾的事件

            if topic['type'] == '特定领域':
                # 生成event_code
                event_code = str(self.event_num)
                event_desc = topic['desc']
                source = random.choice(self.source)
                effect = []
                # 持续时间随机1-4
                last = random.randint(1, 5)
                if 'pro_area' in topic:
                    # 1.1到1.5倍的范围,越小，概率越大，小利好多，大利好少。
                    # effect_intensity = random.randint(11, 15)/10

                    # 下面这个相比上面好些。但最大的就是倍数是2
                    xx = random.randint(1, 10)
                    xxx = xx * xx / 100
                    print('xxx', end=' ')
                    print(xxx)
                    effect_intensity = (1.9 - xxx)

                    for area in topic['pro_area']:
                        effect.append({'area': area, 'price': effect_intensity})

                if 'cons_area' in topic:
                    yy = random.randint(90, 100)
                    effect_intensity = yy * yy / 10000
                    print('yyy', end=' ')
                    print(effect_intensity)

                    for area in topic['cons_area']:
                        effect.append({'area': area, 'price': effect_intensity})

            elif topic['type'] == '随机公司':
                event_code = str(self.event_num)

                source = random.choice(self.source)

                last = random.randint(1, 5)

                # 随机一个company_code
                company_code = random.choice(list(self.market_obj.keys()))

                event_desc = self.market_obj[company_code]['name'] + topic['desc']

                if topic['is_pro'] == 1:
                    xx = random.randint(1, 10)
                    xxx = xx * xx / 100
                    effect_intensity = (1.9 - xxx)

                    effect = [{'code': company_code, 'price': effect_intensity}]

                if topic['is_pro'] == 0:
                    yy = random.randint(90, 100)
                    effect_intensity = yy * yy / 10000
                    effect = [{'code': company_code, 'price': effect_intensity}]
            else:
                pass

            event = {
                event_code: {
                    'effects': effect,
                    'last': last,
                    'source': source,
                    'desc': event_desc
                }

            }
            self.event_num += 1

            self.current_events.update(event)

        print(self.current_events)

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
                    effect_company['price'] *= effect['price']

                elif 'area' in effect:
                    # 某个领域的价格受到影响
                    # 相关度
                    for company_code, company in market.items():
                        # 如果消息行业在公司行业中
                        if effect['area'] in company['area']:

                            new_market[company_code]['price'] *= effect['price']

            # 减去持续时间
            event['last'] -= 1
            if event['last'] < 1:
                to_be_deleted_event.append(event_key)

        # 删除失效的事件
        for e_key in to_be_deleted_event:
            self.current_events.pop(e_key)

        return new_market


class market(object):
    def __init__(self):
        # self.market_obj = {
        #     'AAPL': {'name': '苹果', 'price': 10.2, 'code': 'AAPL', 'quick_name': 'APPLE_PINGGUO',
        #              'area': {'互联网': 1.0, '高科技': 1.5},
        #              'tendency': '-'},
        #     'NVDA': {'name': '英伟达', 'price': 20.2, 'code': 'NVDA', 'quick_name': 'NVIDA_YINGWEIDA',
        #              'area': {'高科技': 2.0},
        #              'tendency': '-'},
        #     '300750': {'name': '宁德时代', 'price': 4.25, 'code': '300750', 'quick_name': 'CATI_NINGDESHIDAI',
        #                'area': {'新能源': 2.0},
        #                'tendency': '-'},
        #     '601398': {'name': '工商银行', 'price': 1.25, 'code': '601398', 'quick_name': 'CBC_GONGSHANG',
        #                'area': {'银行': 1.5, '互联网': -1.5},
        #                'tendency': '-'},
        #     '00700': {'name': '腾讯  ', 'price': 3.25, 'code': '00700', 'quick_name': 'TENCENT_TENGXUN',
        #               'area': {'高科技': 0.2},
        #               'tendency': '-'},
        # }
        self.market_obj = {}

        self.last_round_market_obj = {}

        self.area_ls = ['高科技', '互联网', '新能源', '银行', '农业', '房地产', '医药', '物流', '消费', '能源',
                        '军工', '游戏传媒', '采矿', '汽车']

        self.company_ls = ['AAPL', 'NVDA', '300750', '601398', '00700']

    def generate_company(self):
        # todo 没有考虑重名的情况
        this_name = names()
        area_name = random.choice(self.area_ls)
        # 暂时定 每一个公司只有一个领域
        first_name = this_name.generate_company_name_first()
        second_name = this_name.generate_company_name_second(area_name)
        company_code = this_name.generate_company_code(first_name)
        company_name = first_name + second_name
        quick_name = this_name.generate_quick_name(company_name)

        # 随机一个价格
        price = random.randint(1, 100000) / 1000

        # 行业相关性，正向相关, 相关度越高，对利好和利空越敏感
        # todo：后面还要增加一下，是否有负向相关的因素
        area_relevent = random.randint(0, 100)

        company = {
            company_code: {
                'name': company_name, 'price': price, 'code': company_code, 'quick_name': quick_name,
                'area': {area_name: area_relevent},
                'tendency': '-'
            }
        }

        return company

    def generate_companies(self, n):
        companies = {}
        # 生成n个公司
        for i in range(n):
            company = self.generate_company()
            companies.update(company)
        return companies

    def next_round(self):

        for company_code, company in self.market_obj.items():
            # print(self.last_round_market_obj[company_code])
            # 随机变化金额
            x = random.randint(95, 105)
            xx = x / 100

            self.market_obj[company_code]['price'] *= xx
            last_round_company = self.last_round_market_obj[company_code]

            if last_round_company['price'] - company['price'] > 0.01:
                # 下跌
                company['tendency'] += '↘'

            elif company['price'] - last_round_company['price'] > 0.01:
                # 上涨
                company['tendency'] += '↗'

            else:
                company['tendency'] += '-'

            if len(company['tendency']) > 5:
                company['tendency'] = company['tendency'][1:]

        self.last_round_market_obj = deepcopy(self.market_obj)
        print(self.last_round_market_obj)
        print(self.market_obj)

    def fuzzy_search_company_name(self, target):
        for key, content in self.market_obj.items():
            # print(key)
            # print(target)
            # print(content['quick_name'])
            if target in content['name'] or target in content['quick_name']:
                return key
        return None


class investor(object):
    def __init__(self, fund):
        self.fund = float(fund)
        self.hold_obj = {
            # 'AAPL': {'name': '苹果', 'price': 10.2, 'code': 'AAPL', 'amount': 200, }
        }
        self.cost_base = 10
        self.cost_total = 10
        self.status = {}  # ['starve', 'good', 'ill', 'dead', 'jail']

        self.capital = 0

    def caculate_capital(self, market_obj):
        capital = 0
        for company_code, company in self.hold_obj.items():
            capital += market_obj[company_code]['price'] * company['amount']
        self.capital = capital

    def next_round(self):
        # 消耗资金
        self.cost_total = self.cost_base
        self.fund -= self.cost_total
        if self.fund < 0:
            if 'starve' in self.status:
                self.status['starve'] += 1
                if self.status['starve'] > 3:
                    self.status['dead'] = 1
            else:
                self.status['starve'] = 1
        else:
            if 'starve' in self.status:
                self.status.pop('starve')

    def get_player_baseinfo(self):
        player_base_info = [
            '现金: %.1f, 当前资产价值%.1f, 当前每回合资金消耗%.1f' % (self.fund, self.capital, self.cost_total),
        ]
        if 'starve' in self.status:
            # if self.status['starve'] < 2:
            player_base_info.append('你的现金已经为负，连外卖都点不起了，尽快想办法搞到一些现金！')

        return player_base_info

    def game_tips(self):
        tutorial = [
        ]

        gametips = [
            '每回合都会消耗一定的基础资金，购买食物，支付房租，维持生存',
            '按g可以花钱买消息。但钱不是万能的！',
            # todo '你的人格魅力，决定了你从熟人获得消息的机会',
            '公司的名字通常和他们的主营业务有关联，比如互联网企业通常会叫xx网络',
            '有一些公司的主业非常集中，意味着他们对利好/利空消息更敏感'
        ]
        helptips = [
            'g: 花费金钱调研，获取消息  \tr: 查看已获得的消息',
            't：进行交易',
            'w：查看自己的持仓',
        ]
        tip_i = random.randint(0, len(gametips))
        return tip_i


class company(object):
    pass


class play_console(object):
    def __init__(self):
        self.window_width = 60

        self.style = 'all_buttons'  # all_buttons vs 2_buttons

    def draw_board_fragment(self, company_obj, type):

        print('-' * self.window_width)
        space = (self.window_width - 8) // 4
        print('公司' + '\t' * space + type)
        print('-' * self.window_width)

        for company_code, company in company_obj.items():

            if type == '股价':
                tendency = company['tendency'][-1:]
                # 汉字占空间大，乘以2
                content_len = len(company['name']) * 2 + len(company['code']) \
                              + len('%.3f' % company['price'])

                n = (self.window_width - content_len) // 4

                # tendency留个口看历史趋势
                print('%s(%s)' % (company['name'], company['code']) + '\t' + '- --' * (n - 2) + '\t' + '%.3f' % company[
                    'price'] + '\t' + tendency)
            elif type == '数量':
                content_len = len(company['name']) * 2 + len(company['code']) + len(str(company['amount']))

                n = (self.window_width - content_len) // 4

                print('%s(%s)' % (company['name'], company['code']) + '\t' + '- --' * (n - 2) + '\t' + '%d' % company[
                    'amount'])

        print('-' * self.window_width)

    def draw_console_fragment(self, button1, button2):
        print('_' * self.window_width)
        space = (self.window_width - 14) // 4
        print(button1 + '\t' * space + button2)

    def draw_console_all_button_fragment(self):
        content = [{'name': '持仓', 'btn': 'c'}, {'name': '交易', 'btn': 'j'},
                   {'name': '调研', 'btn': 'd'}, {'name': '市场', 'btn': 's'}, {'name': '消息', 'btn': 'x'},
                   {'name': '下一回合', 'btn': 'n'}]
        c_len = 2 + 1 + 2 + 1 + 2
        # 汉字2，字母1，括号2，分割竖线1
        result = '| '
        current_btn_num = 1
        btn_num_each_line = (self.window_width - 2) // c_len
        for c in content:
            if current_btn_num > btn_num_each_line:
                result += c['name'] + '(' + c['btn'] + ')' + ' | ' + '\n| '
                current_btn_num = 1
            else:
                result += c['name'] + '(' + c['btn'] + ')' + ' | '
                current_btn_num += 1

        print(result)

    def draw_hold_page(self, hold_obj):
        space = (self.window_width - 8) // 8
        print('\t' * space + '【持仓】')
        self.draw_board_fragment(hold_obj, '数量')
        if self.style == '2_buttons':
            self.draw_console_fragment('市场（m）', '交易（t）')
        else:
            self.draw_console_all_button_fragment()

    def draw_market_page(self, market_obj):
        space = (self.window_width - 8) // 8
        print('\t' * space + '【市场】')
        self.draw_board_fragment(market_obj, '股价')
        if self.style == '2_buttons':
            self.draw_console_fragment('持仓（w）', '交易(t)')
        else:
            self.draw_console_all_button_fragment()

    def draw_news_page(self, current_events):
        space = (self.window_width - 8) // 8
        print('\t' * space + '【消息】')
        for event_key, event in current_events.items():
            news_desc = event['desc']
            print(event['source'])
            self.draw_box_multiline(news_desc, '-', '')
        self.draw_console_fragment('通过调研(d)获取消息，花费100', '')

    def draw_game_tip(self, player, start_date):

        content = player.tutorial[start_date]
        self.draw_box_multiline()

    def draw_player_base_info(self, player, market_obj):
        player.caculate_capital(market_obj)
        content = player.get_player_baseinfo()
        for info in content:
            self.draw_box_multiline(info, '', '')

    def draw_top_info_fragment(self, start_date):
        # print('=' * 50)
        top_info = '第%d回合' % (start_date)
        # top_info_n = len(top_info)
        # top_info_tab_n = (48 - top_info_n) // 4
        # top_info_tab_a_n = top_info_tab_n // 2
        # top_info_tab_b_n = top_info_tab_n - top_info_tab_a_n
        # print('|' + '\t' * round(top_info_tab_a_n) + top_info + '\t' * round(top_info_tab_b_n) + '|')
        # print('=' * 50)
        self.draw_box_major(top_info, '=', '|')

    def draw_box_major(self, content, type, side):
        print(type * self.window_width)
        content_n = len(content)
        content_tab_n = (self.window_width - content_n) // 4
        content_tab_a_n = content_tab_n // 2
        content_tab_b_n = content_tab_n - content_tab_a_n
        print(side + '\t' * round(content_tab_a_n) + content + '\t' * round(content_tab_b_n) + side)
        print(type * self.window_width)

    def draw_box_multiline(self, content, up='-', down='-'):
        # todo 根据汉字和其他字符字数计算宽度。

        if len(up) > 0:
            print(up * self.window_width)
        result = ''
        for i in range(0, len(content), self.window_width // 2):
            result += content[i:i + self.window_width // 2] + '\n\t'

        print('\t' + result)
        if len(down) > 0:
            print(down * self.window_width)

    def do_transaction(self, company_code, amount):
        pass

    def do_investigation_market(self, player, this_news, cost):
        # 检查用户余额是否够100
        if player.fund < cost:
            print('你的钱不够！你当前只有%.3f' % player.fund)
        else:
            player.fund -= cost
            is_get_message_success = False

            for current_event_key, current_event in this_news.current_events.items():
                # 获取消息的概率
                success_chance = random.randint(0, 100) / 100
                # 0.1表示有10%的概率获得
                if success_chance < 0.8:
                    # 如果已经收到过的消息，就pass掉
                    if current_event_key in this_news.known_events:
                        pass
                    else:
                        this_news.known_events[current_event_key] = current_event
                        # 显示
                        self.draw_news_page(this_news.known_events)
                        is_get_message_success = True
                        print('你现在的资金：%.2f' % player.fund)
                        break

            if is_get_message_success is False:
                print('没什么消息，一无所获！当前资金：%.2f' % player.fund)

    def do_investigation_company(self, player, this_market, company_code, cost):
        # 检查用户余额是否够100
        if player.fund < cost:
            print('你的钱不够！你当前只有%.3f' % player.fund)
        else:
            player.fund -= cost
            # 获取消息的概率
            success_chance = random.randint(0, 100) / 100
            # 0.1表示有10%的概率获得
            # 调查公司有0.9的成功率
            if success_chance < 0.9:
                # 公司
                if company_code in this_market:
                    company = this_market[company_code]
                    # 获取公司主营
                    area_desc = ''
                    for area_name, area_relevance in company['area'].items():
                        area_desc += area_name + '(相关度：' + str(area_relevance) + '}'

                    # 返回公司信息
                    print('%s 目前的主营领域有: %s' % (company['name'], area_desc))
                    print('你现在的资金：%.2f' % player.fund)
                else:
                    print('没有找到这个公司')

            else:
                print('没什么消息，一无所获！当前资金：%.2f' % player.fund)


    def run(self):
        # 初始化数据
        start_date = 1
        cmd = ''
        player = investor(1000)

        this_market = market()

        this_market.market_obj = this_market.generate_companies(10)

        this_market.last_round_market_obj = deepcopy(this_market.market_obj)

        this_news = news(this_market.area_ls, this_market.market_obj, start_date)

        this_news.generate_new_event()

        while cmd != 'exit':
            if 'dead' in player.status:
                if 'starve' in player.status:
                    print('贫困和饥饿折磨着你，来要房租的房东，发现了你倒地上...')
                    print('GAME OVER')
                cmd = input('是否重新开始？ [Y/N]')
                if cmd.upper() == 'Y':
                    pass
                else:
                    cmd = 'exit'
                continue

            # 顶部 信息板 宽度计算
            self.draw_top_info_fragment(start_date)

            # 个人资产情况
            self.draw_player_base_info(player, this_market.market_obj)

            # 默认展示市场
            self.draw_market_page(this_market.market_obj)
            cmd = input('\n请输入：')

            # 点击n进入下一个回合
            while cmd != 'n':

                # 持仓
                if cmd == 'c':
                    self.draw_hold_page(player.hold_obj)

                # 市场
                elif cmd == 's':
                    self.draw_market_page(this_market.market_obj)

                # 消息面板
                elif cmd == 'x':
                    self.draw_news_page(this_news.known_events)

                # 调研信息
                elif cmd == 'd':
                    # 调查市场  调研公司
                    company_or_market = input('输入公司代码调研公司，输入"enter"调研市场：')

                    # 输入enter nothing
                    if len(company_or_market) == 0:
                        cost = input('花费多少钱进行调研？(默认100一次)')
                        if len(cost) > 0:
                            # 调研市场
                            try:
                                cost = float(cost)
                            except ValueError as e:
                                print('花费金额不是数字？')
                                continue
                        else:
                            cost = 100

                        self.do_investigation_market(player, this_news, cost)

                    else:
                        # 调研公司
                        company_code = company_or_market.upper()

                        # 检查company_code是否在市场里
                        try:
                            market_company = this_market.market_obj[company_code]

                        except KeyError as e:
                            # 没找到，模糊搜索
                            company_code = this_market.fuzzy_search_company_name(company_code)
                            if company_code is not None:
                                c = input('你要找的是%s(%s)吗 (Y/N)' % (
                                    this_market.market_obj[company_code]['name'],
                                    this_market.market_obj[company_code]['code']))
                                if c.upper() == 'Y':
                                    # market_company = this_market.market_obj[company_code]
                                    pass
                                elif c.upper() == 'N':
                                    continue
                                else:
                                    print('')
                                    continue
                            else:
                                print('公司代码不存在')
                                continue

                        cost = input('花费多少钱进行调研？(默认100一次)')
                        if len(cost) > 0:
                            # 调研市场
                            try:
                                cost = float(cost)
                            except ValueError as e:
                                print('花费金额不是数字？')
                                continue
                        else:
                            cost = 100

                        self.do_investigation_company(player, this_market.market_obj, company_code, cost)


                elif cmd == 'j':

                    company_code = input('公司代码：')
                    company_code = company_code.upper()

                    # 检查company_code是否在市场里
                    try:
                        market_company = this_market.market_obj[company_code]
                    except KeyError as e:
                        # 没找到，模糊搜索
                        company_code = this_market.fuzzy_search_company_name(company_code)
                        if company_code is not None:
                            c = input('你要找的是%s(%s)吗 (Y/N)' % (
                                this_market.market_obj[company_code]['name'],
                                this_market.market_obj[company_code]['code']))
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

                cmd = input('\n请输入')

            print('\n')
            start_date += 1

            # 回合结束
            # 更新人员状态
            player.next_round()

            # 消息面影响市场
            this_market.market_obj = this_news.use_event(this_market.market_obj)

            # 已知消息清理掉
            this_news.known_events.clear()

            # 更新市场
            this_market.next_round()

            # 更新事件
            this_news.generate_new_event()


if __name__ == '__main__':
    p = play_console()
    p.run()
