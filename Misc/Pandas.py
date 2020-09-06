import  pandas

df1 = pandas.DataFrame([[2,4,6],[10,20,30]])
df2 = pandas.DataFrame([[2,4,6],[10,20,30]],columns=['Price','Age','Value'])
df3 = pandas.DataFrame([[2,4,6],[10,20,30]],columns=['Price','Age','Value']
        , index=['First','Second'])

print(df1)
# print(df2)
# print(df3)

print(df1.mean())
print(df1.mean().mean())
print(df2.Price.mean())