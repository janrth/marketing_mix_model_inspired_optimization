import numpy as np
import scipy


class optimization(object):
    '''
    Using scipy.optimize.minimize to optimize sales based on a
    main constraint. Code is in line with p3p8 accoring to pycodestyle.
    '''
    def __init__(self,
                 beta_sales,
                 beta_contacts,
                 initial,
                 customer,
                 alpha):
        self.beta_sales = beta_sales
        self.beta_contacts = beta_contacts
        self.initial = initial
        self.customer = customer
        self.alpha = alpha

    def n_cust(self, x):
        '''
        Predict number of customers using channel information.
        '''
        cust = (
               self.beta_contacts[0]*x[0] +
               self.beta_contacts[1]*x[1] +
               self.beta_contacts[2]*x[2] +
               self.beta_contacts[3]*x[3]
        )
        return cust

    def objective_function(self, x):
        '''
        Applying negative exponential function to predict sales
        based on the pre-trained coefficients, to incorporate
        diminishing marginal returns.
        '''
        y = -(
            self.alpha*(1-np.exp(-self.beta_sales[0]*x[0])) +
            self.alpha*(1-np.exp(-self.beta_sales[1]*x[1])) +
            self.alpha*(1-np.exp(-self.beta_sales[2]*x[2])) +
            self.alpha*(1-np.exp(-self.beta_sales[3]*x[3]))
        )
        return y

    def main_constraint(self, x):
        '''
        The constraint keeps the number of customers per person
        equal, therefore optimizing the relative amount of sales
        per fixed customers.
        '''
        cust = self.customer
        return (self.beta_contacts[0]*x[0]+self.beta_contacts[1]*x[1] +
                self.beta_contacts[2]*x[2]+self.beta_contacts[3]*x[3])-cust

    def optimizer(self, x):
        '''
        Define equality or inequality.
        '''
        con_main = {'type': 'eq', 'fun': self.main_constraint}
        cons = [con_main]
        bnds = [(0, 1), (0, 1), (0, 1), (0, 1)]
        solver = scipy.optimize.minimize(self.objective_function,
                                         self.initial,
                                         method='SLSQP',
                                         bounds=bnds,
                                         constraints=cons)
        solver
        return solver
