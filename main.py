"""
- นำตัวแปร list_person ที่คุณสร้างเสร็จแล้ว มาทำการวนซ้ำโดยใช้ For Loop 
- โดยคุณสามารถใช้ range(len(list_person)) 
- เพื่อให้ข้อมูลในการวนซ้ำเป็นตัวเลขตั้งแต่ 0 จนถึงตำแหน่งสุดท้ายของ list_person ได้ 
- และตัวแปรที่คุณสร้างขึ้นเช่น i จะกลายเป็นตัวเลขที่ใช้ในการเข้าถึงตำแหน่ง index ของข้องมูลนั้นๆ ให้มา 
- print ออกมาเป็น key name ตัวอย่าง
"""

# นำข้อมูลจากโจทย์ก่อนหน้ามาหรือสร้างใหม่เองก็ได้ ตัวอย่างเช่น
ist_person = list_person = [
    {"name": "Andy", "age": 19, "year_born": 2004, "nick_name": "andy"},
    {"name": "Jane", "age": 24, "year_born": 1999, "nick_name": "jane"},
    {"name": "Ten", "age": 18, "year_born": 2004, "nick_name": "ten"},
    {"name": "Eve", "age": 21, "year_born": 2002, "nick_name": "eve"},
    {"name": "Charlie", "age": 18, "year_born": 2005, "nick_name": "charlie"},
    {"name": "Grace", "age": 25, "year_born": 1998, "nick_name": "grace"},
    {"name": "Deam", "age": 19, "year_born": 2004, "nick_name": "deam"},
    {"name": "Jame", "age": 18, "year_born": 2005, "nick_name": "jame"},
    {"name": "Mark", "age": 19, "year_born": 2004, "nick_name": "mark"},
    {"name": "Ohm", "age": 19, "year_born": 2004, "nick_name": "ohm"}]

# ทำการ for loop ตัวอย่างเช่น
for i in range(len(list_person)):
    print(list_person[i]["name"])
   
    

