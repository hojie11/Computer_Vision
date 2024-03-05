# Faster-RCNN 
Faster R-CNN: Towards Real-Time Object Detection with Region Proposal Networks 리뷰

기존 Fast RCNN 모델은 Selective search algorithm을 통해 region proposal을 추출하기 때문에 학습 및 Detection 속도가 느리며 Detection 과정이 end to end로 이루어지지 않음</br></br>

Faster RCNN은 Detection 하고자 하는 물체에 대한 후보 영역을 추출하는 네트워크인 Region Proposal Network(PRN)을 도입하여 기존의 문제점을 해결하였음</br>
PRN은 객체의 영역을 보다 정확하게 추출할 수 있또록 다양한 크기의 **Anchor box**(bbox)를 도입하여, 해당 영역을 RCNN 네트워크에 전달하여 객체의 클래스와 **Anchor box**의 위치를 Prediction함

<p align='center'>
    <img src="assets/architecture.JPG" width=70% height=70%>
</p></br>

전체 학습 과정은 아래와 같음
1. 입력 이미지로부터 Featuer map을 추출함
2. 추출한 Feature map은 PRN을 통과해 객체에 대하여 적절한 **Anchor box**를 계산함
3. 1)과 2)의 결과물에 ROI Pooing을 수행하여 고정된 크기의 feature map을 생성함
4. RCNN 네트워크를 통해 해당 Feature map에 대한 Class와 Bounding box 위치를 계산함

## 학습
### 학습환경
```
OS : LINUX 20.04
CPU : Intel(R) Xeon(R) Silver 4214R CPU @ 2.40GHz
GPU : NVIDIA RTX A6000(VRAM 48G)
RAM : 128G
```

## 참고
1. chenyuntc의 github [[page](https://github.com/chenyuntc/simple-faster-rcnn-pytorch.git)]

2. sangnekim의 github [[page](https://github.com/sangnekim/faster-rcnn-for-studying)]