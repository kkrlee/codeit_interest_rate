INTEREST_RATE = 0.12
APARTMENT_PRICE = 1100000000

year = 1988
amount = 50000000

while year < 2016:
    amount = amount * (1 + INTEREST_RATE)
    year += 1

if amount > APARTMENT_PRICE:
    print("%d원 차이로 동일 아저씨의 말씀이 맞습니다." % (amount - APARTMENT_PRICE))
elif amount < APARTMENT_PRICE:
    print("%d원 차이로 미란 아주머니의 말씀이 맞습니다." % (APARTMENT_PRICE - amount))
else:
    print("Same")
