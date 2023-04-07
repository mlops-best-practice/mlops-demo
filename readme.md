# MLOPS DEMO
Đây là một ví dụ đơn giản về dự án MLOps, cung cấp quy trình huấn luyện và triển khai các mô hình học máy.

## INTRODUCTION

MLOps là một phương pháp để quản lý và triển khai các mô hình học máy trong một môi trường sản xuất. Nó kết hợp các quy trình, công cụ và kỹ thuật để tự động hóa việc huấn luyện và triển khai các mô hình.

Mục tiêu của ví dụ này giúp các bạn hiểu rõ về quy trình, luồng hoạt động của một dự án MLops có sự kết hợp giữa những thành viên trong một dự án Machine Learning.

## MACHINE LEARNING WORKFLOW

ML Workflow có thể hiểu là một quy trình được sử dụng để triển khai và quản lý các mô hình học máy. Với một workflow lý tưởng, sẽ giúp phối hợp giữa khoa học dữ liệu và kỹ thuật phần mềm khi xây dựng, huấn luyện, triển khai và duy trì các mô hình học máy trở lên dễ dàng, có thể được đưa vào sản xuất một cách nhanh chóng, an toàn và hiệu quả. 

Trong ML WORKFLOW gồm có rất nhiều phase khác nhau, mỗi phase có mục đích và nhiệm vụ khác nhau. Trong đó, có 2 phase cơ bản nhất: Development &  Production.

###  DEVELOPMENT PHASE

###  PRODUCTION PHASE

## SETUP
### Create environments
Chúng ta cần tạo một môi trường ảo để chạy các bước tiếp theo. Bạn có thể sử dụng conda hoặc virtualenv để tạo một môi trường ảo.
Ví dụ, để tạo một môi trường ảo sử dụng `conda`, hãy chạy lệnh sau:

```
conda create --name mlops-demo python=3.8
```

### Activate environments
Khi môi trường ảo đã được tạo, bạn cần kích hoạt nó để sử dụng các gói và thư viện cài đặt trong môi trường đó.

Để kích hoạt môi trường sử dụng conda, hãy chạy lệnh sau:
``` 
conda create --name mlops-demo python=3.8
```
## Setup varible environment
Chúng ta cần cài đặt một số biến môi trường để sử dụng cho quá trình huấn luyện và triển khai. Hãy sửa đổi các giá trị trong tệp .env để phù hợp với dự án của bạn.
```
cp .env.example .env
```
## TRAINING DEMO
## Training on Notebook
Bạn có thể sử dụng Jupyter Notebook để huấn luyện mô hình. Hãy mở tệp `notebooks/train.ipynb` và làm theo các hướng dẫn trong notebook.
## Training by Script file
Ngoài việc sử dụng Jupyter Notebook, bạn có thể huấn luyện mô hình bằng cách chạy một tệp script. Hãy sử dụng lệnh sau để huấn luyện mô hình:

## INFERENCE DEMO

## AUTHOR
Pham Manh - AI Engineer
