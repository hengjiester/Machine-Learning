    critics={'Lisa Rose': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.5,
     'Just My Luck': 3.0, 'Superman Returns': 3.5, 'You, Me and Dupree': 2.5, 
     'The Night Listener': 3.0},
    'Gene Seymour': {'Lady in the Water': 3.0, 'Snakes on a Plane': 3.5, 
     'Just My Luck': 1.5, 'Superman Returns': 5.0, 'The Night Listener': 3.0, 
     'You, Me and Dupree': 3.5}, 
    'Michael Phillips': {'Lady in the Water': 2.5, 'Snakes on a Plane': 3.0,
     'Superman Returns': 3.5, 'The Night Listener': 4.0},
    'Claudia Puig': {'Snakes on a Plane': 3.5, 'Just My Luck': 3.0,
     'The Night Listener': 4.5, 'Superman Returns': 4.0, 
     'You, Me and Dupree': 2.5},
    'Mick LaSalle': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0, 
     'Just My Luck': 2.0, 'Superman Returns': 3.0, 'The Night Listener': 3.0,
     'You, Me and Dupree': 2.0}, 
    'Jack Matthews': {'Lady in the Water': 3.0, 'Snakes on a Plane': 4.0,
     'The Night Listener': 3.0, 'Superman Returns': 5.0, 'You, Me and Dupree': 3.5},
    'Toby': {'Snakes on a Plane':4.5,'You, Me and Dupree':1.0,'Superman Returns':4.0}}
    
    #print(critics['Lisa Rose']['Lady in the Water'])
    #print(critics.keys())
    
    def sim_distance(preItem,p1,p2):
        si,sumValue={},0
        
        for name1 in preItem[p1].keys():
            if name1 in preItem[p2].keys():
                si[name1]=1
        if len(si)==0:
            return 0
        
        for k in si.keys():
            sumValue=sumValue+pow(preItem[p1][k]-preItem[p2][k],2)
        value=1/(1+sumValue)
        return value
            
    
    #simD=sim_distance(critics,'Jack Matthews','Toby')  
    #欧几米德算法
    simD=sim_distance(critics,'Lisa Rose','Gene Seymour')        
    print(simD)
