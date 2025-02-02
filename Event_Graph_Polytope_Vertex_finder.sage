def with_all_edge_labellings(G,alphabet,edges=None):
    if edges == None:
        edges = G.edges(labels=False,sort=False);
    if edges == []:
        yield G;
    else:
        for H in with_all_edge_labellings(G,alphabet,edges[1:]):
            for a in alphabet:
                H.set_edge_label(edges[0][0],edges[0][1],a);
                yield H;


def is_classical_edge_labelling(G):
    d = {i:False for i in G.vertices(sort=False)}
    c = {i:False for i in G.vertices(sort=False)}

    def search(i):
        d[i]=True
        c[i]=True
        for j in G.neighbor_iterator(i):
            if c[j] and G.edge_label(i,j)==0:
                return False
            else:
                if not d[j] and  G.edge_label(i,j)==1:
                    bit = search(j)
                    if not bit: return False
        return True
                    
    for i in G.vertices(sort=False):
        if not d[i]:
            c = {j:False for j in G.vertices(sort=False)}
            bit = search(i)
            if not bit: return False
    return True

def polytope_vertices(G):
    return [H.edge_labels() for H in with_all_edge_labellings(G,[0,1]) if is_classical_edge_labelling(H)]


def sorted_edge_labels(G):
    def gen():
        for e in G.edges(sort=True,labels=True):
            yield e[2]
    return [l for l in gen()]        

def efficient_polytope_vertices(G,verbose=False):
    v = G.vertices(sort=True)
    N = len(v)
    lam = {i:False for i in range(0,N-1)}
    def update(i,x):
        lam[i]=x
        for j in range(0,i):
            if G.has_edge(v[i],v[j]):
                if lam[j]==x:
                    G.set_edge_label(v[i],v[j],1)
                else:
                    G.set_edge_label(v[i],v[j],0)
    
    def generate(i,nxt):
        if i == N:
            if verbose:
                print (G.edges(sort=True,labels=True))
            yield(sorted_edge_labels(G))
        else:
            for x in range(0,nxt):
                update(i,x)
                for r in generate(i+1,nxt):
                    yield r
            update(i,nxt)
            for r in generate(i+1,nxt+1):
                yield r
    for r in generate(0,0):
        yield r
        

def main(G):
    cnt=0
    for e in efficient_polytope_vertices(G):
        ln = ""
        fst=True
        for r in e:
            if fst:
                fst=False
            else:
                ln=ln+" "
            ln=ln+str(r)
        print(ln)          
        cnt=cnt+1
    print(len(G.edges(sort=False)))
    print(cnt)
    
def classical_polytope(G):
    return Polyhedron (vertices = [v for v in efficient_polytope_vertices(G)], base_ring=QQ)
    
def run_it(G):
    print("The graph has the following edges:")
    print(G.edges(labels=False,sort=False))
    vertices = [v for v in efficient_polytope_vertices(G)] 
    print("\nThe allowed classical assignments are:")
    for v in vertices:
        print(v)

    print("")
    OP = Polyhedron (vertices = vertices)
    print(OP)
    print("\nThe vertices of the polytope are:")
    for v in OP.Vrepresentation():
        print (v)
    print("\nThe facets of the polytope are given by the inequalities:")
    for ineq in OP.Hrepresentation():
        print (ineq)
    print("\nThe inequalities coming from cycles in the cycles are:")
    for ineq in all_cycles_ineqs(G):
        print("Inequality: ("+str(ineq[1:])[1:-1]+") x + "+str(ineq[0])+" >= 0")
    print("\nThe inequalities coming from bounds are:")
    for ineq in all_bounds_ineqs(G):
        print("Inequality: ("+str(ineq[1:])[1:-1]+") x + "+str(ineq[0])+" >= 0")  
    CP = Polyhedron(ieqs = [i for i in all_bounds_ineqs(G)]+[i for i in all_cycles_ineqs(G)])
    print("\nJointly they form the polytope given by inequalities:")
    for ineq in CP.Hrepresentation():
        print (ineq)
    print("\nand whose vertices are:")
    for v in CP.Vrepresentation():
        print(v)   
    print("\n\nSanity check: overlaps polytope contained in \"cycles\" one? "+str(OP <= CP))
    eq = (OP == CP)
    print("\nAre they equal? "+str(eq))
    if not(eq):
        missing = [ineq for ineq in OP.Hrepresentation() if not Polyhedron(ieqs=[ineq]) & CP == CP]
        outside = [ext  for ext  in CP.Vrepresentation() if not Polyhedron(vertices=[ext]) & OP == Polyhedron(vertices=[ext])]
        print("\n\nThe missing inequalities from the overlaps polytope are:")
        for ineq in missing: print(ineq)
        print("\n\nThe vertices of the cycle polytope that are outside the other are:")
        for ext  in outside: print(ext) 
        print("\n\nPretty printing the missing inequalities with the edges of the graph:")
        for ineq in missing: pp_ineq(G,ineq)
        print("\n\nPretty printing the outside vertices with the edges of the graph:")
        for ext in outside:  pp_ext(G,ext)
    print("\n--------------------------------------------------------")
        
def pp_ineq(G,ineq):
    l = list(ineq)
    b = l[0]
    c = l[1:]
    n=0
    s = ""
    for (u,v,_) in G.edge_iterator():
        if not c[n]==0:
            if c[n]<0:
                s=s+"- "
            else:
                s=s+"+ "
            if not abs(c[n])==1:
                s=s+str(c[n])+" "
            s=s+"("+str(u)+"="+str(v)+") "
        n=n+1
    print(s+">="+str(-b))   
    
def pp_ext(G,ext):
    n=0
    s = ""
    for (u,v,_) in G.edge_iterator():
        if not n==0: s=s+", "
        s=s+"("+str(u)+"="+str(v)+") -> "+str(ext[n])
        n=n+1
    print(s+".")


    
def unit_polytope(dim):
    return Polyhedron(vertices=[v for v in Words(alphabet=[0,1], length=dim)])
    
    
    
K2=graphs.CompleteGraph(2)
K4=graphs.CompleteGraph(4)
C4=graphs.CycleGraph(4)
K3=graphs.CompleteGraph(3)
H=graphs.HouseGraph()



polys = [classical_polytope(K3),
         classical_polytope(C4),
         unit_polytope(3) * classical_polytope(K3),
         classical_polytope(C4) * unit_polytope(2),
        (unit_polytope(3) * classical_polytope(K3)) & (classical_polytope(C4) * unit_polytope(2)),
        classical_polytope(H)]

#for p in polys:
#    print(p)
#    for i in p.Hrepresentation():
#        print(i)
#    print()


def glue(g1,g2,v1,w1,v2,w2,verbose=False):
    if verbose:
        g1.show()
        g2.show()
    g = g1.disjoint_union(g2)
    if verbose:
        print("disjoint union")
        g.show()
    g.add_edge((0,v1),(1,v2))
    g.add_edge((0,w1),(1,w2))
    if verbose:
        print("add edges")
        g.show()
    g.contract_edge((0,v1),(1,v2))
    g.contract_edge((0,w1),(1,w2))
    if verbose:
        print("contract")
        g.show()
    return g
    
    
def combinehrep(P1,P2):
    for h in P1.Hrepresentation():
        yield h
    for h in P2.Hrepresentation():
        yield h

        
        
def test_edge_glue(h1,h2,v1,w1,v2,w2,verbose=False):
    if verbose:
        h1.show()
        h2.show()
        print("identifying "+str((v1,w1))+" with "+str((v2,w2)))
    n1 = len(h1.vertices(sort=False))
    n2 = len(h2.vertices(sort=False))
    m1 = len(h1.edges(sort=False))
    m2 = len(h2.edges(sort=False))
    g1 = h1.relabel({v1:100,w1:101},inplace=False)
    g2 = h2.relabel({v2:-2,w2:-1},inplace=False)
    if verbose:
        g1.show()
        g2.show()
    g = glue(g1,g2,100,101,-2,-1,verbose=verbose)
    if verbose:
        g.show()
    P1 = classical_polytope(g1)         
    P2 = classical_polytope(g2)
    P  = classical_polytope(g)
    if verbose:
        [vv for vv in efficient_polytope_vertices(g1,verbose=verbose)]
        [vv for vv in efficient_polytope_vertices(g2,verbose=verbose)]
        [vv for vv in efficient_polytope_vertices(g,verbose=verbose)]

    PP1 = P1 * unit_polytope(m2-1)
    PP2 = unit_polytope(m1-1) * P2
   
    Q = Polyhedron(ieqs=[h for h in combinehrep(PP1,PP2)])
    if verbose:
        print(P1)
        print(P2)
        print(Q)
        print(P)
        print(sorted(Q.Vrepresentation()))
        print(sorted(P.Vrepresentation()))
        print(P==Q)

    return (P==Q)
    

def combine():
    a = unit_polytope(3) * classical_polytope(K3)
    aH = a.Hrepresentation()
    b = classical_polytope(C4) * unit_polytope(2)
    bH = b.Hrepresentation()
    for h in aH:
        yield h
    for h in bH:
        yield h
        
#test_edge_glue(K4,K3,0,1,0,1)

#for g1 in graphs(4):
#    if g1.is_connected():
#        for g2 in graphs(4):
#            if g2.is_connected():
#                for v1 in g1.vertices(sort=False):
#                    for w1 in g1.vertices(sort=False):
#                        if g1.has_edge(v1,w1):
#                            for v2 in g2.vertices(sort=False):
#                                for w2 in g2.vertices(sort=False):
#                                    if g2.has_edge(v2,w2):
#                                        test = test_edge_glue(g1,g2,v1,w1,v2,w2)
#                                        print(test)
#                                        if not test:
#                                            print("FALSE")
#                                            test_edge_glue(g1,g2,v1,w1,v2,w2,verbose=True)
#                                            error("")


def test_bridge(Ga,e,vs1,verbose=False):#,testinho=True):
    vs2 = [v for v in Ga.vertices(sort=False) if (not v==e[0]) and (not v==e[1]) and not (v in vs1)]
    if verbose:
        print("calling test e = "+str(e)+", vs1 = "+str(vs1)+", vs2 = "+str(vs2))
        Ga.show()
    nvs1 = len(vs1)
    nvs  = len(Ga.vertices(sort=False))
    relabelled_order = vs1+[e[0],e[1]]+vs2
    perm = [x-1 for x in Permutation([x+1 for x in relabelled_order]).inverse()]
    G = Ga.relabel(perm,inplace=False)
    if verbose:
        print("after relabelling: vs1 = "+str([x for x in range(0,nvs1)])+", e = "+str((nvs1,nvs1+1))+", vs2 = "+str([x for x in range(nvs1+2,nvs)]))
    G1 = G.copy()
    G2 = G.copy()
    for v in range(0,nvs1):
        G2.delete_vertex(v)
    for v in range(nvs1+2,nvs):
        G1.delete_vertex(v)
    m1 = len(G1.edges(sort=False))
    m2 = len(G2.edges(sort=False))
    if not m1+m2-1 == len(G.edges(sort=False)):
        #print("not good cut")
        return True
    #if testinho and not Ga.has_edge(e):
    #    print("ATTTTT")
    #    test_bridge(Ga,e,vs1,verbose=True,testinho=False)
    #    error()
    if verbose:
        print("RESULTING DECOMPOSITION\n G is:")
        G.show()
        print("G1 = G - vs2 is:")
        G1.show()
        print("G2 = G - vs1 is:")
        G2.show()
    #G1.relabel({e[0]:100,e[1]:101},inplace=True)
    #G2.relabel({e[0]:-2,e[1]:-1},inplace=True)

    
    P  = classical_polytope(G)
    P1 = classical_polytope(G1)
    P2 = classical_polytope(G2)
    PP1 = P1 * unit_polytope(m2-1)
    PP2 = unit_polytope(m1-1) * P2
    Q = PP1 & PP2
    #Q = Polyhedron(ieqs=[h for h in combinehrep(PP1,PP2)])
    if verbose:
        print(P1)
        print(P2)
        print(PP1)
        print(PP2)
        print(Q)
        print(P)
        print(sorted(Q.Vrepresentation()))
        print(sorted(P.Vrepresentation()))
        print(P==Q)
    return(P==Q)

n=7
count=0  
counttests=0
print("There are "+str(len([G for G in graphs(n) if G.is_connected()]))+" graphs to check.")
for G in graphs(n):
    if G.is_connected():
        count+=1
        for e in G.edges(sort=False, labels=False):
                    rem = set([v for v in G.vertices(sort=False) if not v==e[0] and not v==e[1]])
                    #print("e = "+str(e)+", rem = "+ str(rem)+", subsets(rem) = "+str([x for x in subsets(rem)]))
                    for vs1 in subsets(rem):
                        if len(vs1)>0 and len(vs1)<len(rem):
                            #print("vs1 = "+str(vs1))
                            #print("CALLING")
                            pass_test = test_bridge(G,e,vs1,verbose=False)
                            counttests+=1
                            #print(pass_test)
                            if not pass_test:
                                test_bridge(G,e,vs1,verbose=True)
                                error()
        print("checked "+str(count)+" graphs, run "+str(counttests)+" tests.")
        
    

print("FINITO")                                            
