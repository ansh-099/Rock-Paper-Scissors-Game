# Rock-Paper-Scissors-Game

Play Rock Paper Scissors with your computer. The project contains Convolutional neural network, which detects user's hand and gesture and calculate's result accordingly.

<img width="1440" alt="Screenshot 2020-08-09 at 10 34 21 PM" src="https://user-images.githubusercontent.com/35291991/89737689-93521f80-da90-11ea-9976-4455b2cf69f5.png">


## Get Started Now

* Add new Entry. These entries contains images of hand gesture for rock, paper, scissors which will further be used for training.
```sh
$ python3 new_entry.py
```

* Create dataset(.csv) with those images uploaded
```sh
$ jupyter nbconvert --to python3 create_dataset.ipynb
```

* Train model
```sh
$ jupyter nbconvert --to python3 train_model.ipynb
```

* Play game
```sh
$ python3 play_game.py
```
</br>
Find documentation -  [OpenCV](https://docs.opencv.org/master/d9/df8/tutorial_root.html)
