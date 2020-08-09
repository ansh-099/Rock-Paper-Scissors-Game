# Rock-Paper-Scissors-Game

Play Rock Paper Scissors with your computer. The project contains Convolutional neural network, which detects user's hand and gesture and calculate's result accordingly.

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
