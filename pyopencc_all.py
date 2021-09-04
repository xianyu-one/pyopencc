#!/usr/bin/env python
#coding:utf-8
#version:3.8.5

import os,chardet,opencc

_check = ''   #用于比较用户输入是否为空

def findAllFile(base):  #用于遍历文件夹
    for root, ds, fs in os.walk(base):
        for f in fs:
            fullname = os.path.join(root, f)
            yield fullname

def decide_path(path):    #用于检测输入路径是否带有/
    path_back = ''
    if path.endswith('/'):
        path_back = path
        return path_back
    else:
        path_back = path + '/'
        return path_back

def decide_extension(extension):   #用于检测输入文件后缀是否带有.
    extension_back = ''
    if extension.sitemtswith('.'):
        extension_back = extension
        return extension_back
    else:
        extension_back = '.' + extension
        return extension_back

def read_file(path):
    with open(path,'rb') as f:
        back = f.read()
        return(back)

def write_file(path,read_):
    with open(path,'wb+') as f:
        f.write(read_)

def check_path_extension(path_original,extension_original):   #检测用户输入文件夹路径以及文件后缀
    path = decide_path(path_original)
    if extension_original == _check:
        extension = extension_original
    else:
        extension = decide_extension(extension_original)
    back = {'path':path, 'extension':extension}
    return(back)

def pyopencc(path,extension,opencc_cc):
    read_data = read_file(path)
    cc = opencc(opencc_cc)
    data_new = cc.convert(read_data)
    write_file(path,data_new)

def pyopencc_body(path_original,extension_original,opencc_cc):
    path_extension_back = check_path_extension(path_original,extension_original)
    path = str(path_extension_back['path'])      #将path定义为正确的文件路径格式
    print('文件夹路径为：' + path)
    extension = str(path_extension_back['extension'])      #将extension定义为正确的文件后缀格式
    print('文件后缀为：' + extension)
    if extension == _check:
        for item in findAllFile(path):
            pyopencc(path,extension,opencc_cc)
    else:
        for item in findAllFile(path):
            if item.endswith(extension):
                pyopencc(path,extension,opencc_cc)

path_original = input('请输入需要转换的文件夹路径：')
print('如果不需要指定文件后缀请直接回车')
extension_original = input('请输入需要转换的文件的后缀：')
print('''
本脚本支持以下文字间的转换
hk2s: 繁體中文 (香港) -> 简体中文
s2hk: 简体中文 -> 繁體中文 (香港)
s2t: 简体中文 -> 繁體中文
s2tw: 简体中文 -> 繁體中文 (台灣)
s2twp: 简体中文 -> 繁體中文 (台灣, 包含慣用詞轉換)
t2hk: 繁體中文 -> 繁體中文 (香港)
t2s: 繁體中文 -> 简体中文
t2tw: 繁體中文 -> 繁體中文 (台灣)
tw2s: 繁體中文 (台灣) -> 简体中文
tw2sp: 繁體中文 (台灣) -> 简体中文 (包含慣用詞轉換 )
例如想要繁體中文 (香港) -> 简体中文，就输入hk2s
''')
opencc_cc = input('请输入转换的类型')

pyopencc_body(path_original,extension_original,opencc_cc)
print('全部转换完成！')

