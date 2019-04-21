visitedList = []
queue = []
weight = [0]
cost=[0]
edgeheu = [("Sirajgonj","Tangail",188),("Sirajgonj","Mymenshing",171),("Sirajgonj","Natore",361),("Sirajgonj","Bogra",375),
          ("Manikganj","Gazipur",95),("Manikganj","Tangail",188),("Manikganj","Faridpur",237),("Magura","Rajbari",239),
          ("Magura","Faridpur",237),("Khustia","Rajbari",239),("Khustia","Natore",361),("Gazipur","Tangail",188),
          ("Gazipur","Dhaka",0),("Gazipur","Manikganj",155),("Faaridpur","Manikganj",155),("Faridpur","Magura",236),
          ("Natore","Naogaon",369),("Natore","Kushtia",324),("Natore","Sirajgonj",248),("Bogra","Sirajgonj",248),
          ("Bogra","Naogaon",369),("Rajbari","Magura",236),("Rajbari","Kushtia",324),("Tangail","Gazipur",95),
          ("Tangail","Manikganj",155),("Tangail","Sirajgonj",248),("Dhaka","Gazipur",95),("Dhaka","Narshindi",105),
          ("Dhaka","Mymenshing",171),("Dhaka","Narayangonj",85),("Mymenshing","Sirajgonj",248),("Mymenshing","Dhaka",0),
          ("Narayangonj","Dhaka",0),("Narshindi","Dhaka",0),("Narshindi","Kishorgonj",155),("Kishorgonj","Narshindi",105),
          ("Kishorgonj","Netrokona",204),("Netrokona","Kishorgonj",155),("Netrokona","Sunamgonj",245),
          ("Sunamgonj","Netrokona",204),("Naogaon","Bogra",375),("Naogaon","Natore",361)]

edgewei = [("Sirajgonj","Tangail",75),("Sirajgonj","Mymenshing",94),("Sirajgonj","Natore",135),("Sirajgonj","Bogra",146),
          ("Manikganj","Gazipur",133),("Manikganj","Tangail",141),("Manikganj","Faridpur",115),("Magura","Rajbari",65),
          ("Magura","Faridpur",70),("Khustia","Rajbari",106),("Khustia","Natore",113),("Gazipur","Tangail",92),
          ("Gazipur","Dhaka",96),("Gazipur","Manikganj",133),("Faaridpur","Manikganj",115),("Faridpur","Magura",70),
          ("Natore","Naogaon",70),("Natore","Kushtia",113),("Natore","Sirajgonj",135),("Bogra","Sirajgonj",146),
          ("Bogra","Naogaon",66),("Rajbari","Magura",65),("Rajbari","Kushtia",106),("Tangail","Gazipur",92),
          ("Tangail","Manikganj",141),("Tangail","Sirajgonj",75),("Dhaka","Gazipur",96),("Dhaka","Narshindi",80),
          ("Dhaka","Mymenshing",206),("Dhaka","Narayangonj",90),("Mymenshing","Sirajgonj",94),("Mymenshing","Dhaka",206),
          ("Narayangonj","Dhaka",90),("Narshindi","Dhaka",80),("Narshindi","Kishorgonj",110),
          ("Kishorgonj","Narshindi",110),("Kishorgonj","Netrokona",210),("Netrokona","Kishorgonj",210),
          ("Netrokona","Sunamgonj",145),("Sunamgonj","Netrokona",145),("Naogaon","Bogra",66),
          ("Naogaon","Natore",70)]



def queue_child(currentNode,currentWieght):
    for current in range(0,len(edgeheu),1):
        if currentNode in edgeheu[current][0]:
            queue.append(edgeheu[current][1])
            weight.append(edgeheu[current][2]+edgewei[current][2])
    current_cost =cost.pop()
    cost.append(current_cost+currentWieght)

    a = weight.index(min(weight))
    temp_node = queue[a]
    #temp_width = weight[a]

    queue.remove(temp_node)
    queue.append(temp_node)

    #weight sort resverse to remove the minimum value from queue
    weight.sort(reverse=True)




def a_star():
    queue.append("Natore")
    while queue:
        currentNode = queue.pop()
        currentWieght = weight.pop()
        if not currentNode in visitedList:
            queue_child(currentNode,currentWieght)
            if currentNode == "Dhaka":
                visitedList.append(currentNode)

                break
            else:
                visitedList.append(currentNode)
                print(visitedList)
                print(cost[0])

    return visitedList

a_star()
print(visitedList)
print(cost[0])