import math
import sys

def protein(file):
    chain_a = []  
    chain_b = []  
    with open(file) as fd:
        for line in fd:
            if line[0:6] == "ATOM  " and  line[13:15]=="CA":
                if line[21] == "A":
                    chain_a.append({
                        "id": int(line[23:26]), 
                        "coord": (float(line[30:38]), float(line[38:46]), float(line[46:54])), 
                        "amino":line[17:20]})
                elif line[21] == "B":
                    chain_b.append({
                        "id": int(line[23:26]), 
                        "coord": (float(line[30:38]), float(line[38:46]), float(line[46:54])), 
                        "amino":line[17:20]})
    return chain_a, chain_b
    
    
                
def distance(coord1, coord2):
    x1, y1, z1 = coord1
    x2, y2, z2 = coord2
    return math.sqrt(pow(x1 - x2, 2) + pow(y1 - y2, 2) + pow(z1 - z2, 2))

def find_distance_pair(chain_a,d,s):
    pair = []
    for cid1 in chain_a:
        for cid2 in chain_a:
            if distance(cid1['coord'], cid2['coord']) <= d and abs(cid1['id']-cid2['id'])>=s:
                if((cid2,cid1) in pair):
                    continue
                else:
                    pair.append((cid1,cid2))
                
    return pair

def print_pair(fileName,chain_a,chain_b,d,s):
    pair=find_distance_pair(chain_a,d,s)
    pair2=find_distance_pair(chain_b,d,s)
    #Output for 3r0a.pdb with D=5.0 and S=40:
    #Chain: A --> TRP(39) - LYS(86) : 4.848 Angstroms
    print("Output for " +fileName+" with D="+str(d)+" and S="+str(s)+":")
    for each_pair in pair:
        get_distance=distance(each_pair[0]['coord'],each_pair[1]['coord'])
        print("Chain: A --> "+each_pair[0]['amino']+"("+str(each_pair[0]['id'])+ ") - " +each_pair[1]['amino']+"("+str(each_pair[1]['id'])+") : "+str(get_distance) +" Angstroms")
    for each_pair in pair2:
        get_distance2=distance(each_pair[0]['coord'],each_pair[1]['coord'])
        print("Chain: B --> "+each_pair[0]['amino']+"("+str(each_pair[0]['id'])+ ") - " +each_pair[1]['amino']+"("+str(each_pair[1]['id'])+") : "+str(get_distance2) +" Angstroms")    
 


#python hw3 <pdb file name> <D> <S>
if __name__ == "__main__":
#def main(argv):
    #files = sys.argv[1]
    #d=sys.argv[2]
    #s=sys.argv[3]
    my_file=['3r0a.pdb','6k97.pdb']
    for file in my_file:
        chain_a,chain_b=protein(file)
        print_pair("3r0a.pdb",chain_a,chain_b,5.0,40)
    #for file in files:
    #    chain_a, chain_b = protein(file)
    #    print_pair("3r0a.pdb",chain_a,chain_b,d,s)
        
        

        