# GenieNet  

CGI Detection using Deep Convolutional Neural Networks
  
-----  
<img src="https://user-images.githubusercontent.com/42594454/133894460-f87e6734-803d-465c-95a9-938608f12b9e.gif" width="100%">   

## Inspiration
 Computer generated imagery is the application of computer graphics to create or contribute to images in art, printed media, video games and simulations. There are a few popular tools and techniques used in computer generated imagery like Photoshop, green screen, generative adversial networks and animative modelling. Besides the cool and satisfactory results of CGI, there are few situations where it becomes a great threat to the society. They look very realistic such that it becomes difficult to distinguish them from photographic images and they are immune to the state-of-the-art deep fake detection techniques. There is a high risk of using these images in fraudulent activities as a replacement to the original face for faking the identity. Also, there are significant records of portraying false morphed images of an individual in social media.  

## What it does
The webapp takes in the suspicious image as input and makes prediction using the pretrained model. The result comprises of two components:
  - Photographic confidence
  - Tampered confidence  

## How we built it
We have constructed a convolutional neural network and trained it on multiple image datasets containing real and tampered images. The model with least generalization error is chosen and saved. Transfer learning is implemented using the pretrained model for faster inference and hence the predictions are super fast and accurate.  

![](https://user-images.githubusercontent.com/42594454/133894966-24704241-968e-4240-a12d-a5bc8685512e.png)  
   
## Deployment  
We have deployed our web app on Microsoft Azure Cloud ensuring that it stays up stable for a long time with the efficient hosting management services of Microsoft.  
Deployed on  - https://genienet.azurewebsites.net

### Video demo  
YouTube : https://youtu.be/0jr3Uxq2tG0

## Challenges we ran into
- The deployment of the model into the django app took very long than expected, since we tried to run the inference on PyTorch CPU version.
- Building the UI is also a time-consuming activity and it demanded a full-fledged work time.  

## What we learned
- We learnt how to implement transfer learning for Convolutional Neural Network (CNN) models and deploying them on to the django application.
- We also learnt some basic video editing to make the video pitch for the project. The challenging part is to build the video very quick by learning parallely.  

## What's next for GenieNet
- We have planned to improvise the accuracy of the model by collecting more samples of the photographic and computer graphic images and thinking to integrate this system with the deep fake detection algorithms for building a highly robust system of image forgery detection.

## Screenshots 

<img src="https://user-images.githubusercontent.com/70621058/133917578-3487427a-c843-48aa-a45e-1460454b9f3d.PNG" width="33%"><img src="https://user-images.githubusercontent.com/70621058/133918450-59b160e2-f3fb-4096-b830-ed4f0f1f9463.PNG" width="33%"><img src="https://user-images.githubusercontent.com/70621058/133917588-04610033-7134-4372-a0d7-67bc226918e0.PNG" width="33%"><img src="https://user-images.githubusercontent.com/70621058/133917582-662d9c01-02a6-4672-814e-39626ed1ba5f.PNG" width="33%"><img src="https://user-images.githubusercontent.com/70621058/133917586-af29e6bb-1384-448f-a777-74fad8302d11.PNG" width="33%"><img src="https://user-images.githubusercontent.com/70621058/133917585-ebe0b540-f710-4abf-a526-b3ef024ed63a.PNG" width="33%">
