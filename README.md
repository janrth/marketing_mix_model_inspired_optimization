We have the possibility to connect to customers through 4 different channels, which I named a,b,c and d for simplicity reasons. 
Each sales person has a fixed numnber of customers and we would like to maximize the expected sales, while keeping the number of customers
constant. We develope an objective function and a main constraint based on a linear regression. Additionally we assume diminishing marginal returns,
which are implemented in a naive way applying a negative exponential function with a abitrary set alpha of 0.6:
-`f(x) = alpha*(1-exp(-coefficient*x))`
-'f(x) = alpha*(1-exp(-coefficient*x))'


