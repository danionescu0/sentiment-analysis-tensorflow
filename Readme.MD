# Sentiment Analisys with Tensorflow

Forked from: https://github.com/katakonst/sentiment-analysis-tensorflow

This is a example of sentiment analisys for romanian and english language built up on tensorflow and tflearn

###Enhancements:

* added a webserver to expose a api

* added  Docker containers

###Swagger: 
http://localhost:8001/docs

###Usage with curl
````bash
curl -X 'PUT' \
  'http://localhost:8001/api/analize' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "phrase": "Ceva text rau"
}'
````
Response body:
````json
{
  "phrase": "Ceva text rau",
  "language": "ro",
  "positive": 0.020164920017123222,
  "negative": 0.979835033416748
}
````


###Running in dev mode
````bash
cd project_folder
uvicorn webserver:app --reload --host 0.0.0.0 --port 8001

````

###Running with docker compose
````bash
docker-compose up
````

###Usage with docker
Language parameter can be en/ro
````bash
docker run -e "language=en" --publish 8080:8001 danionescu/sentiment-analysis-tensorflow:latest
````


# Accuracy
After 10 epochs for romanian dataset  :
```sh
Training Step: 5360  | total loss: 0.05475 | time: 51.239s
| Adam | epoch: 010 | loss: 0.05475 - acc: 0.9881 | val_loss: 0.53884 - val_acc: 0.8536 -- iter: 17144/17144
```
After 10 epochs for english dataset  :
```sh
Training Step: 13620  | total loss: 0.05636 | time: 142.459s
| Adam | epoch: 010 | loss: 0.05636 - acc: 0.9940 | val_loss: 0.18359 - val_acc: 0.9396 -- iter: 43561/43561
```
# How to use it
### Predict
Pass `en` for English or `ro` for Romanian as arg to command line followed by text
```sh
$ python predict.py en "Food is awesome"
negative=0.022818154
positive=0.97718185
```

```sh
$ python predict.py ro "Mancarea este proasta"
negative=0.9629853
positive=0.037014768
```

### Train
Pass `en` for English or `ro` for Romanian as arg to command line
```sh
$ python train.py en
```
# Datasets
Positive dataset is more numerous than the negative one. This may cause a drop in accuracy.
### English dataset
   Dataset of reviews from yelp and imdb reviews
##### Train:
   - neg: 10090
   - pos: 33532
   - total: 43561
##### Test
   - neg: 10228
   - pos: 33394
   - total: 43622

### Romanian dataset
  Dataset of products and movies reviews
##### Train:
   - neg: 6370
   - pos: 10774
   - total: 17144
##### Test
   - neg: 4427
   - pos: 5840
   - total: 10267
