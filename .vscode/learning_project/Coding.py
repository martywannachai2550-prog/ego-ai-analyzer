import random
import time
def slow_print(text, delay=1):
    print(text)
    time.sleep(delay)

#---------------------------------------------------------------#
statschecking = ("คุณต้องการดูค่าพลังของคุณหรือไม่\n"
    "(y)ใช่\n"
    "(n)ไม่")
#---------------------------------------------------------------#
slimes = {
    "สไลม์ขนาดเล็ก": {
        "hp": 10,
        "atk": 3,
        "gold": 4
    },
    "สไลม์ขนาดกลาง": {
        "hp": 20,
        "atk": 5,
        "gold": 8
    },
    "สไลม์ขนาดใหญ่": {
        "hp": 35,
        "atk": 8,
        "gold": 15
    }
}

#---------------------------------------------------------------#
races = ["มนุษย์","เอลฟ์"]
race = random.choice(races)
#---------------------------------------------------------------#

print ("=== Welcome to UWTC ===")
Name = input("กรุณาตั้งชื่อของคุณ >>> ")

print("")

print(f"ชื่อของคุณคือ {Name}")
print(f"เผ่าของคุณคือ {race}")
if race == "มนุษย์":
    Hp = 100
    Atk = 55
    Mana = 25
    Gold = 0
    print(f"ค่าพลังชีวิต : {Hp}")
    print(f"ค่าพลังโจมตี : {Atk}")
    print(f"ค่าพลังเวทย์ : {Mana}")
    
else:
    Hp = 75
    Atk = 255
    Mana = 75
    Gold = 0
    print(f"ค่าพลังชีวิต : {Hp}")
    print(f"ค่าพลังโจมตี : {Atk}")
    print(f"ค่าพลังเวทย์ : {Mana}")
    
stats = {
    "hp": Hp,
    "atk": Atk,
    "mana": Mana,
    "gold": Gold
}

#---------------------------------------------------------------#
print()
slow_print("คุณต้องการไปที่ไหนเป็นที่แรก(กรุณาตอบเป็นหมายเลข(1หรือ2หรือ3))",1)
slow_print("1.)ร้านช่างตีดาบ",0.5)
slow_print("2.)ร้านค้าชุดเกราะ",0.5)
slow_print("3.)โบสถ์ศักดิ์สิทธิ์",0.5)
place = input("คุณต้องการที่จะเดินทางไปที่ไหน(1/2/3): ")

#---------------------------------------------------------------#

print("")

if place == "1":
    slow_print("คุณมาถึงร้านช่างตีดาบแล้ว",1)
    slow_print("**คุณได้รับดาบหินคม**",0.5)
    print("ค่าพลังโจมตี +3")
    stats["atk"] += 3
    
elif place == "2":
    slow_print("คุณมาถึงร้านชุดเกราะแล้ว",1)
    slow_print("**คุณได้รับชุดเกราะหนังบาง**",0.5)
    print("ค่าพลังชีวิต +5")
    stats["hp"] += 5
    
elif place == "3":
    slow_print("คุณมาถึงโบสถ์แล้ว",1)
    slow_print("**คุณได้สวดภาวนาต่อพระผู้เป็นเจ้า**",0.5)
    slow_print("คุณรู้สึกได้ถึงพลังที่เอ่อล้นออกมา",0.5)
    print("ค่าพลังเวทย์ +10")
    stats["mana"] += 10
    
else:
    slow_print("คุณได้เดินทางเข้าสู่สัทธิมืด",1.5)
    slow_print("**คุณยังไม่สามารถรับพลังแห่งความมืดไหว**",0.5)
    slow_print("**คุณเอ้อระเบิดตาย**",0.25)
    print("GAME OVER")
    exit()
    
#---------------------------------------------------------------#

print("")

print(statschecking)
tc = input("คุณต้องการดูหรือไม่(y/n): ")
if tc == "y":
    for key in stats:
        print(key.upper(),":", stats[key])
else:
    print("-")
    
print("")

slow_print("คุณได้เดินทางไปยังกิลด์",1)
print("กรุณาเลือกเควสแรกของคุณ")
quest1 = ("1.)จัดการสไลม์ 5 ตัว\n"
    "2.)ทำความสะอาดโบสถ์สักดิ์สิทธิ์")
print(quest1)

Aquest = input("กรุณาเลือกเควสของคุณ: ")

print("")
        
#---------------------------------------------------------------#

def battle(monster_name, monster, stats):
    monster_hp = monster["hp"]

    slow_print(f"**คุณได้เจอกับ {monster_name}**", 0.5)

    action = input("คุณต้องการสู้หรือไม่(y/n): ")
    if action != "y":
        print("คุณหลบหนี")
        return False

    while monster_hp > 0 and stats["hp"] > 0:
        choice = input("โจมตี(f) เช็คค่าพลัง(c) หนี(r): ")

        if choice == "f":
            monster_hp -= stats["atk"]
            slow_print(f"คุณโจมตี {monster_name}", 0.3)
            slow_print("",0.5)

            if monster_hp <= 0:
                slow_print("คุณชนะ!", 0.4)
                stats["gold"] += monster["gold"]
                slow_print("",0.5)
                return True

            stats["hp"] -= monster["atk"]
            stats["hp"] = max(0, stats["hp"])
            slow_print(f"HP คุณเหลือ {stats['hp']}", 0.3)

        elif choice == "c":
            print(f"มอน HP: {monster_hp} | ATK: {monster['atk']}")
            if monster_name == "สไลม์ขนาดเล็ก":
                slow_print("เป็นสไลม์ที่น่ารักดีนะว่าไหม?",1)
            if monster_name == "สไลม์ขนาดกลาง":
                slow_print("มันดูเหมือนว่ามันจะอยากต่อสู้กับคุณอยู่นะ!",1)
            if monster_name == "สไลม์ขนาดใหญ่":
                slow_print("มันเกิดจากสไลม์หลายสิบตัวหลอมรวมเข้าด้วยกัน!!!",1)
            print("")    

        elif choice == "r":
            print("คุณหนีออกจากการต่อสู้")
            slow_print("",0.5)
            return False

    return False


#---------------------------------------------------------------#
        
if Aquest == "1":
    slime_kill = 0
    while slime_kill < 5 and stats["hp"] > 0:
        monster_name = random.choice(list(slimes.keys()))
        monster = slimes[monster_name]
        if battle(monster_name, monster, stats):
            slime_kill += 1
            print(f"กำจัดสไลม์แล้ว {slime_kill}/5 ตัว")

    if slime_kill == 5:
        print("เควสสำเร็จ!")
        stats["gold"] += 50
        slow_print("",0.5)
        
#---------------------------------------------------------------#

if Aquest == "2":
    print("**คุณได้เดินทางไปยังโบสถ์ศักดิ์สิทธิ์**")
    print("**คุณได้ทำความสะอาดโบสถ์ศักดิ์สิทธิ็จนสะอาด**")
    print("**จิตใจของคุณถูกชะล้างจากความเหนื่อยล้า**")
    print("Hp ของคุณได้รับการฟื้นฟู")
    stats["hp"] += 25
    
#---------------------------------------------------------------#
