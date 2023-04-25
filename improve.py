from snn import experiment

eps_l=[0,1]

std=0.9
batch_size=64
learning_rate=0.05
n_epochs=20
print_process=True


eps_r=[]

for eps in eps_l:
    eps_r.append(experiment(std=std, net=4, batch_size=batch_size, learning_rate=learning_rate, n_epochs=n_epochs,print_process=print_process,eps=eps))

print("Experiment for eps: batch_size = {}, learning_rate = {}, n_epochs = {}".format(batch_size,learning_rate,n_epochs))
print(eps_r)