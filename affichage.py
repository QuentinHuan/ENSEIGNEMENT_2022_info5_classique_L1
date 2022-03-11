def __str__(self):
    s = "" # chaine de caractere qui contient le resultat

    # iteration sur [-1; N+1]² (indices {-1} et {N} pour les bordures)
    for i in range(-1,self.dimension+1):
        for j in range(-1,self.dimension+1):

            # cases appartenant à la bordures verticales --> |
            if(j==-1 or j==self.dimension): 
                s=s+"|"
            else: # plateau et cases de la bordurde verticales
                # cases appartenant à la bordures horizontales --> -
                if(i==-1 or i==self.dimension): 
                    s=s+"-"
                else: # cases appartenant au plateau
                    if(self.plateau[i][j] == 0):
                        s=s+" "
                    if(self.plateau[i][j] == 1):
                        s=s+"#"
                    if(self.plateau[i][j] == 2):
                        s=s+"x"
        s=s+"\n"
    return s
