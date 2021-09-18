#!/usr/bin/env python
#coding:utf-8
#version:3.8.5

import os,opencc,sys

_check = ''

def findallfile(path):
    for root, ds, fs in os.walk(path):
        for f in fs:
            fullname = os.path.join(root, f)
            yield fullname

def decide_path(path):
    path_back = ''
    if path.endswith('/'):
        path_back = path
        return path_back
    else:
        path_back = path + '/'
        return path_back

def decide_extension(extension):
    extension_back = ''
    if extension.startswith('.'):
        extension_back = extension
        return extension_back
    else:
        extension_back = '.' + extension
        return extension_back

def check_path_extension(path_original,extension_original):
    path = decide_path(path_original)
    if extension_original == _check:
        extension = extension_original
    else:
        extension = decide_extension(extension_original)
    back = {'path':path, 'extension':extension}
    return back

def read_data(path):
    result = []
    with open(path,'r') as f:
        for line in f:
            result.append(line.strip('\n'))
        return result

def write_data(path,data):
    with open(path,'w') as f:
        for i in data:
            f.write(str(i) + '\n')

def pyopencc(data,opencc_cc):
    result = []
    cc = opencc.OpenCC(opencc_cc)
    for aline in data:
        data_new = cc.convert(aline)
        result.append(data_new)
    return result

def pyopencc_body(path_original,extension_original,opencc_cc):
    path_extension_back = check_path_extension(path_original,extension_original)
    path = str(path_extension_back['path'])
    print('文件夹路径为' + path)
    extension = str(path_extension_back['extension'])
    if extension == _check:
        print('未指定文件后缀')
        for item in findallfile(path):
            print('正在转换：' + item)
            data_old = read_data(item)
            data_new = pyopencc(data_old,opencc_cc)
            write_data(item,data_new)
            print('文件：' + item + ' 转换完成！')
    else:
        print('文件后缀为：' + extension)
        for item in findallfile(path):
            if item.endswith(extension):
                print('正在转换：' + item)
                data_old = read_data(item)
                data_new = pyopencc(data_old,opencc_cc)
                write_data(item,data_new)
                print('文件：' + item + ' 转换完成！')

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