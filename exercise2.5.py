
sum_temp: int = 0
avg=0

for i in range(5):
    sum_temp:float=float(input("enter temperature: "))
    if 45 < sum_temp < -50:
      break
    sum_temp += avg
else:
    avg = sum_temp / 5
    print(f"average = {avg: .2f}")