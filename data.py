# coding:utf-8
# these data should be in database. available for all
import random

'''
p_ls = {'google':company_instance}
'''
p_ls = {}
c_ls = {}
secret_ls= {}
event_ls = {}

people_name_pool = ['john','stephen','susan']
company_name_pool = ['google','microsoft','tencent']


def getp_ls():
    return p_ls

def getc_ls():
    return c_ls

def getSecret_ls():
    return secret_ls

def getEvent_ls():
    return event_ls

def getRandom_notrepeat_name(pool):
    if len(pool) > 0:
        result =  random.sample(pool,1)[0]
        pool.remove(result)
        return result

