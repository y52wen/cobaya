from cobaya.likelihood import Likelihood

'''
class _H0_prototype(Likelihood):
    # Data type for aggregated chi2 (case sensitive)
    type = "H0"
    # variables from yaml
    H0_mean: float
    H0_std: float
    def initialize(self):
        self.norm = norm(loc=self.H0_mean, scale=self.H0_std)
    def get_requirements(self):
        return {'H0': None}
    def logp(self, **params_values):
        H0_theory = self.provider.get_param("H0")
        return self.norm.logpdf(H0_theory)
'''
class positive_oml(Likelihood):
    
    def get_requirements(self):
        return {'omegal': None}

        
    def initialize(self):
        self.norm = norm(loc=0.0, scale=1.0)
      
    #Note we have to return the log value!!!
    def logp(self, **params_values):
        omegal_theory = self.provider.get_param("omegal")
        if omegal_theory>=0:
            return 0.0
        else:
            return -1e30
         
        
