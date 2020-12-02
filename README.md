# Depression-Predicter
Use audio data to predict the probability of having depression.

1. Description of dataset
2. Model
3. Usage

### Description of dataset

We use MODMA dataset which contains the audio data of people who ill with depression and be healthy.

Audio is another non-invasive accessible physiological data, and studies have shown that mental disorders will be causing the patients’ audio data to differ from healthy controls, said in introduction paper.

### Model

Baidu Ai-Studio is a good choice for freshman in deep learning area. we just need prepare dataset and send it to EasyDL platform, than we can use the model by sending HTTP-requests to baidu API.

### Usage

This repository is a flask project, providing user interface. A web is established for collecting audio data, then send to the model we trained earlier. Predict and relative recommendation well be displayed in the web page. User can have a knowledge of self mental-health state.



