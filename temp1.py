import torch

data = range(100, 200)

random_sampler = torch.utils.data.RandomSampler(data)
cnt = 0
for index in random_sampler:
    print("index:{},data:{}".format(index,data[index]))
    cnt += 1
print(cnt)
