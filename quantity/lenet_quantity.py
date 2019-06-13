from torch.utils.data import DataLoader
from torchvision import transforms
from torchvision import datasets
import activation_quantizer



    
def main():
    test_dataset = datasets.MNIST(
        root='./data', train=False, transform=transforms.ToTensor())
    test_loader = DataLoader(
        test_dataset, batch_size=1, shuffle=False)
    data_sets = []
    for data_list in test_loader:
        img, _ = data_list
        data_sets.append(img)
    test_lenet = activation_quantizer.Quantity()
    # test_lenet.activation_quantize(data_sets)
    #test_lenet.weight_quantize()
    test_lenet.rewrite_weight()

if __name__ == "__main__":
    main()