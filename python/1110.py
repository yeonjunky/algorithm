n = int(input())
result = n
count = 1

if(n < 10):
    sip = 0
    il = n

else:
    sip = int(n / 10)
    il = int(n % 10)

n = (il * 10) + (sip + il) % 10

while(n != result):

    sip = int(n / 10)
    il = int(n % 10)

    n = (il * 10) + (sip + il) % 10

    count += 1

print(count)