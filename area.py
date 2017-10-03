
#Anything you write here will be ignored

'''
This program is to find the biggest number of 3
'''

yin = int(input())
yang = int(input())
if yin>yang:
    print("Yin")
elif yang>yin:
        print("Yang")
else:
        print("Harmony and peace")

android_sales = int(input())
iOS_sales = int(input())
WinPhone_sales = int(input())

if android_sales > iOS_sales:
    if android_sales > WinPhone_sales:
        print("Android")
    elif android_sales == WinPhone_sales:
        print("Android and Windows Phone")
elif android_sales == iOS_sales:
    if iOS_sales > WinPhone_sales:
        print("Android and iOS")
    elif WinPhone_sales > iOS_sales:
        print("Windows Phone")
else:
    if iOS_sales > WinPhone_sales:
        print("iOS")
    elif iOS_sales == WinPhone_sales:
        print("iOS and Windows Phone")
    else:
        print("All equal")
