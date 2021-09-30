def person_lister(f):
    def inner(people):
        lis=[]
        for i in range(len(people)):
            for j in range(i+1,len(people)):
                if int(people[i][2])>int(people[j][2]):
                    people.insert(i,people[j])
                    del[people[j+1]]
        for i in range(len(people)):
            lis.append(f(people[i]))
            
        return lis
        
    return inner
            
            
        
@person_lister
def name_format(person):
    return ("Mr." if person[3] == 'M' else 'Ms.' )+' '+person[0]+' '+person[1]
people=[input().split() for i in range(int(input()))]
print(*name_format(people),sep='\n')
