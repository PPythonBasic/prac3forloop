- นำตัวแปร list_person ที่คุณสร้างเสร็จแล้ว มาทำการวนซ้ำโดยใช้ For Loop 
- โดยคุณสามารถใช้ range(len(list_person)) 
- เพื่อให้ข้อมูลในการวนซ้ำเป็นตัวเลขตั้งแต่ 0 จนถึงตำแหน่งสุดท้ายของ list_person ได้ 
- และตัวแปรที่คุณสร้างขึ้นเช่น i จะกลายเป็นตัวเลขที่ใช้ในการเข้าถึงตำแหน่ง index ของข้องมูลนั้นๆ ให้มา 
- print ออกมาเป็น key name ตัวอย่าง

```py
list_data = [{"name":"a"},{"name":"b"}]
for i in range(len(list_data)):
    print(list_data[i]["name"])
```

- คุณก็จะได้ ข้อมูลใน key name ออกมาแล้วลองปรับเอาไปใช้กับโค้ดคุณ
