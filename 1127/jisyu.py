import calcFunc

from cryptography.fernet import Fernet
import base64

#1
amount = input("売買価格を入力してください")
fee = calcFunc.feeCalc(float(amount))
print("仲介手数料は" +  str(fee) + "万円です")


#2
# 暗号化・復号化対象のメッセージ
data = "日本語で書かれた秘密のメッセージ".encode("utf-8")

# インスタンス生成
key = Fernet.generate_key()
f = Fernet(key)

# 暗号化されたデータ
token = f.encrypt(data)
print(token)

# 復号化されたデータ
data_decrypt = f.decrypt(token)
print(f.decrypt(token).decode("utf-8"))