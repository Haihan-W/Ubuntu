#This code did not use any library package, e.g. numpy or scipy, instead it uses basic numerical formula to get linear regression

def compute_error_for_line_given_points(b,m,points):
	#initialize at 0
	totalError=0
	#for every point
        For i in range(0, len(points)):
	    #get x value
	    x=points[i,0]
	    #get y value
	    y=points[i,1]
            #get the square diff, add to total error
            totalError += (y-(m*x+b)) ** 2
	#get average: 
        return totalError/float(len(points))

#THEORY for the following two gradient functions:     gradient= slope, gradient_descent= find the minimun error in error func, that is the bottom of the error bowl(error function is like an bowl, in terms of both b and m(3D plot)), in terms of both b and m-- that is partial derivative of error in terms of both b and m will be converged to 0-- For one point in error function map, partial deriv of error in terms of b is negative→ means b is smaller than b value at the bottom of error bowl ; same thing apply for m. So everytime when we !minus! partial deriv in terms of b&m from current value of b&m (update value), we can make new b&m closer to error bowl.

def gradient_descent_runner(points, starting_b, starting_m, learning_rate, num_iteration):
	#starting b and m
	b=starting_b
	m=starting_m

    #gradient descent
    for i in range(num_iteration):
	#update b and m with the new more accurate b and m by performing this gradient step
        [b,m]= step_gradient(b,m,array(points), learning_rate)
    return [b,m]


def step_gradient(b_current, m_current, points, learningRate):
	#starting points for gradients (partial derivative)
	b_gradient=0
	m_gradient=0
        N=float(len(points))
	for i in range(0, len(points)):
		x= points[i,0]
		y=points[i,1]
		#direction with respect to b and m
		#computing partial derivatives of our error function
		b_gradient += -(2/N) *(y-((m_current * x) + b_current))
		m_gradient += (2/N) * x *(y-((m_current*x)+b_current))
		#update b and m using partial deriv
		new_b=b_current- (learning_rate * b_gradient)
		new _m=m_current - (learning_rate * m_gradient)
		#NOTE: LEARNING RATE determine how fast we want to converge)
	return [new_b,new_m]         

def run():
	#step 1- collect data
	points = genfromtxt(‘data.csv’,delimiter=’,’)
    	#step 2- define hyperparameters
	learning_rate=0.0001  #How fast should model converge, too small, take long time to converge; too big-- too fast, error func might not decrease, it might not converge

	#y=mx+b
	initial_b=0
	initial_m=0
	num_iterations = 1000

	#step 3-- training model
	Print ‘starting gradient descent at b={0}, m={1}, error = {2}’.format(initial_b,initial_m,compute_error_for_line_given_points(initial_b,initial_m,points))
	[b,m] = gradient_descent_runner(points, initial_b, initial_m, learning_rate, num_iterations)
	Print ‘ending point at b={1}, m={2}, error={3}’.format(num_iteration, b,m, compute_error_for_line_given_points(b,m,points))
                                                                                                                                               



If __name__ == ‘__main__’:  #main function
       run()



