from snn import experiment

n_epochs=20
std_l=[0.3,0.6,0.9]
net_l = range(4)
batch_size_l=[64,128,256,512,1024]
learning_rate_l=[0.005,0.01, 0.05, 0.1, 0.5]
print_process=False  #是否打印训练过程

#net
net_r=[]
batch_size=64
learning_rate=0.05
for std in std_l:
    for net in net_l:
        net_r.append(experiment(std=std, net=net, batch_size=batch_size, learning_rate=learning_rate, n_epochs=n_epochs,print_process=print_process))
print("Experiment for net: batch_size = {}, learning_rate = {}, n_epochs = {}".format(batch_size,learning_rate,n_epochs))
print(net_r)

#batch_size
batch_size_r=[]
net=0
learning_rate=0.05
for std in std_l:
    for batch_size in batch_size_l:
        batch_size_r.append(experiment(std=std, net=net, batch_size=batch_size, learning_rate=learning_rate, n_epochs=n_epochs,print_process=print_process))
print("Experiment for batch_size: net = {}, learning_rate = {}, n_epochs = {}".format(net,learning_rate,n_epochs))
print(batch_size_r)

#learning_rate
learning_rate_r=[]
net=0
batch_size=64
for std in std_l:
    for learning_rate in learning_rate_l:
        learning_rate_r.append(experiment(std=std, net=net, batch_size=batch_size, learning_rate=learning_rate, n_epochs=n_epochs,print_process=print_process))
print("Experiment for learning_rate: net = {}, batch_size = {}, n_epochs = {}".format(net,batch_size,n_epochs))
print(learning_rate_r)