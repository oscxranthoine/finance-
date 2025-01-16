import numpy as np
from scipy.stats import norm


# Fonction de pricing pour options call/put
def pricing(s,k,t,r,vol,type="c")->float:
    d1= (np.log(s/k)+(r+(vol**2)/2)*t)/(vol*np.sqrt(t))
    d2=d1-(vol*np.sqrt(t))

# Calcul pour une option call
    if type == "c":
        price=( norm.cdf(d1)*s)-(norm.cdf(d2)*k*np.exp(-r*t))
        return price 
        
     # Calcul pour une option put
    elif type == "p":
        price=k(np.exp(-r*t))*norm.cdf(-d2)-(s*norm.cdf(-d1))
        return price 
    
    # Gérer les erreurs pour un type invalide
    else:
        raise ValueError("option_type doit être 'call' ou 'put'")

# Partie principale du programme
# Paramètres de l'option
if __name__ == "__main__":
    s=100 # Prix du sous-jacent
    k=102 # Strike price (prix d'exercice)
    t=0.66 # Temps à l'échéance en années
    r=0.05 # Taux d'intérêt sans risque
    vol=0.07 # Volatilité annuelle
    price  = pricing(s,k,t,r,vol)   # Calcul du prix de l'option call
    print(f'call price :{price:.2f}')
   




