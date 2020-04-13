plt.figure(figsize=(12,12))

start_index = 0

for i in range(25):
    plt.subplot(5, 5, i+1)
    plt.grid(False)
    plt.xticks([])
    plt.yticks([])

    predn = np.argmax(pred[start_index+i])

    gt = y_test[start_index+i]
    col ='g'

    if predn!= gt:
     col = 'r'
    plt.xlabel('i={}, predn={}, gt={}' . format(start_index+1, predn, gt))
    plt.imshow(x_test[start_index+i], cmap='binary')
    plt.show()
