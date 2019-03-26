# -*- coding: utf-8 -*-
"""
@Date: Created on Tue Mar 26 21:50:19 2019
@Author: Haojun Gao
@Description: 
"""

import os
from html.parser import HTMLParser  


class MyHTMLParser(HTMLParser):   
    def __init__(self):   
        HTMLParser.__init__(self)   
        self.href = []
        self.target = []  
    def handle_starttag(self, tag, attrs):   
        #print "Encountered the beginning of a %s tag" % tag   
        if tag == "a":   
            if len(attrs) == 0:   
                pass   
            else:   
                for (variable, value) in attrs:   
                    if variable == "href":   
                        self.href.append(value)
                    if variable == "title":   
                        self.target.append(value)
                        
def get_last_line(inputfile):
    filesize = os.path.getsize(inputfile)
    blocksize = 1024
    dat_file = open(inputfile, 'rb')
    last_line = ""
    if filesize > blocksize:
        maxseekpoint = (filesize // blocksize)
        dat_file.seek((maxseekpoint - 1) * blocksize)
    elif filesize:
        # maxseekpoint = blocksize % filesize
        dat_file.seek(0, 0)
    lines = dat_file.readlines()
    if lines:
        last_line = lines[-1].strip()
    # print "last line : ", last_line
    dat_file.close()
    return last_line
                     
if __name__ == "__main__":   
    html_code = "    <div class=\"mod mod-innerScenic\" data-cs-p=\"\u5185\u90e8\u666f\u70b9\">\n        <div class=\"mhd\">\u5185\u90e8\u666f\u70b9<\/div>\n        <div class=\"mbd\">\n            <ul class=\"clearfix\">\n                    <li>\n        <a href=\"\/poi\/6627770.html\" target=\"_blank\" title=\"\u89d2\u697c\">\n            <img src=\"http:\/\/b3-q.mafengwo.net\/s10\/M00\/55\/F4\/wKgBZ1ms5_aAbfDpAAFQz9xtL5417.jpeg?imageMogr2%2Fthumbnail%2F%21235x150r%2Fgravity%2FCenter%2Fcrop%2F%21235x150%2Fquality%2F100\" width=\"235\" height=\"150\"\/>\n            <span class=\"num num-top\">1<\/span>\n            <div class=\"info\">\n                <h3>\u89d2\u697c<\/h3>\n                <span><em>15696<\/em>\u4eba\u53bb\u8fc7<\/span>\n            <\/div>\n        <\/a>\n    <\/li>\n    <li>\n        <a href=\"\/poi\/21463.html\" target=\"_blank\" title=\"\u5348\u95e8\">\n            <img src=\"http:\/\/b1-q.mafengwo.net\/s11\/M00\/0A\/C4\/wKgBEFtZZZmAWOpuAA6mTlMGjzU180.png?imageMogr2%2Fthumbnail%2F%21235x150r%2Fgravity%2FCenter%2Fcrop%2F%21235x150%2Fquality%2F100\" width=\"235\" height=\"150\"\/>\n            <span class=\"num num-top\">2<\/span>\n            <div class=\"info\">\n                <h3>\u5348\u95e8<\/h3>\n                <span><em>35335<\/em>\u4eba\u53bb\u8fc7<\/span>\n            <\/div>\n        <\/a>\n    <\/li>\n    <li>\n        <a href=\"\/poi\/6627769.html\" target=\"_blank\" title=\"\u6545\u5bab\u535a\u7269\u9662-\u73cd\u5b9d\u9986\">\n            <img src=\"http:\/\/n3-q.mafengwo.net\/s8\/M00\/52\/DB\/wKgBpVUK8yiAKyCGABjlVHOSOPY11.jpeg?imageMogr2%2Fthumbnail%2F%21235x150r%2Fgravity%2FCenter%2Fcrop%2F%21235x150%2Fquality%2F100\" width=\"235\" height=\"150\"\/>\n            <span class=\"num num-top\">3<\/span>\n            <div class=\"info\">\n                <h3>\u6545\u5bab\u535a\u7269\u9662-\u73cd...<\/h3>\n                <span><em>9272<\/em>\u4eba\u53bb\u8fc7<\/span>\n            <\/div>\n        <\/a>\n    <\/li>\n    <li>\n        <a href=\"\/poi\/6627771.html\" target=\"_blank\" title=\"\u6545\u5bab\u4e5d\u9f99\u58c1\">\n            <img src=\"http:\/\/n4-q.mafengwo.net\/s9\/M00\/DE\/8A\/wKgBs1gYgWWAS3QeAAQP53ucRnk00.jpeg?imageMogr2%2Fthumbnail%2F%21235x150r%2Fgravity%2FCenter%2Fcrop%2F%21235x150%2Fquality%2F100\" width=\"235\" height=\"150\"\/>\n            <span class=\"num num-top\">4<\/span>\n            <div class=\"info\">\n                <h3>\u6545\u5bab\u4e5d\u9f99\u58c1<\/h3>\n                <span><em>13088<\/em>\u4eba\u53bb\u8fc7<\/span>\n            <\/div>\n        <\/a>\n    <\/li>\n    <li>\n        <a href=\"\/poi\/6627768.html\" target=\"_blank\" title=\"\u6545\u5bab\u535a\u7269\u9662-\u5fa1\u82b1\u56ed\">\n            <img src=\"http:\/\/b1-q.mafengwo.net\/s6\/M00\/8A\/F8\/wKgB4lKO1IeAaOB4AAT7_xDN9aU71.jpeg?imageMogr2%2Fthumbnail%2F%21235x150r%2Fgravity%2FCenter%2Fcrop%2F%21235x150%2Fquality%2F100\" width=\"235\" height=\"150\"\/>\n            <span class=\"num num-top\">5<\/span>\n            <div class=\"info\">\n                <h3>\u6545\u5bab\u535a\u7269\u9662-\u5fa1...<\/h3>\n                <span><em>10728<\/em>\u4eba\u53bb\u8fc7<\/span>\n            <\/div>\n        <\/a>\n    <\/li>\n    <li>\n        <a href=\"\/poi\/834363.html\" target=\"_blank\" title=\"\u592a\u548c\u6bbf\">\n            <img src=\"http:\/\/b4-q.mafengwo.net\/s11\/M00\/59\/D1\/wKgBEFsCnYGAQKs5ABUaUPT8QeM05.jpeg?imageMogr2%2Fthumbnail%2F%21235x150r%2Fgravity%2FCenter%2Fcrop%2F%21235x150%2Fquality%2F100\" width=\"235\" height=\"150\"\/>\n            <span class=\"num num-top\">6<\/span>\n            <div class=\"info\">\n                <h3>\u592a\u548c\u6bbf<\/h3>\n                <span><em>3321<\/em>\u4eba\u53bb\u8fc7<\/span>\n            <\/div>\n        <\/a>\n    <\/li>\n    <li>\n        <a href=\"\/poi\/6627806.html\" target=\"_blank\" title=\"\u592a\u548c\u95e8\">\n            <img src=\"http:\/\/n2-q.mafengwo.net\/s11\/M00\/D4\/09\/wKgBEFr1UzyASeogAAdqHgxw3Uo23.jpeg?imageMogr2%2Fthumbnail%2F%21235x150r%2Fgravity%2FCenter%2Fcrop%2F%21235x150%2Fquality%2F100\" width=\"235\" height=\"150\"\/>\n            <span class=\"num num-top\">7<\/span>\n            <div class=\"info\">\n                <h3>\u592a\u548c\u95e8<\/h3>\n                <span><em>2167<\/em>\u4eba\u53bb\u8fc7<\/span>\n            <\/div>\n        <\/a>\n    <\/li>\n    <li>\n        <a href=\"\/poi\/849540.html\" target=\"_blank\" title=\"\u4e7e\u6e05\u5bab\">\n            <img src=\"http:\/\/p3-q.mafengwo.net\/s9\/M00\/36\/73\/wKgBs1cCLFaAHVt4ACesywxFAMQ46.jpeg?imageMogr2%2Fthumbnail%2F%21235x150r%2Fgravity%2FCenter%2Fcrop%2F%21235x150%2Fquality%2F100\" width=\"235\" height=\"150\"\/>\n            <span class=\"num num-top\">8<\/span>\n            <div class=\"info\">\n                <h3>\u4e7e\u6e05\u5bab<\/h3>\n                <span><em>1802<\/em>\u4eba\u53bb\u8fc7<\/span>\n            <\/div>\n        <\/a>\n    <\/li>\n\n            <\/ul>\n        <\/div>\n                    <div class=\"more more-subpoi\">\n                <a class=\"btn-subpoi\" data-page=\"1\">\u67e5\u770b\u66f4\u591a<\/a>\n            <\/div>\n            <\/div>\n<style>\n    .mod-innerScenic .more {\n        margin-top: 20px;\n        text-align: center;\n    }\n    .mod-innerScenic .more a {\n        display: inline-block;\n        width: 160px;\n        height: 50px;\n        background-color: #fff;\n        border: 1px solid #fc9c27;\n        line-height: 50px;\n        color: #ff9d00;\n        font-size: 14px;\n        border-radius: 4px;\n        text-align: center;\n    }\n    .mod-innerScenic .num {\n        width: 40px;\n    }\n<\/style>"
    hp = MyHTMLParser()   
    hp.feed(html_code)   
    hp.close()   
    print(hp.href)
    print(hp.target)  
    
    page = 1

    filePath = "./data/list_all.txt"
    if os.access(filePath, os.F_OK):
        print ("[Get_List]Given file path is exist.")
        page_byte = get_last_line(filePath).split()[-1]
        page = int(page_byte.decode(encoding='utf-8'))
        print ("[Get_List]Already spider page :",page)
    else:
        with open(filePath, 'a+',encoding='utf-8') as f:
            f.write("name\ttype_id\tid\tlat\tlng\tpage\n")