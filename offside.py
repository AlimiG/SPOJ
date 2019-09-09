#Hemisphere Network is the largest television network in Tumbolia, 
# a small country located east of South America (or south of East America). 
# The most popular sport in Tumbolia, unsurprisingly, is soccer; 
# many games are broadcast every week in Tumbolia.

#Hemisphere Network receives many requests to replay dubious plays
#  usually, these happen when a player is deemed to be offside by the referee. 
# An attacking player is offside if he is nearer to his opponents’ goal line than the second last opponent. 
# A player is not offside if

#    he is level with the second last opponent or

#    he is level with the last two opponents. 

#Through the use of computer graphics technology,
#  Hemisphere Network can take an image of the field
#  and determine the distances of the players to the defending team’s goal line, 
# but they still need a program that, given these distances, decides whether a player is offside.

a ,b = '30', '30'
while True:
    a,b = input().split(' ')
    if int(a) == 0 and int(b)== 0:
        break
    
    
    attack= input().split(' ')
    lisa = [int(x) for x in attack]

    defend = input().split(' ')
    lisd = [int(x) for x in defend]

    lisd.sort()
    if min(lisa) < lisd[1]:
        print('Y')
    else:
        print('N')