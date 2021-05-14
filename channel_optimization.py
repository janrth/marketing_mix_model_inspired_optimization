import numpy as np
import scipy


class optimization(object):
    '''Using scipy.optimize.minimize to optimize sales based on a
    main constraint. Code is in line with p3p8 accoring to pycodestyle.'''
    def __init__(self,
                 beta_sales_a,
                 beta_sales_b,
                 beta_sales_c,
                 beta_sales_d,
                 beta_contacts_a,
                 beta_contacts_b,
                 beta_contacts_c,
                 beta_contacts_d,
                 initial,
                 customer,
                 alpha):
        self.beta_sales_a = beta_sales_a
        self.beta_sales_b = beta_sales_b
        self.beta_sales_c = beta_sales_c
        self.beta_sales_d = beta_sales_d
        self.beta_contacts_a = beta_contacts_a
        self.beta_contacts_b = beta_contacts_b
        self.beta_contacts_c = beta_contacts_c
        self.beta_contacts_d = beta_contacts_d
        self.initial = initial
        self.customer = customer
        self.alpha = alpha

    def n_cust(self, x):
        '''Predict number of customers using channel information'''
        cust = (
               self.beta_contacts_a*x[0] +
               self.beta_contacts_b*x[1] +
               self.beta_contacts_c*x[2] +
               self.beta_contacts_d*x[3]
        )
        return cust

    def objective_function(self, x):
        '''Applying negative exponential function to predict sales
        based on the pre-trained coefficients, to incorporate
        diminishing marginal returns.'''
        y = -(
            self.alpha*(1-np.exp(-self.beta_sales_a*x[0])) +
            self.alpha*(1-np.exp(-self.beta_sales_b*x[1])) +
            self.alpha*(1-np.exp(-self.beta_sales_c*x[2])) +
            self.alpha*(1-np.exp(-self.beta_sales_d*x[3]))
        )
        return y

    def main_constraint(self, x):
        '''The constraint keeps the number of customers per person
        equal, therefore optimizing the relative amount of sales
        per fixed customers.'''
        cust = self.customer
        return (self.beta_contacts_a*x[0]+self.beta_contacts_b*x[1] +
                self.beta_contacts_c*x[2]+self.beta_contacts_d*x[3])-cust

    def optimizer(self, x):
        '''Define equality or inequality'''
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
