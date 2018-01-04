# coding: UTF-8

#comment

print ("Hello, World!")
print ("Bye!")
print ("あいうえお")

#文字連結
print ("Hello!", "Satou")

#改行
print ("Tomato is \"very\" delicious")
print ("The browser displays an \
error message")

print ("Python" + "です")
print ("-" * 40)
print (len("こんにちは"))
print (len("こんにちは".encode("UTF-8")))

#数値連結
print ("Year" + str(2000))
print (u"円周率" + str(3.14159))

#文字配列
jpstr = "表計算"
print (jpstr[0])
print (jpstr[1])
print (jpstr[2])

alpstr = "ABCDE"
print ("対象文字列 " + alpstr)
print ("[1:3]  " + alpstr[1:3])
print ("[1:-1] " + alpstr[1:-1])
print ("[1:]   " + alpstr[1:])
print ("[:2]   " + alpstr[:2])

#数値
print(5e3)
print(8.0/3)
print(8/3)
print(1+2*3)
print((1+2)*3)

a="14"
print(int(a))
print(int(a, 10))
print(int(a, 16))
b=14.5
print(int(b))

#変数
identify = "Katou"
print (u"識別子:" + identify)
identify = 200
print (identify)
print (u"識別子:" + str(identify) )

a=100
b=a
a=200
print(b)

list1 = [1, 2]
list2 = list1
list1.append(3)
print (list1)
print (list2)

#条件文
amari = 10 % 3
if amari != 0:
	print (u"割り切れませんでした")
	print (u"余りは", str(amari), u"です")

#比較演算子
#別のオブジェクト
list1 = [1, 2, 3]
list2 = [1, 2, 3]
print ("list1 == list2", list1 == list2)
print ("list1 is list2", list1 is list2)
#同一オブジェクト
list1 = [1, 2, 3]
list2 = list1
print ("list1 == list2", list1 == list2)
print ("list1 is list2", list1 is list2)

old = 25
if old < 10 and (old < 30):
  print ("old is under 10")
elif old < 20:
  print ("old is between 10 and 20")
elif old <30:
  print ("old is between 20 and 30")
else:
	print ("old is over 30")
	
	
#リスト
list1 = ["A", "B", "C", "D"]
print (len(list1), ":", list1)
list1[1:3] = ["b", "B", "C", "C", "d"]
print (len(list1), ":", list1)
list1.append("e")
print (len(list1), ":", list1)
list1.extend(["E", "F"])
print (len(list1), ":", list1)
list1 += ["G", "H"]
print (len(list1), ":", list1)
list1.remove("C")
print (len(list1), ":", list1)

if "C" in list1:
 print ("C exists. Count:" + str(list1.count("C")))

#ディクショナリ
dict = {"yamada":75, "endou":82, "tanaka":92}
print (dict["yamada"])
print (dict)
dict["yamada"] = 78
print (dict)
print (u"要素数=" + str(len(dict)) )

#繰り返し
#while文
num = 0
while num < 3:
  print ("num = " + str(num))
  num += 1
else: #breakのときに実行されないだけ？
  print (u"繰り返しが終了した時の最後の値") 
  print ("num = " + str(num))
print ("End")

#for文
for num in [4, 3, 12]:
  print ("num = " + str(num))
else:
  print (u"繰り返しが終了した時の最後の値") 
  print ("num = " + str(num))
print ("End")

print (range(10) )
print (range(1, 11))
print (range(1, 11, 2))
list2 = range(1, 11, 2)
print (list2)

sum = 0
for num in range(1, 11):
  sum += num;
print ("sum = " + str(sum))

#関数
def add(x, y):
    ans = x + y
    return ans

n = add(3, 5)
print (n)

#クラス
class TestClass:
	"""example class"""				# 三重クォートによるコメント
	
	useCount = 0
	
	def __init__(self):				# コンストラクタ
		self.name = ""
		TestClass.useCount += 1
	def __del__(self):				# デストラクタ
		TestClass.useCount -= 1
		
	def getName(self):				# getName()メソッド
		return self.name
	def setName(self, name):		# setName()メソッド
		self.name = name


a1 = TestClass()					# クラスのインスタンスを生成
a1.setName("Tanaka")				# setName()メソッドをコール
print (a1.getName() )				# getName()メソッドをコール

a2 = TestClass()
a2.name = "Suzuki"
print (a2.name)						#変数でアクセス
print (a2.getName() )				#メソッドでアクセス

print (TestClass.useCount)			#クラス変数にアクセス
